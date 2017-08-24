from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^register_chick$',
        views.RegisterChickView.as_view(),
        name='register_chick',
    ),
    url(
        r'^get_chick$',
        views.GetChickView.as_view(),
        name='get_chick',
    ),
    url(
        r'^deleted_chick$',
        views.DeleteChickView.as_view(),
        name='delete_chick',
    ),
]