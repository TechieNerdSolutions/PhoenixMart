from django.urls import path
from . import views

app_name = 'vendor'

urlpatterns = [
    path('dashboard/', views.vendor_dashboard_view, name='vendor-dashboard'),
    path('profile/', views.vendor_profile_view, name='vendor-profile'),
    path('profile/update/', views.vendor_profile_update_view, name='vendor-profile-update'),
    path('delete/request/', views.vendor_delete_request_view, name='vendor-delete-request'),
    path('list/', views.vendor_list_view, name='vendor-list'),
    path('detail/<int:vendor_id>/', views.vendor_detail_view, name='vendor-detail'),
    path('products/<int:vendor_id>/', views.vendor_products_view, name='vendor-products'),
    path('create-product/', views.create_product_view, name='create-product'),
    path('update-product/<int:product_id>/', views.update_product_view, name='update-product'),
    path('delete-product/<int:product_id>/', views.delete_product_view, name='delete-product'),
    path('orders/', views.vendor_orders_view, name='vendor-orders'),
    path('order-detail/<int:order_id>/', views.vendor_order_detail_view, name='vendor-order-detail'),
    path('order-status-update/<int:order_id>/', views.vendor_order_status_update_view, name='vendor-order-status-update'),
    path('order-delete/<int:order_id>/', views.vendor_order_delete_view, name='vendor-order-delete'),
    path('become-vendor/', views.become_vendor_view, name='become-vendor'),
]

urlpatterns += [
    path('become-vendor/submit/', views.become_vendor_submit_view, name='become-vendor-submit'),
]
