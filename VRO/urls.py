"""VRO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import homepage.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage.views.home, name="home"),
    path('about/', homepage.views.about, name="about"),
    path('map/', homepage.views.map, name="map"),
    path('collection/', homepage.views.collection, name="collection"),    
    path('notice/', homepage.views.notice, name="notice"),
    path('signup/', homepage.views.signup, name='signup'),
    path('login/', homepage.views.login, name='login'),
    path('logout/', homepage.views.logout, name='logout'),
    path('OUTER/', homepage.views.OUTER, name='OUTER'),
    path('SHOES/', homepage.views.SHOES, name='SHOES'),
    path('BOTTOM/', homepage.views.BOTTOM, name='BOTTOM'),
    path('ACC/', homepage.views.ACC, name='ACC'),
    path('top/', homepage.views.top, name='top'),
    path('homepage/<int:notice_id>/detail', homepage.views.detail, name='detail'),
    path('notice/<int:pk>/comment', homepage.views.comment_new, name="comment_new"),
    path('comment/<int:comment_id/remove', homepage.views.comment_remove, name="comment_remove"),
    path('qna/', homepage.views.qna, name="qna"),
    path('homepage/<int:qna_id>/detail2', homepage.views.detail2, name='detail2'),
    path('homepage/new/', homepage.views.new, name='new'),
    path('homepage/create/', homepage.views.create, name='create'),
]
