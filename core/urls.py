from django.urls import path
from rooms import views as room_views

app_name = "core"  # config.urls의 namesapce와 똑같아야 함

urlpatterns = [
    path("", room_views.all_rooms, name="home"),
]
