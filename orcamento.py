# _*_ encoding: utf-8 _*_

from abc import ABCMeta, abstractmethod

class Estado_de_um_orcamento(object):

	__metaclass__ = ABCMeta

	@abstractmethod
	def aplica_desconto_extra(self, orcamento):
		pass

	@abstractmethod
	def aprova(self, orcamento):
		pass

	@abstractmethod
	def reprova(self, orcamento):
		pass

	@abstractmethod
	def finaliza(self, orcamento):
		pass

class Em_aprovacao(Estado_de_um_orcamento):

	def __init__(self):
		self.__ja_aplicado = False

	def aplica_desconto_extra(self, orcamento):
		if(self.__ja_aplicado == False):
			self.__ja_aplicado = True
			orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
		else:
			raise Exception('Desconto já aplicado!')

	def aprova(self, orcamento):
		orcamento.estado_atual = Aprovado()

	def reprova(self, orcamento):
		orcamento.estado_atual = Reprovado()

	def finaliza(self, orcamento):
		raise Exception('Orçamentos em aprovação não podem ser finalizados')


class Aprovado(Estado_de_um_orcamento):
	
	def __init__(self):
		self.__ja_aplicado = False

	def aplica_desconto_extra(self, orcamento):
		if(self.__ja_aplicado == False):
			self.__ja_aplicado = True
			orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
		else:
			raise Exception('Desconto já aplicado!')

	def aprova(self, orcamento):
		raise Exception('Orçamento já está aprovado!')

	def reprova(self, orcamento):
		raise Exception('Orçamentos aprovados não podem ser reprovados')

	def finaliza(self, orcamento):
		orcamento.estado_atual = Finalizado()

	
class Reprovado(Estado_de_um_orcamento):
	def aplica_desconto_extra(self, orcamento):
		raise Exception('Orçamentos reprovados não recebem desconto extra')

	def aprova(self, orcamento):
		raise Exception('Orçamentos reprovados não podem ser aprovados')

	def reprova(self, orcamento):
		raise Exception('Orçamento já está reprovado!')

	def finaliza(self, orcamento):
		orcamento.estado_atual = Finalizado()


class Finalizado(Estado_de_um_orcamento):
	def aplica_desconto_extra(self, orcamento):
		raise Exception('Orçamentos finalizados não recebem desconto extra')
	
	def aprova(self, orcamento):
		raise Exception('Orçamentos finalizados não podem ser aprovados')

	def reprova(self, orcamento):
		raise Exception('Orçamentos finalizados não podem ser reprovados')

	def finaliza(self, orcamento):
		raise Exception('Orçamento já está finalizado!')


class Orcamento(object):

	def __init__(self):
		self.__itens = [] # atributo 'privado' com '__'
		self.estado_atual = Em_aprovacao()
		self.__desconto_extra = 0

	def aprova(self):
		self.estado_atual.aprova(orcamento)

	def reprova(self):
		self.estado_atual.reprova(orcamento)

	def finaliza(self):
		self.estado_atual.finaliza(orcamento)

	def adiciona_desconto_extra(self, desconto):
		self.__desconto_extra+=desconto

	def aplica_desconto_extra(self):
		self.estado_atual.aplica_desconto_extra(self)
	
	@property
	def valor(self): # se comporta como um 'geter'
		total = 0.0
		for item in self.__itens:
			total+= item.valor
		return total - self.__desconto_extra

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

# este trecho possibilita a execução de testes com esta classe
if __name__ == '__main__': 

	orcamento = Orcamento()
	orcamento.adiciona_item(Item('ITEM 01', 100))
	orcamento.adiciona_item(Item('ITEM 02', 50))
	orcamento.adiciona_item(Item('ITEM 03', 400))

	print orcamento.valor
	orcamento.aplica_desconto_extra()
	print orcamento.valor
	orcamento.aprova()
	orcamento.aplica_desconto_extra()
	print orcamento.valor
	orcamento.aplica_desconto_extra()
	print orcamento.valor