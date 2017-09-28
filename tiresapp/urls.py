from django.contrib.staticfiles.urls import static
from django.conf.urls import url

from tires import settings
from tiresapp import views

urlpatterns = [
    url(r'^api/tires/$', views.TireList.as_view()),
    url(r'^api/tires/(?P<pk>[0-9]+)/$', views.TireDetail.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
