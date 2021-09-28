"""app URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from core.views import success_view, logout_view, projects_view, projects_page_view, create_project_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('api/', include('projects.urls')),

    path('', include([
        path('login/', LoginView.as_view(template_name="web/login.html"), name="web-login"),
        path('login1', LoginView.as_view(template_name="web/login1.html"), name="web-login1"),
        path('', success_view, name="success-view"),
        path('projects/', projects_view, name="projects_view"),
        path('projects-page/', projects_page_view, name="projects_page_view"),
        path('projects-page/<pk>/', projects_page_view, name="projects_page_view"),
        # re_path(r'^projects-page/()', projects_page_view, name="projects_page_view"),
        # path('projects', projects_view.as_view(template_name="web/projects.html"), name="projects-view"),
        path('logout/', LogoutView.as_view(template_name="web/logout.html"), name="logout_user"),
        path('create-project/', create_project_view.as_view(), name='select-client-view'),
    ])),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
