from recursos import tabela

class Work(object):

	def __init__(self, tipo, modo):
		super(Work, self).__init__()
		self.tipo = tipo
		self.modo = modo

	def trainer(self,tipo):
		peito=['supino','crucifixo','remada','pullover']
		triceps=['francesa','pulldown','testa']
		biceps=['scott', 'concentrada']
		costas=['puxada']
		ombro=[]
		perna=[]
		abdomen=[]


def traingen():
	tipo=raw_input("Qual tipo de treino?(ABC, AB ou A)")
	modo=raw_input("Acompanhado ou solo?(A ou S)")
	tabela()
	print 'treino aqui'
	tabela()

traingen()



