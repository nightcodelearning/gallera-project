from django.conf.urls import url
from django.conf import settings

from django.views.static import serve



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

if settings.DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)$', serve, {'document_root':
                                                            settings.MEDIA_ROOT}))
