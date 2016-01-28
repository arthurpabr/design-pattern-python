# _*_ encoding: utf-8 _*_

from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

	def calcula(self, orcamento):
		# exemplo do design patter Chain of Responsability (cadeia de responsabilidades)
		desconto = Desconto_por_cinco_itens(
				Desconto_por_mais_de_quinhentos_reais(Sem_desconto())
			).calcula(orcamento)
		return desconto

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

	print orcamento.valor

	calculador = Calculador_de_descontos()
	desconto = calculador.calcula(orcamento)
	print 'Desconto calculado %s' % (desconto)