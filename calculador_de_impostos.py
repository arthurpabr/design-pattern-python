# _*_ encoding: utf-8 _*_

from impostos import ISS, ICMS

class Calculador_de_impostos(object):

	def realiza_calculo(self, orcamento, imposto): 
		# o 'imposto' é a estratégia de cálculo; 
		# pode ser uma função, método ou instância de classe em Python que está sendo passada como parâmetro
		# design pattern "strategy"
		imposto_calculado = imposto.calcula(orcamento)
		print imposto_calculado


# este trecho possibilita a execução de testes com esta classe
if __name__ == '__main__': 

	from orcamento import Orcamento

	calculador = Calculador_de_impostos()
	orcamento = Orcamento(500)
	calculador.realiza_calculo(orcamento, ICMS())
	calculador.realiza_calculo(orcamento, ISS())