class Category:
	name = None
	description = None
	count = None
	parent = None

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.count = 0
		self.parent = 0

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setDescription(self, description):
		self.description = description

	def getDescription(self):
		return self.description

	def setCount(self, count):
		self.count = count

	def getCount(self):
		return self.count

	def setParent(self, parent):
		self.parent = parent

	def getParent(self):
		return self.parent