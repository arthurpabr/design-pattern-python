# _*_ encoding: utf-8 _*_

from datetime import date

class Item(object):

	def __init__(self, descricao, valor):
		self.__descricao = descricao
		self.__valor = valor

	@property
	def descricao(self):
		return self.__descricao

	@property
	def valor(self):
		return self.__valor


class Nota_fiscal(object):

	def __init__(self, razao_social, cnpj, itens, data_de_emissao, detalhes, observadores=[]):
		self.__razao_social = razao_social
		self.__cnpj = cnpj
		self.__data_de_emissao = data_de_emissao
		if len(detalhes) > 20:
			raise Exception('Os detalhes de uma nota fiscal não podem ter mais do que 20 caracteres')
		self.__detalhes = detalhes
		self.__itens = itens

		for observador in observadores:
			observador(self)
		
	@property
	def razao_social(self):
		return self.__razao_social

	@property
	def cnpj(self):
		return self.__cnpj

	@property
	def data_de_emissao(self):
		return self.__data_de_emissao

	@property
	def detalhes(self):
		return self.__detalhes

# este trecho possibilita a execução de testes com esta classe
if __name__ == '__main__': 

	from criador_de_nota_fiscal import Criador_de_nota_fiscal
	from observadores import imprime, envia_por_email, salva_no_banco

	itens=[
		Item('Item A',100),
		Item('Item B',200),
		Item('Item C',300),
		Item('Item D',400)
	]

	# Desing pattern Observer: você passa para o objeto de interesse (neste 
	# exemplo a nota fiscal) os "observadores" do mesmo, ou seja, funções 
	# que estão interessadas em sua criação e que realizam alguma ação quando
	# isso ocorre.
	# Em Python é possível PASSAR FUNÇÕES COMO PARÂMETRO, o que facilita 
	# bastante a implementação deste design pattern
	observadores=[imprime, envia_por_email, salva_no_banco, imprime]

	nota_fiscal_criada_com_builder = (Criador_de_nota_fiscal()
		.com_razao_social('Empresa Teste Ltda')
		.com_cnpj('004474171/0001-40')
		.com_itens(itens)
		.com_observadores(observadores)
		.constroi());