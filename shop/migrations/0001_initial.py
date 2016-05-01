# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-01 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BornGiftsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_code', models.TextField()),
                ('description', models.TextField()),
                ('fathers_name', models.TextField()),
                ('fathers_image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='BornGiftsListProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('born_gift_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.BornGiftsList')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('brief', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.TextField()),
                ('stock_units', models.DecimalField(decimal_places=0, max_digits=5)),
                ('image', models.ImageField(upload_to=b'')),
                ('is_outlet', models.BooleanField()),
                ('description', models.TextField()),
                ('brand_reference', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Pack')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Category')),
                ('description', models.TextField()),
            ],
            bases=('shop.category',),
        ),
        migrations.AddField(
            model_name='product',
            name='related_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category'),
        ),
        migrations.AddField(
            model_name='borngiftslistproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='related_subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_subcategory', to='shop.SubCategory'),
        ),
    ]
