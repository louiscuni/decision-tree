class node :

	def __init__ (self, profondeur, leftson, rightson, nature, value ):
		self.profondeur = profondeur #profondeur du node sur l'arbre globale
		self.leftson = leftson #fils gauche
		self.rightson = rightson #fils droit
		self.nature = nature #nature feuille ou node ?
		self.value = value


