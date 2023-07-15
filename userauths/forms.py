from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'email']



class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Full Name"}))
    bio = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Bio"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Phone"}))

    class Meta:
        model = Profile
        fields = ['full_name', 'image', 'bio', 'phone']



from django import forms
from .models import User, Profile, ContactUs


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email"}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password1 = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already in use.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("The passwords must match.")
        return password2


class UserChangeForm(forms.ModelForm):
    password = forms.CharField(max_length=128, required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'date_of_birth')


class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={"placeholder": "Full Name"}))
    bio = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={"placeholder": "Biography"}))
    phone = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={"placeholder": "Phone"}))
    social_media_handles = forms.CharField(max_length=200, required=False,widget=forms.TextInput(attrs={"placeholder": "Social Media Handles"}))

    class Meta:
        model = Profile
        fields = ('full_name', 'bio', 'phone', 'social_media_handles')


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('full_name', 'email', 'phone', 'subject', 'message')

