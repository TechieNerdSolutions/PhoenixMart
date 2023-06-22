# Generated by Django 4.2.1 on 2023-06-22 01:14

import ckeditor_uploader.fields
import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefgh12345",
                        length=10,
                        max_length=20,
                        prefix="cat",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(default="Food", max_length=100)),
                (
                    "image",
                    models.ImageField(default="category.jpg", upload_to="category"),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Tags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "vid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefgh12345",
                        length=10,
                        max_length=20,
                        prefix="ven",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(default="phoenixify", max_length=100)),
                (
                    "image",
                    models.ImageField(
                        default="vendor.jpg", upload_to=core.models.user_directory_path
                    ),
                ),
                (
                    "cover_image",
                    models.ImageField(
                        default="vendor.jpg", upload_to=core.models.user_directory_path
                    ),
                ),
                (
                    "description",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, default="I am am Amazing Vendor", null=True
                    ),
                ),
                (
                    "address",
                    models.CharField(default="123 Main Street.", max_length=100),
                ),
                ("contact", models.CharField(default="+123 (456) 789", max_length=100)),
                ("chat_resp_time", models.CharField(default="100", max_length=100)),
                ("shipping_on_time", models.CharField(default="100", max_length=100)),
                ("authentic_rating", models.CharField(default="100", max_length=100)),
                ("days_return", models.CharField(default="100", max_length=100)),
                ("warranty_period", models.CharField(default="100", max_length=100)),
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Vendors",
            },
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mobile", models.CharField(max_length=300, null=True)),
                ("address", models.CharField(max_length=100, null=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Address",
            },
        ),
    ]
