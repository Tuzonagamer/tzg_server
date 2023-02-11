import json
import pathlib

class ResponseContainer:
	"""
	route Response
	:autor: Jajoya
	:date: 2022-11-23
	"""
	def __init__(self, className):
		self.name = className
		self.status = None
		self.message = None
		self.is_ok = None
		self.object = None
		self.object_ = None
		self.data_list = []
		
		with open("{0}/object.json".format(pathlib.Path(__file__).parent.resolve()), 'r') as j:
			self.structure = json.loads(j.read())
		self.restarObject()
		"""
		"""

	def clearObject(self):
		self.object = None

	def restarObject(self):
		self.object = self.structure

	def alertCallContext(self,enpoint):
		print("""
			class: {}\n
			enpoint: {}\n
		""".format(self.name, enpoint))

	def getObject(self):
		self.object["name_autor"] = self.name		
		self.object["message"] = self.message		
		self.object["is_ok"] = self.is_ok		
		self.object["status"] = self.status		
		self.object["data_object"] = self.object_		
		self.object["data_list"] = self.data_list		
		return self.object