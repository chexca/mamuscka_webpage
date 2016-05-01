from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
	name = models.TextField()
	brief = models.TextField()

	def __unicode__(self):
		return self._meta.object_name

	class Meta:
		verbose_name_plural = "categories"


class SubCategory(Category):
	description = models.TextField()

	def __unicode__(self):
		return self._meta.object_name

	class Meta:
		verbose_name_plural = "subcategories"


class Brand(models.Model):
	name = models.TextField()
	image = models.ImageField()

	def __unicode__(self):
		return self._meta.object_name


class Product(models.Model):
	prize = models.DecimalField(decimal_places=2, max_digits=10)
	discount = models.DecimalField(decimal_places=2, max_digits=10)
	color = models.TextField()
	stock_units = models.DecimalField(decimal_places=0, max_digits=5)
	image = models.ImageField()

	related_category = models.ForeignKey(Category)
	related_subcategory = models.ForeignKey(SubCategory, related_name='%(class)s_subcategory')
	brand = models.ForeignKey(Brand)

	is_outlet = models.BooleanField()
	description = models.TextField()
	brand_reference = models.TextField()

	def __unicode__(self):
		return self._meta.object_name


class Pack(models.Model):
	pack_price = models.DecimalField(decimal_places=2, max_digits=10)

	def __unicode__(self):
		return self._meta.object_name


class ProductPack(models.Model):
	product = models.ForeignKey(Product)
	pack = models.ForeignKey(Pack)

	def __unicode__(self):
		return self._meta.object_name


class BornGiftsList(models.Model):
	access_code = models.TextField()
	description = models.TextField()
	fathers_name = models.TextField()
	fathers_image = models.ImageField()

	def __unicode__(self):
		return self._meta.object_name


class BornGiftsListProducts(models.Model):
	product = models.ForeignKey(Product)
	born_gift_list = models.ForeignKey(BornGiftsList)

	def __unicode__(self):
		return self._meta.object_name

	class Meta:
		verbose_name_plural = "born gifts list products"


class GiftCard(models.Model):
	code = models.TextField()
	amount = models.DecimalField(decimal_places=2, max_digits=10)

	def __unicode__(self):
		return self._meta.object_name
