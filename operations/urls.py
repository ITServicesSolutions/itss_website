from django.urls import path
from .views import (
    run_migrations,
    collect_static,
    create_backup,
    get_operations_status
)

urlpatterns = [
    path('', get_operations_status, name='operations-status'),
    path('run-migrations/', run_migrations, name='run-migrations'),
    path('collect-static/', collect_static, name='collect-static'),
    path('create-backup/', create_backup, name='create-backup'),
]
