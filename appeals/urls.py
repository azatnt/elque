from django.urls import path

from appeals.views import complete_appeal, create_appeal, get_appeal, rector_clients, update_appeal_status


urlpatterns = [
    path('create_appeal/', create_appeal, name='create_appeal'),
    path('get_appeal/', get_appeal, name='get_appeal'),
    path('update_appeal_status/', update_appeal_status, name='update_appeal_status'),
    path('rector_clients/', rector_clients, name='rector_clients'),
    path('complete_appeal/', complete_appeal, name='complete_appeal'),
]
