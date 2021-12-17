"""mgn2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from posts import views


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('delete/<slug:slug>/', views.delete, name='delete'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),
    path("contact/<slug:slug>/", views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('api/', include('posts.api.urls')),
    path('', include('posts.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('index', views.index),
    path('post/<int:id>/', views.post_detail)
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

]