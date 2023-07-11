"""Exploratory_Visual_Sequence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from Exploratory_Visual_Sequence import settings
from user import views as user_views
from admins import views as admin_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('^$',user_views.index,name="index"),
    url('user/register', user_views.register, name="register"),
    url('user/userpage',user_views.userpage,name="userpage"),
    url('user/details', user_views.details, name="details"),
    url('user/products/(?P<pk>\d+)/$', user_views.all_products, name="all_products"),
    url(r'^Cart/$',user_views.cart,name='cart'),
    url(r'^viewreview/(?P<pk>\d+)/$',user_views.viewreview,name='viewreview'),
    url('user/visual_sequence', user_views.visual_sequence, name="visual_sequence"),
    url('user/update_details',user_views.update_details,name="update_details"),
    url('categoryanalysis/(?P<chart_type>\w+)',user_views.categoryanalysis_chart,name="categoryanalysis_chart"),


    url('login',admin_views.login,name="login"),
    url('adminpage/',admin_views.admin_page,name="admin_page"),
    url('adminhomepage/',admin_views.homepage,name="homepage"),
    url('adminuserdetails/',admin_views.userdetails,name="userdetails"),
    url('cateanalysis/(?P<chart_type>\w+)',admin_views.cateanalysis,name="cateanalysis"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)