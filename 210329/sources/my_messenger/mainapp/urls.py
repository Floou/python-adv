from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index),
    path('dialog/<int:dialog_id>/', mainapp.dialog, name='dialog'),
]
