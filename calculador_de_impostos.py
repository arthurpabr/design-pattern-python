# _*_ encoding: utf-8 _*_

from impostos import ISS, ICMS, ICPP, IKCV

class Calculador_de_impostos(object):

	def realiza_calculo(self, orcamento, imposto): 
		# o 'imposto' é a estratégia de cálculo; 
		# pode ser uma função, método ou instância de classe em Python que está sendo passada como parâmetro
		# design pattern "strategy"
		imposto_calculado = imposto.calcula(orcamento)
		print imposto_calculado


# este trecho possibilita a execução de testes com esta classe
if __name__ == '__main__': 

	from orcamento import Orcamento, Item

	orcamento = Orcamento()
	orcamento.adiciona_item(Item('ITEM 01', 100))
	orcamento.adiciona_item(Item('ITEM 02', 50))
	orcamento.adiciona_item(Item('ITEM 03', 400))
	orcamento.adiciona_item(Item('ITEM 04', 400))
	orcamento.adiciona_item(Item('ITEM 05', 500))
	orcamento.adiciona_item(Item('ITEM 06', 40))

	calculador = Calculador_de_impostos()
	
	print 'ICMS e ISS'
	calculador.realiza_calculo(orcamento, ICMS())
	calculador.realiza_calculo(orcamento, ISS())

	print 'ICPP e IKCV'
	calculador.realiza_calculo(orcamento, ICPP())
	calculador.realiza_calculo(orcamento, IKCV())