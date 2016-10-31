from django.conf.urls import include, url
from django.contrib import admin
from catalog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'jasmines.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index, name='index'),
    url(r'^register/',views.register, name='register'),
    url(r'^$',views.index, name='index'),
    url(r'^signin/',views.signin, name='signin'),

]
