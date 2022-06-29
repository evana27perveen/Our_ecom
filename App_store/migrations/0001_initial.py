# Generated by Django 3.2.7 on 2021-12-06 07:13

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Children', 'Children'), ('Special Collection', 'Special Collection')], max_length=20)),
                ('sub_category', models.CharField(max_length=50, unique=True)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_header_image', models.ImageField(upload_to='product_image')),
                ('product_image_1', models.ImageField(upload_to='product_image')),
                ('product_image_2', models.ImageField(upload_to='product_image')),
                ('product_image_3', models.ImageField(upload_to='product_image')),
                ('product_name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Children', 'Children'), ('Special Collection', 'Special Collection')], max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('available_colors', django_mysql.models.ListCharField(models.CharField(max_length=50), blank=True, max_length=510, null=True, size=10)),
                ('available_sizes', django_mysql.models.ListCharField(models.CharField(max_length=50), blank=True, max_length=408, null=True, size=8)),
                ('initial_price', models.PositiveIntegerField()),
                ('selling_price', models.PositiveIntegerField()),
                ('product_description', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now=True)),
                ('product_sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sub_category', to='App_store.subcategorymodel')),
            ],
        ),
    ]
