from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from shortuuid.django_fields import ShortUUIDField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.conf import settings
from core.models import Address

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20,
                         prefix="ven", alphabet="abcdefgh12345")

    title = models.CharField(max_length=100, default="phoenixify")
    profile_photo = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to=user_directory_path, default="blank")
    description = RichTextUploadingField(
        null=True, blank=True, default="I am an Amazing Vendor")

    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, related_name="vendor_address"
    )
    contact_emergency = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, related_name="contact_emergency_address"
    )
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vendor')
    is_registered = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    website_url = models.CharField(max_length=200, blank=True, null=True)
    social_media_handles = models.CharField(max_length=200, blank=True, null=True)

    logo = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)

    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.profile_photo.url))

    def __str__(self):
        return self.title

    @classmethod
    def create_vendor(cls, user, **kwargs):
        from products.models import Product  # Import inside the method/function
        vendor = cls(user=user, **kwargs)
        vendor.is_registered = True
        vendor.save()
        return vendor

    def get_products(self):
        from products.models import Product  # Import inside the method/function
        return Product.objects.filter(vendor=self)

    def add_product(self, title, image, description, price, old_price, specifications, product_type, stock_count, life_span, manufactured_date, tags, product_status, status, in_stock, featured, digital, sku):
        from products.models import Product  # Import inside the method/function
        product = Product.objects.create(
            vendor=self,
            title=title,
            image=image,
            description=description,
            price=price,
            old_price=old_price,
            specifications=specifications,
            product_type=product_type,
            stock_count=stock_count,
            life_span=life_span,
            manufactured_date=manufactured_date,
            tags=tags,
            product_status=product_status,
            status=status,
            in_stock=in_stock,
            featured=featured,
            digital=digital,
            sku=sku,
            variant_title=variant_title,
            variant_color=variant_color,
            variant_size=variant_size,
            variant_image=variant_image,
            variant_price=variant_price,
            variant_stock_count=variant_stock_count,
            variant_type=variant_type,
        )
        return product

    slug = models.SlugField(max_length=255, unique=True)
