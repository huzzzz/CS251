from django.conf.urls import url, include
from adminlogin.views import adminlogout, main_page, addcourse, addstudent,adminPage,check


urlpatterns= [
	url(r'^$', main_page, name='main_page'),
	# url(r'^admin_poll/', include('polls.urls')),
	url(r'^check', check, name='check'),
	# url(r'^login/', login, name='login'),
	url(r'^logout/', adminlogout, name='logout'),
	url(r'^addcourse/', addcourse, name ='addcourse'),
	url(r'^addstudent/',addstudent, name='addstudent'),
	url(r'^adminPage/',adminPage, name='adminPage'),
]