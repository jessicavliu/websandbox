class Category:

	#term_id = None #seems like it should be a field. But I don't set it- the db does. So should I keep it?
	name = ""
	description = ""
	count = 0
	parent = None

	def __init__(self, name, description, parent):
		self.name = name
		self.description = description
		self.count = 0
		self.parent = parent #type Category


	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def set_description(self, description):
		self.description = description

	def get_description(self):
		return self.description

	def set_count(self, count):
		self.count = count

	def get_count(self):
		return self.count

	def set_parent_category(self, parent):
		self.parent = parent

	def get_parent_category(self):
		return self.parent

	def has_parent_category(self):
		return True if self.parent != None else False