from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from core.models import Category
from core.choices import STATUS_CHOICE, STATUS, RATING
from vendor.models import Vendor

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# ProductVariant Model
class ProductVariant(models.Model):
    var_id = ShortUUIDField(unique=True)
    variant_title = models.CharField(max_length=255, default="Fresh Pear")
    variant_color = models.CharField(max_length=100, default="Red", null=True, blank=True)
    variant_size = models.CharField(max_length=100, default="Large", null=True, blank=True)
    variant_image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    variant_price = models.DecimalField(max_digits=15, decimal_places=2, default=1.99)
    variant_stock_count = models.IntegerField(default=10)
    variant_type = models.CharField(max_length=100, default="Organic", null=True, blank=True)

    def __str__(self):
        return self.variant_title

# Product Model
class Product(models.Model):
    pid = ShortUUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="product_categories"
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name="vendor_products")

    title = models.CharField(max_length=255, default="Fresh Pear")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    description = RichTextUploadingField(null=True, blank=True, default=None)

    price = models.DecimalField(max_digits=15, decimal_places=2, default=1.99)
    old_price = models.DecimalField(max_digits=15, decimal_places=2, default=2.99)

    specifications = RichTextUploadingField(null=True, blank=True)
    product_type = models.CharField(max_length=100, default="Organic", null=True, blank=True)
    stock_count = models.IntegerField(default=10)
    life_span = models.CharField(max_length=100, default="100 Days", null=True, blank=True)
    manufactured_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    tags = TaggableManager(blank=True)

    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")

    status = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")

    variants = models.ManyToManyField(ProductVariant, related_name="products")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price

    class Meta:
        verbose_name_plural = "Products"


# Product Images
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"


# Product Review
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="reviews")
    product_variant = models.ForeignKey(
        ProductVariant, on_delete=models.SET_NULL, null=True, related_name="variant_reviews"
    )
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, null=True, blank=True)
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
    price = models.DecimalField(max_digits=15, decimal_places=2, default=1.99)
    paid_status = models.BooleanField(default=False, null=False, blank=True)
    order_date = models.DateTimeField(auto_now_add=True, null=False, blank=True)
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
    price = models.DecimalField(max_digits=15, decimal_places=2, default=1.99)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=1.99)

    class Meta:
        verbose_name_plural = "Cart Order Items"

    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))


# Wishlists
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Wishlists"

    def __str__(self):
        return self.product.title
