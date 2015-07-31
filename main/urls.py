from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),

    url(r'^register/$', 'main.views.register', name='register'),
    url(r'^login/$', 'main.views.login', name='login'),
    url(r'^logout/$', 'main.views.logout', name='logout'),

    url(r'^create-post/$', 'main.views.create_post', name='create_post'),
    url(r'^get-posts/$', 'main.views.get_posts', name='get_posts'),

    url(r'^create-favorite/$', 'main.views.create_favorite', name='create_favorite'),
    url(r'^delete-favorite/$', 'main.views.delete_favorite', name='delete_favorite'),
    url(r'^get-favorites/$', 'main.views.get_favorites', name='get_favorites'),
    url(r'^(?P<username>\w+)/favorites/$', 'main.views.view_favorites', name='view_favorites'),
]
