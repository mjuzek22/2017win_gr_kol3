#Kol4 Testing
#github_partner: dodek08



import unittest
from kol1 import System
from kol1 import Client
from kol1 import Bank
import math


class MyTest(unittest.TestCase):

	def setUp(self):
		self.name = "Adam Kowalski"
		self.id = 2
		self.test_instance_1 = Client(self.name, self.id)
		self.test_instance_2 = Bank(self.name, self.id)
		self.test_instance_3 = System()

	def test_init_Client(self):
		self.assertEqual(self.test_instance_1.name, self.name)
		self.assertEqual(self.test_instance_1.id, self.id)

	def test_init_Bank(self):
		self.assertEqual(self.test_instance_2.name, self.name)
		self.assertEqual(self.test_instance_2.id, self.id)

	#def test_info_Client(self):
	#	self.assertEqual(self.test_instance_1.info(),( self.name, self.id,"0"))
	
		
	
