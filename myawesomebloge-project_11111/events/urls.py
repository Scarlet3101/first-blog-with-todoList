from django.urls import path
from .import views
urlpatterns = [

    path('',views.home, name="home"),
    path('<int:post_id>/',views.specific_post_in_home, name ="specific_post_in_home"),
]
