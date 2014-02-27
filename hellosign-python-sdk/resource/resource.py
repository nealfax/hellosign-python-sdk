import json
from abc import ABCMeta, abstractmethod

class Resource(object):

	__metaclass__ = ABCMeta
	json_data = None

	"""docstring for Resource"""
	# def __init__(self, arg):
	# 	super(Resource, self).__init__()
	# 	self.arg = arg

	def __init__(self, jsonstr = None):
		super(Resource, self).__init__()
		if jsonstr is not None:
			print jsonstr
			self.json_data = json.loads(json.dumps(jsonstr))

	# @abstractmethod
	# def say_something(self):
	# 	raise NotImplementedError()
