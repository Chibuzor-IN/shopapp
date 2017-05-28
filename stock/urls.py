from django.conf.urls import url
from . import views
from .views import Home

app_name = "stock"
urlpatterns = [
    url(r'^$', Home.as_view(), name = "home"),
    url(r'^add_item/', views.add_item, name = "add_item"),
    url(r'^edit_items/', views.edit_items, name = "edit_items"),
    url(r'^delete_items/', views.delete_items, name = "delete_items"),
    url(r'^search_to_view/', views.search_to_view, name = "search_to_view"),
    url(r'^search_to_edit/', views.search_to_edit, name = "search_to_edit"),
]
