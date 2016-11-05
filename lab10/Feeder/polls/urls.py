from django.conf.urls import url

from polls.views import adminlogin, register, mainpage

# urlpatterns = patterns[
#     # url(r'^about/$', views.about, name='about'),
#     # url(r'^category/(?P<category_name_url>\w+)$', views.category, name='category'),
#     # url(r'^add_category/$', views.add_category, name='add_category'),
#     # url(r'^category/(?P<category_name_url>\w+)/add_page/$', views.add_page, name='add_page'),
#      # ADD NEW PATTERN!
# ]
urlpatterns = [
	url(r'^register/', register, name = 'register'),
    # url(r'^splogin/', include('adminlogin.urls')),
    url(r'^login/', adminlogin, name = 'login'),
    url(r'^home/', mainpage, name = 'mainpage'),
]	