from django import forms
from stripe import Review 
from products.models import Product, ProductReview,  ProductVariant


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'price',
            'old_price',
            'specifications',
            'product_type',
            'stock_count',
            'life_span',
            'manufactured_date',
            'tags',
            'product_status',
            'status',
            'featured',
            'digital',
            'sku',
            'variants',
            
        ]
        widgets = {
            'tags': forms.TextInput(attrs={'class': 'tags-input'}),
        }
        
class ProductVariantForm(forms.ModelForm):
    model = ProductVariant
    fields = [
        'var_id',
        'variant_title',
        'variant_price', 
        'variant_stock_count',
        'variant_type',
    ]

class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Write review"}), required=True)

    class Meta:
        model = ProductReview
        fields = ['review', 'rating']


class ProductVariantReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['review', 'rating']
