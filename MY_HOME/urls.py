"""MY_HOME URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from MY_HOME.views import IndexView, AboutView, UserCreateView, UserCreateDoneTV, CreateView
from bookmark.views import BookmarkDV, BookmarkLV, BookmarkCV,  BookmarkUV, BookmarkRV
from blog.views import PostLV, PostCV, PostDV, PostUV

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('bookmark/', BookmarkLV.as_view(),
         name='bookmark_index'),
    path('bookmark/delete/<pk>', BookmarkRV.as_view(), name='bookmark_delete'),
    path('bookmark/update/<pk>', BookmarkUV.as_view(), name="bookmark_update"),
    path('bookmark/create', BookmarkCV.as_view(), name='bookmark_create'),
    path('bookmark/<pk>', BookmarkDV.as_view(), name='bookmark_detail'),

    path('accounts/register/', UserCreateView.as_view(),name='register' ),

    path('about/', AboutView.as_view(), name="about"),
    path('accounts/',
         include('django.contrib.auth.urls')),

    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    path('blog/', PostLV.as_view(), name="blog"),
    path('blog/create', PostCV.as_view(), name="blog_create"),
    path('blog/update/<pk>', PostUV.as_view(), name="blog_update"),
    path('blog/delete/<pk>', PostDV.as_view(), name="blog_delete"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
