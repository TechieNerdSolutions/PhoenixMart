from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from vendor.models import Vendor


class VendorForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True,widget=forms.TextInput(attrs={"placeholder": "Email"}) )

    class Meta:
        model = Vendor
        fields = [
            "title",
            "image",
            "cover_image",
            "description",
            "address",
            "contact_emergency",
            "chat_resp_time",
            "shipping_on_time",
            "authentic_rating",
            "days_return",
            "warranty_period",
            "website_url",
            "social_media_handles",
        ]

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_description(self):
        description = self.cleaned_data["description"]
        if len(description) < 100:
            raise forms.ValidationError("Description must be at least 100 characters long.")
        return description

    def clean_address(self):
        address = self.cleaned_data["address"]
        if len(address) < 10:
            raise forms.ValidationError("Address must be at least 10 characters long.")
        return address

class VendorUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={"placeholder": "Email"}))

    class Meta:
        model = Vendor
        fields = [
            "title",
            "profile_photo",
            "cover_image",
            "description",
            "address",
            "contact_emergency",
            "chat_resp_time",
            "shipping_on_time",
            "authentic_rating",
            "days_return",
            "warranty_period",
            "website_url",
            "social_media_handles",
        ]

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_description(self):
        description = self.cleaned_data["description"]
        if len(description) < 100:
            raise forms.ValidationError("Description must be at least 100 characters long.")
        return description

    def clean_address(self):
        address = self.cleaned_data["address"]
        if len(address) < 10:
            raise forms.ValidationError("Address must be at least 10 characters long.")
        return address


class OrderStatusUpdateForm(forms.Form):
    status = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Status"}))

    class Meta:
        model = Vendor
        fields = [
            "status",
        ]