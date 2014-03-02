import json
from abc import ABCMeta, abstractmethod

class Resource(object):

	__metaclass__ = ABCMeta
	json_data = None

	"""docstring for Resource"""
	# def __init__(self, arg):
	# 	super(Resource, self).__init__()
	# 	self.arg = arg

	def __init__(self, jsonstr = None, key = None):
		super(Resource, self).__init__()
		if jsonstr is not None:
			if key is not None:
				object.__setattr__(self, 'json_data', json.loads(json.dumps(jsonstr))[key])
			else:
				object.__setattr__(self, 'json_data', json.loads(json.dumps(jsonstr)))				

	def __getattr__(self, name):
		if name in self.json_data:
			return self.json_data[name]
		else:
			raise AttributeError

	def __setattr__(self, name, value):
		if name in self.json_data:
			self.json_data[name] = value
		else:
			raise AttributeError

	# @abstractmethod
	# def say_something(self):
	# 	raise NotImplementedError()
