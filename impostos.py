# _*_ encoding: utf-8 _*_

class ISS(object):
		
	def calcula(self, orcamento):
		return orcamento.valor * 0.1


class ICMS(object):

	def calcula(self, orcamento):
		return orcamento.valor * 0.6