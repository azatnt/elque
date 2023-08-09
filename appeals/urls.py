from django.urls import path

from appeals.views import complete_appeal, create_appeal, rector_clients


urlpatterns = [
    path('create_appeal/', create_appeal, name='create_appeal'),
    path('rector_clients/', rector_clients, name='rector_clients'),
    path('complete_appeal/', complete_appeal, name='complete_appeal'),
]
