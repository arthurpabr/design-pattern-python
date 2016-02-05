# _*_ encoding: utf-8 _*_

def imprime(nota_fiscal):
	print 'Imprimindo nota fiscal %s' % (nota_fiscal.cnpj)

def envia_por_email(nota_fiscal):
	print 'Enviando por email nota fiscal %s' % (nota_fiscal.cnpj)

def salva_no_banco(nota_fiscal):
	print 'Salvando no banco nota fiscal %s' % (nota_fiscal.cnpj)