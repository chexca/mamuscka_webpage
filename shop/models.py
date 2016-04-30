from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	pass

class Category(models.Model):
	pass

class SubCategory(Category):
	pass

class Pack(models.Model):
	pass

class Brand(models.Model):
	pass

class BornGiftsList(models.Model):
	pass

class GiftCard(models.Model):
	pass 
