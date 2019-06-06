from django.urls import path
from .views import booking
from . import views

app_name = 'booking'
urlpatterns = [
    path('index/', views.index, name= "index"),
    path('booking/', booking, name="booking"),
    path('add/', views.FieldCreateView.as_view(), name="create-field"),
    path('', views.FieldList.as_view(), name='field_list'),
    path('view/<int:pk>/', views.FieldView.as_view(), name='field_view'),
    path('edit/<int:pk>/', views.FieldUpdate.as_view(), name='field_edit'),
    path('delete/<int:pk>/', views.FieldDelete.as_view(), name='field_delete')
]
