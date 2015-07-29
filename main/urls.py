from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),
]
