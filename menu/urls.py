from django.urls import path

from .views import MenuView

urlpatterns = [
    path("menu/<slug:menu_name>/", MenuView.as_view(), name='menu'),
    path("menu/<slug:menu_name>/<slug:item_name>/", MenuView.as_view(), name='menu_item'),
]
