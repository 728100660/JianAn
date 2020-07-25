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
    url(r'^sent_notify/',views.sent_notify,name='sent_notify'),
    url(r'^set_status/',views.set_status,name='set_status'),
    url(r'^appointment/',views.appointment,name='appointment'),
    url(r'^get_appointment_info/',views.get_appointment_info,name='get_appointment_info'),
    url(r'^get_notify/',views.get_notify,name='get_notify'),
    url(r'^get_place/',views.get_place,name='get_place'),
    url(r'^get_ab_info/',views.get_ab_info,name='get_ab_info'),
    url(r'^get_latest_notify/',views.get_latest_notify,name='get_latest_notify'),
    url(r'^bind/',views.bind,name='bind'),
    url(r'^upload_file/',views.upload_file,name='upload_file'),
    url(r'^get_stream_people/',views.get_stream_people,name='get_stream_people'),
    url(r'^get_stream_people_week/',views.get_stream_people_week,name='get_stream_people_week'),
}
