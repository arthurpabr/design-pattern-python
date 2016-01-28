# _*_ encoding: utf-8 _*_

class Orcamento(object):

	def __init__(self, valor):
		self.__valor = valor # atributo 'privado' com '__'
	
	@property
	def valor(self): # se comporta como um 'geter'
		return self.__valor
