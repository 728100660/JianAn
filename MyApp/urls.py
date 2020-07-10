# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^test/',views.test,name='test'),
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^get_number/',views.get_number,name='get_number'),
    url(r'^get_user_info/',views.get_user_info,name='get_user_info'),
    url(r'^modify_information/',views.modify_information,name='modify_information'),
    url(r'^set_status/',views.set_status,name='set_status'),
    url(r'^appointment/',views.appointment,name='appointment'),
    
}