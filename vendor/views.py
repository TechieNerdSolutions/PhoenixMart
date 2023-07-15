from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from regex import E
from requests import session
from taggit.models import Tag
from .models import Vendor
from userauths.models import ContactUs, Profile
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib.auth.decorators import login_required

import calendar
from django.db.models import Count, Avg
from django.db.models.functions import ExtractMonth
from django.core import serializers

from products.models import Product, CartOrder
from core.models import Address
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product, ProductImages
from products.forms import ProductForm



def vendor_dashboard_view(request):
    user = request.user
    vendor = Vendor.objects.get(user=user)
    products = Product.objects.filter(vendor=vendor).order_by("-id")
    paginator = Paginator(products, 10)
    page_number = request.GET.get("page", 1)
    products = paginator.get_page(page_number)
    context = {
        "products": products,
    }
    return render(request, "vendor/vendor-dashboard.html", context)

def become_vendor_view(request):
    user = request.user

    if not request.user.is_authenticated:
        return redirect("login")

    if Vendor.objects.filter(user=user).exists():
        return redirect("vendor:vendor-dashboard")

    form = VendorForm(request.POST or None)
    if form.is_valid():
        vendor = form.save(commit=False)
        vendor.user = user
        vendor.save()

        messages.success(request, "Vendor Account Created Successfully")

        return redirect("vendor:vendor-dashboard")

    context = {
        "form": form,
    }

    # Add CSRF token
    token = csrf_token(request)
    context["csrf_token"] = token

    return render(request, "vendor/become-vendor.html", context)

def become_vendor_submit_view(request):
    user = request.user

    if not request.user.is_authenticated:
        return redirect("login")

    if Vendor.objects.filter(user=user).exists():
        return redirect("vendor:vendor-dashboard")

    form = VendorForm(request.POST or None)
    if form.is_valid():
        vendor = form.save(commit=False)
        vendor.user = user
        vendor.save()

        messages.success(request, "Vendor Account Created Successfully")

        return redirect("vendor:vendor-dashboard")

    return render(request, "vendor/become-vendor.html", {
        "form": form,
    })


def vendor_profile_view(request):
    user = request.user
    vendor = Vendor.objects.get(user=user)
    context = {
        "vendor": vendor,
    }
    return render(request, "vendor/vendor-profile.html", context)

def vendor_profile_update_view(request):
    user = request.user
    vendor = Vendor.objects.get(user=user)

    form = VendorUpdateForm(request.POST, instance=vendor)
    if form.is_valid():
        form.save()
        messages.success(request, "Vendor Account Updated Successfully")
        return redirect("vendor:vendor-profile")

    context = {
        "vendor": vendor,
        "form": form,
    }

    # Add CSRF token
    token = csrf_token(request)
    context["csrf_token"] = token

    return render(request, "vendor/vendor-profile-update.html", context)

def vendor_delete_request_view(request):
    user = request.user
    vendor = Vendor.objects.get(user=user)

    if request.method == "POST":
        vendor.is_registered = False
        vendor.save()

        messages.success(request, "Vendor Account Deletion Request Sent")

        return redirect("home")

    context = {
        "vendor": vendor,
    }
    return render(request, "vendor/vendor-delete-request.html", context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        "vendors": vendors,
    }
    return render(request, "core/vendor-list.html", context)

def vendor_detail_view(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    products = Product.objects.filter(vendor=vendor, product_status="published").order_by("-id")

    context = {
        "vendor": vendor,
        "products": products,
    }
    return render(request, "core/vendor-detail.html", context)

def create_product_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            for image in form.cleaned_data['p_image']:
                ProductImages.objects.create(product=product, image=image)
            messages.success(request, "Product Created Successfully")
            return redirect("vendor:vendor-dashboard")
    else:
        form = ProductForm()
    return render(request, 'vendor/create-product.html', {'form': form})

def update_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            for image in form.cleaned_data['p_image']:
                ProductImages.objects.create(product=product, image=image)
            messages.success(request, "Product Updated Successfully")
            return redirect("vendor:vendor-dashboard")
    else:
        form = ProductForm(instance=product)
    return render(request, 'vendor/update-product.html', {'form': form, 'product': product})

def delete_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product Deleted Successfully")
        return redirect("vendor:vendor-dashboard")
    return render(request, 'vendor/delete-product.html', {'product': product})



def vendor_orders_view(request):
        user = request.user
        vendor = Vendor.objects.get(user=user)
        orders = vendor.get_orders()
        context = {
            'orders': orders,
        }
        return render(request, 'vendor/vendor_orders.html', context)

def vendor_order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {
        'order': order,
    }
    return render(request, 'vendor/vendor_order_detail.html', context)

def vendor_order_status_update_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = OrderStatusUpdateForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status']
            order.status = status
            order.save()
            messages.success(request, "Order Status Updated Successfully")
            return redirect("vendor:vendor-orders")
    else:
        form = OrderStatusUpdateForm()
    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'vendor/vendor_order_status_update.html', context)


def vendor_order_delete_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        order.delete()
        messages.success(request, "Order Deleted Successfully")
        return redirect("vendor:vendor-orders")
    context = {
        'order': order,
    }
    return render(request, 'vendor/vendor_order_delete.html', context)


def vendor_products_view(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    products = Product.objects.filter(vendor=vendor, product_status="published").order_by("-id")

    context = {
        "vendor": vendor,
        "products": products,
    }
    return render(request, "core/vendor-products.html", context)
