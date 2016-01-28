# _*_ encoding: utf-8 _*_

class Orcamento(object):

	def __init__(self):
		self.__itens = [] # atributo 'privado' com '__'
	
	@property
	def valor(self): # se comporta como um 'geter'
		total = 0.0
		for item in self.__itens:
			total+= item.valor
		return total

	def obter_itens(self):
		return tuple(self.__itens)

	@property
	def total_itens(self):
		return len(self.__itens)

	def adiciona_item(self, item):
		self.__itens.append(item)


class Item(object):

	def __init__(self, nome, valor):
		self.__nome = nome
		self.__valor = valor

	@property
	def valor(self):
		return self.__valor

	def nome(self):
		return self.__nome