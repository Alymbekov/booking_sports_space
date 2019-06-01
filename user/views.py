from django.conf import settings
from django.http import Http404
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib.auth import get_user_model, views as auth_views
from django.urls import reverse, reverse_lazy
from django.utils.http import base36_to_int, int_to_base36
from django.utils.translation import ugettext_lazy as _

from django.template.loader import render_to_string
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from user.forms import UserCreationForm


def home (request):
    return render(request, 'profile/home.html')
def logout(request):
    request.sission.flush()
    return redirect('/user/')

class LoginView(auth_views.LoginView):
    template_name = 'profile/login.html'

class SignUpView(CreateView):
    template_name = 'user/signup.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('user:signup-done')

    def form_valid(self, form):
        ret = super().form_valid(form)

        site_name = 'Local Forum'
        domain = 'localhost'

        uid = int_to_base36(self.object.id)
        token = default_token_generator.make_token(self.object)
        mail_context = {

            'email': self.object.email,
            'domain': domain,
            'site_name': site_name,
            'uid': uid,
            'user': self.object,
            'token': token,
            'url': self.request.build_absolute_uri(reverse(
                'user:signup-confirm',
                kwargs={'uidb36': uid, 'token': token}

            ))
        }

        send_mail(

            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.object.email],
            message='',
            subject=_('Спасибо, ваша регистрация прошла успешно!'),
            html_message=render_to_string(template_name='user/signup.html', context=mail_context),

        )

        return ret

class SignupDoneView(TemplateView):
    template_name = 'user/signup-done.html'

class SignUpConfirmView(View):
     def get(self, request, *args, **kwargs):

        uidb36 = kwargs.get('uidb36')
        token = kwargs.get('token')

        try:
            uid_int = base36_to_int(uidb36)

        except ValueError:
            raise Http404

        user = get_object_or_404(get_user_model(), id=uid_int)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()

        login(request, user=user)
        return redirect('forum:home')




