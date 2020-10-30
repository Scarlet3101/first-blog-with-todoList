"""myawesomebloge URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
import events.views
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', events.views.home, name = 'home'), # home page
    path('posts/',include('blog.urls')),
    path('',include('events.urls')),
    path('tasks/',include('task.urls')),
    path('return_json',events.views.return_json,name = 'return_json'),

    path('add_post',views.add_post,name ="add_post"),
    # path('addData/', views.AddData, name='add_data'),
    path('show_all_data/',views.show_all_data,name ="show_all_data"),
    path('update_news/<str:post_id>',views.update_news, name ="update_news"),
    path('edit_news/',views.edit_news, name ="edit_news"),
    path('del_news/<str:post_id>',views.del_news, name ="del_news"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
