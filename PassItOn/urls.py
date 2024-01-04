"""
URL configuration for PassItOn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Core import views as core_views
from Users import views as user_views
from Offers import views as offer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'),
    path('register_page/', user_views.register_page, name='register_page'),
    path('register_action/', user_views.register_action, name='register_action'),
    path('login_page/', user_views.login_page, name='login_page'),
    path('login_action/', user_views.login_action, name='login_action'),
    path('logout_action/', user_views.logout_action, name='logout_action'),
    path('add_offer_page/', offer_views.add_offer_page, name='add_offer_page'),
    path('add_offer/', offer_views.add_offer, name='add_offer'),
    path('offers_after_search_page/', offer_views.offers_after_search_page, name='offers_after_search_page'),
    path('profile_page/', user_views.profile_page, name='profile_page'),
    path('edit_info_page/', user_views.edit_info_page, name='edit_info_page'),
    #path('edit_info_action/', user_views.edit_info_action, name='edit_info_action'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)