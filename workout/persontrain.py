from recursos import tabela

class Work(object):

	def __init__(self, tipo, modo):
		super(Work, self).__init__()
		self.tipo = tipo
		self.modo = modo


def traingen():
	tipo=raw_input("Qual tipo de treino?(ABC, AB ou A)")
	tipo=tipo.upper()
	modo=raw_input("Acompanhado ou solo?(A ou S)")
	modo=modo.upper()
	print tipo, modo
	tabela()
	print 'treino aqui'
	tabela()



