from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    path('home-page', home_page_view, name='home_page'),
    path('ledger/', ledger_page_view, name='ledger'),
    path('customer-create/', customer_creation_view, name='customer_create'),
    path('customer-update/<int:pk>', customer_update_view, name='customer_update'),
    path('customer-delete/<int:pk>', customer_delete_view, name='customer_delete'),

    path('item-types/index/', items_types_index_view, name='item_types_index'),
    path('item-types/create/', items_types_create_view, name='item_types_create'),
    path('item-types/update/<int:pk>', items_types_update_view, name='item_types_update'),
    path('item-types/delete/<int:pk>', items_types_delete_view, name='item_types_delete'),

    path('items/index/', items_index_view, name='items_index'),
    path('items/create/', items_create_view, name='items_create'),
    path('items/update/<int:pk>', items_update_view, name='items_update'),
    path('items/delete/<int:pk>', items_delete_view, name='items_delete'),

    path('uom/index/', uom_index_view, name='uom_index'),
    path('uom/create/', uom_create_view, name='uom_create'),
    path('uom/update/<int:pk>', uom_update_view, name='uom_update'),
    path('uom/delete/<int:pk>', uom_delete_view, name='uom_delete'),

    path('party-invoice/index', party_invoice_index_view, name='party_invoice_index'),
    path('party-invoice/create', party_invoice_create_view, name='party_invoice_create'),
    path('party-invoice/update/<int:pk>', party_invoice_update_view, name='party_invoice_update'),
    path('party-invoice/delete/<int:pk>', party_invoice_delete_view, name='party_invoice_delete'),

    path('party-invoice-child/index/', party_invoice_child_index_view, name='party_invoice_child_index'),
    path('party-invoice-child/create/', party_invoice_child_create_view, name='party_invoice_child_create'),
    path('party-invoice-child/update/<int:pk>', party_invoice_child_update_view, name='party_invoice_child_update'),
    path('party-invoice-child/delete/<int:pk>', party_invoice_child_delete_view, name='party_invoice_child_delete'),

    path('add-items-details/index/', addItems_details_index_view, name='add_items_details_index'),
    path('add-items-details/create/', addItems_details_create_view, name='add_items_details_create'),
    path('add-items-details/update/<int:pk>', addItems_details_update_view, name='add_items_details_update'),
    path('add-items-details/single/<int:pk>', addItems_sigle_details_view, name='add_items_single_details'),
    path('add-items-details/delete/<int:pk>', addItems_details_delete_view, name='add_items_details_delete'),

    path('sells-customer/index/', sells_customer_index_view, name='sells_customer_index'),
    path('sells-customer/create/', sells_customer_create_view, name='sells_customer_create'),
    path('sells-customer/update/<int:pk>', sells_customer_update_view, name='sells_customer_update'),
    path('sells-customer/delete/<int:pk>', sells_customer_delete_view, name='sells_customer_delete'),

    path('sells-customer/transaction/index/', sells_customer_transaction_index_view, name='sells_customer_transaction_index'),
    path('sells-customer/transaction/create/', sells_customer_transaction_create_view, name='sells_customer_transaction_create'),
    path('sells-customer/transaction/update/<int:pk>', sells_customer_transaction_update_view, name='sells_customer_transaction_update'),
    path('sells-customer/transaction/single-details/<int:pk>', sells_customer_transaction_single_view, name='sells_customer_transaction_single'),
    path('sells-customer/transaction/delete/<int:pk>', sells_customer_transaction_delete_view, name='sells_customer_transaction_delete'),

    path('stocks/', stock_index_view, name='stocks'),

    path('party-invoice/generation/<int:pk>', party_invoice_generation_view, name='party_invoice_generation'),
    path('sells-customer/invoice/generation/<int:pk>', sells_customer_invoice_generation_view, name='sells_customer_invoice_generation'),

    # AJAX URL
    path('ajax/load-phone-no/', ajax_load_customer_phone_no, name='ajax_load_customer_phone_no'),
    path('ajax/load-address/', ajax_load_customer_address, name='ajax_load_customer_address'),
    path('ajax/load-phone-no/', ajax_load_sells_customer_phone_no, name='ajax_load_sells_customer_phone_no'),
    path('ajax/load-address/', ajax_load_sells_customer_address, name='ajax_load_sells_customer_address'),
]
