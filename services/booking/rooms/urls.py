from django.urls import include, path

from rooms import views as room_views

urlpatterns = [
    path('<int:room_id>/book', room_views.book),
    path('<int:room_id>/book404', room_views.book404),
    path('<int:room_id>/error', room_views.error),
]