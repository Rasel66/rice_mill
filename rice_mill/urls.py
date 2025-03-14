from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    path('home-page', home_page_view, name='home_page'),
    path('ledger/', ledger_page_view, name='ledger'),
    path('customer-create/', customer_creation_view, name='customer_create'),
]
