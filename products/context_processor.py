from ast import Add
from products.models import Product, CartOrder, ProductImages, ProductReview, Wishlist
from core.models import Category, Address
from django.db.models import Min, Max
from django.contrib import messages
from vendor.models import Vendor

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()

    min_max_price = Product.objects.aggregate(Min("price"), Max("price"))

    if request.user.is_authenticated:
        try:
            user_wishlist = Wishlist.objects.filter(user=request.user)
            # You can also check if the wishlist is empty and set it to 0 accordingly
            wishlist = user_wishlist.count() if user_wishlist.exists() else 0
        except:
            messages.warning(request, "You need to login before accessing your wishlist.")
            wishlist = 0
    else:
        wishlist = 0

    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None

    return {
        'categories':categories,
        'wishlist':wishlist,
        'address':address,
        'vendors':vendors,
        'min_max_price':min_max_price,
    }