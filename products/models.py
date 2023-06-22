from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from core.chioces import STATUS_CHOICE, STATUS, RATING
from core.models import Category, Vendor

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
    
# Tag Model
class Tags(models.Model):
    pass

# Product Model
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10,
                         max_length=20, alphabet="abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="category")
    vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, null=True, related_name="product")

    title = models.CharField(max_length=100, default="Fresh Pear")
    image = models.ImageField(
        upload_to=user_directory_path, default="product.jpg")
    # description = models.TextField(null=True, blank=True, default="This is the product")
    description = RichTextUploadingField(
        null=True, blank=True, default="This is the product")

    price = models.DecimalField(
        max_digits=15, decimal_places=2, default="1.99")
    old_price = models.DecimalField(
        max_digits=15, decimal_places=2, default="2.99")

    specifications = RichTextUploadingField(null=True, blank=True)
    # specifications = models.TextField(null=True, blank=True)
    type = models.CharField(
        max_length=100, default="Organic", null=True, blank=True)
    stock_count = models.CharField(
        max_length=100, default="10", null=True, blank=True)
    life = models.CharField(
        max_length=100, default="100 Days", null=True, blank=True)
    mfd = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    tags = TaggableManager(blank=True)

    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    product_status = models.CharField(
        choices=STATUS, max_length=10, default="in_review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=10,
                         prefix="sku", alphabet="1234567890")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_precentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price

# Product Images
class ProductImages(models.Model):
    images = models.ImageField(
        upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(
        Product, related_name="p_images", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

# Product Review
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating

# Cart Order
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=15, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=False, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    product_status = models.CharField(
        choices=STATUS_CHOICE, max_length=30, default="processing")
    sku = ShortUUIDField(null=True, blank=True, length=5,
                         prefix="SKU", max_length=20, alphabet="abcdefgh12345")

    class Meta:
        verbose_name_plural = "Cart Order"

# Cart Order Items
class CartOrderProducts(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=15, decimal_places=2, default="1.99")
    total = models.DecimalField(
        max_digits=15, decimal_places=2, default="1.99")

    class Meta:
        verbose_name_plural = "Cart Order Items"

    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))


# wishlists  

class wishlist_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "wishlists"

    def __str__(self):
        return self.product.title
