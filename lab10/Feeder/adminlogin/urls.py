from django.conf.urls import url
from adminlogin.views import logout, main_page, addcourse, addinstr, addstudent


urlpatterns= [
	url('r^$/', main_page, name='main_page'),
	url('r^logout/', logout, name='logout'),
	url('r^addinstructor/', addinstr, name='addinstr'),
	url('r^addcourse/', addcourse, name ='addcourse'),
	url('r^addstudent',addstudent, name='addstudent'),
]