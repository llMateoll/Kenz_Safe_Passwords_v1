from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('' , views.home , name='home'),
    path('edit/<int:clave_id>', views.edit, name="edit"),
    path('delete/<int:clave_id>', views.delete, name="delete"),
    #path('/' , views.AddClaves, name='newpassword'),

]