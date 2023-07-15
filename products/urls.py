from django import views
from django.urls import path, include
from products.views import  product_list_view, product_detail_view, tag_list, ajax_add_review, search_view, filter_product, add_to_cart, cart_view, delete_item_from_cart, update_cart, checkout_view, payment_completed_view, payment_failed_view, order_detail,  add_to_wishlist, remove_wishlist

app_name = "products"

urlpatterns = [

    # Product
    path("products/", product_list_view, name="product-list"),
    path("products/<pid>/", product_detail_view, name="product-detail"),

    
    # Tags
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),

    # Add Review
    path("ajax-add-review/<int:pid>/", ajax_add_review, name="ajax-add-review"),

    # Search
    path("search/", search_view, name="search"),

    # Filter product URL
    path("filter-products/", filter_product, name="filter-product"),

    # Add to cart URL
    path("add-to-cart/", add_to_cart, name="add-to-cart"),

    # Cart Page URL
    path("cart/", cart_view, name="cart"),

    # Delete ITem from Cart
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),

    # Update  Cart
    path("update-cart/", update_cart, name="update-cart"),

      # Checkout  URL
    path("checkout/", checkout_view, name="checkout"),

    # Paypal URL
    path('paypal/', include('paypal.standard.ipn.urls')),

    # Payment Successful
    path("payment-completed/", payment_completed_view, name="payment-completed"),

    # Payment Failed
    path("payment-failed/", payment_failed_view, name="payment-failed"),

    # Order Detail URL
    path("dashboard/order/<int:id>", order_detail, name="order-detail"),

    # adding to wishlist
    path("add-to-wishlist/", add_to_wishlist, name="add-to-wishlist"),

    # Remvoing from wishlist
    path("remove-from-wishlist/", remove_wishlist, name="remove-from-wishlist"),

]