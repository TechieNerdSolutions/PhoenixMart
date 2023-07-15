from django import views
from django.urls import path, include
from core.views import index, calendar, category_list_view, category_product_list__view, contact, customer_dashboard, make_address_default, purchase_guide, terms_of_service, privacy_policy, about_us, ajax_contact_form, wishlist_view

app_name = "core"

urlpatterns = [

    # Homepage
    path("", index, name="index"),

    # Category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list__view, name="category-product-list"),

    # Dahboard URL
    path("dashboard/", customer_dashboard, name="dashboard"),

    # wishlist page
    path("wishlist/", wishlist_view, name="wishlist"),

    # Making address defauly
    path("make-default-address/", make_address_default, name="make-default-address"),

    path("contact/", contact, name="contact"),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),

    path("about_us/", about_us, name="about_us"),
    path("purchase_guide/", purchase_guide, name="purchase_guide"),
    path("privacy_policy/", privacy_policy, name="privacy_policy"),
    path("terms_of_service/", terms_of_service, name="terms_of_service"),
]