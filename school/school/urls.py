"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from schoolapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.home_view),
    url(r'^home/',views.home_view),
    url(r'^contact/',views.contact_view),
    url(r'^course',views.course_view),
    url(r'^about/',views.about_view),
    url(r'^notifications/',views.notifications_view),
    url(r'^registrations/',views.Registrations_view),
    url(r'^login/',views.login_view),
]
urlpatterns +=staticfiles_urlpatterns()