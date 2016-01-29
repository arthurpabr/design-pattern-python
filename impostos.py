# _*_ encoding: utf-8 _*_

from abc import ABCMeta, abstractmethod # módulo abstract class

class Template_de_imposto_condicional(object):

	__metaclass__ = ABCMeta # indicando que a classe será abstrata

	def calcula(self, orcamento):
		if self.deve_usar_maxima_taxacao(orcamento):
			return self.maxima_taxacao(orcamento)
		else:
			return self.minima_taxacao(orcamento)

	# o uso da classe abstrata e seus métodos são exemplos do design pattern
	# Template method - uma mesma estrutura é aplicável a diferentes situações
	# (a regra é definida na classe abstrata e as situações são implementadas
	# em cada classe filha)

	@abstractmethod # indicando que a implementação deste método na classe filha é obrigatória
	def deve_usar_maxima_taxacao(orcamento):
		pass

	@abstractmethod # indicando que a implementação deste método na classe filha é obrigatória
	def maxima_taxacao(orcamento):
		pass

	@abstractmethod # indicando que a implementação deste método na classe filha é obrigatória
	def minima_taxacao(orcamento):
		pass


class ISS(object):
		
	def calcula(self, orcamento):
		return orcamento.valor * 0.1


class ICMS(object):

	def calcula(self, orcamento):
		return orcamento.valor * 0.6


class ICPP(Template_de_imposto_condicional):

	def deve_usar_maxima_taxacao(self, orcamento):
		if orcamento.valor > 500:
			return True
		return False

	def maxima_taxacao(self, orcamento):
		return orcamento.valor * 0.07

	def minima_taxacao(self, orcamento):
		return orcamento.valor * 0.05


class IKCV(Template_de_imposto_condicional):

	def deve_usar_maxima_taxacao(self, orcamento):
		if orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento):
			return True
		return False

	def maxima_taxacao(self, orcamento):
		return orcamento.valor * 0.1

	def minima_taxacao(self, orcamento):
		return orcamento.valor * 0.06

	def __tem_item_maior_que_100_reais(self, orcamento):
		for item in orcamento.obter_itens():
			if item.valor > 100:
				return True
		return False