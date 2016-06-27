# coding=utf-8
from django.db import models

class Element(models.Model):
	"""
		docstring for Element
		Esse model recebe um texto e um inteiro
	"""
	code = models.IntegerField(verbose_name='Código')
	text = models.TextField(verbose_name='Texto')

	def __str__(self):
		return self.text
		