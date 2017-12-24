from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.contextfunc),
    url(r'^logout$',views.logout),
    url(r'^addappt$',views.addappointment),
    url(r'^edit/(?P<appointment_id>\d+)$',views.update),
    url(r'^update/(?P<appointment_id>\d+)$',views.editing),
    url(r'^delete/(?P<appointment_id>\d+)$',views.deleting),
    url(r'^dashboard$',views.dashboard),

    # url(r'^ideatyped$',views.addideatodb),
    # url(r'^logout$',views.logout),
    # url(r'^put_likes_indatabase$',views.likesindatabase),
    # url(r'^namelink/(?P<person_id>\d+)$',views.contextfunctwo),
    # url(r'^wholikes/(?P<ideaid>\d+)$',views.wholikes),
    # url(r'^aliaslink/(?P<person_id>\d+)$',views.contextfunctwo),
    # url(r'^deleteidea_from_database/(?P<idea_id>\d+)$',views.deletefromdatabase),

]
