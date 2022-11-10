from django.urls import path

from . import views
from .views import rooms, room, create

urlpatterns = [
    path('meeting/<int:id>', views.detail, name="meeting"),
    path('rooms', rooms, name="rooms"),
    path('rooms/room/<int:id>', room, name="room"),
    path('create/', create, name="create "),
]