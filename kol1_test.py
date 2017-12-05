#Kol4 Testing
#github_partner: dodek08



import unittest
from kol1 import System
from kol1 import Client
from kol1 import Bank
import math


class MyTest(unittest.TestCase):

	def setUp(self):
		self.c_name1 = "Adam Kowalski"
		self.c_name2 = "Anna Nowak"
		self.b_name1 = "MBank"
		self.b_name2 = "PKO"
		self.id1 = 1
		self.id2 = 2
		self.test_client_1 = Client(self.c_name1, self.id1)
		self.test_client_2 = Client(self.c_name2, self.id2)
		self.test_bank_1 = Bank(self.b_name1, self.id1)
		self.test_bank_2 = Bank(self.b_name2, self.id1)
		self.test_system = System()

	def test_init_Client(self):
		self.assertEqual(self.test_client_1.name, self.c_name1)
		self.assertEqual(self.test_client_2.id, self.id2)

	def test_init_Bank(self):
		self.assertEqual(self.test_bank_2.name, self.b_name2)
		self.assertEqual(self.test_bank_1.id, self.id1)

	def test_init_System(self):
		self.assertEqual(self.test_system.number_of_banks,0)


	def test_info_Client(self):
		self.assertEqual(self.test_client_1.info(),(self.c_name1,self.id1,0))
	
	def test_add_client_Bank(self):
		self.test_bank_1.add_client(self.test_client_1, 1000)
		self.assertEqual(self.test_bank_1.clients_ids[0], self.test_client_1.id)

	def test_put_money_Bank(self):
		self.test_bank_1.add_client(self.test_client_1, 1000)
		self.test_bank_1.put_money(self.id1, 1000)
		self.assertEqual(self.test_bank_1.clients_money[self.test_client_1.id], 2000)
   
	def test_withdraw_money_Bank(self):
		self.test_bank_1.add_client(self.test_client_1, 1000)
		self.test_bank_1.withdraw_money(self.id1, 100)
		self.assertEqual(self.test_bank_1.clients_money[self.id1], 900)
		
 	def test_new_bank_System(self):
		self.test_system.new_bank(self.b_name2)
		self.assertEqual(self.test_system.banks[0].name, self.b_name2)

	def test_new_bank_client_System(self):
		self.test_system.new_bank(self.b_name2)
		self.test_system.new_bank_client("Ania",0)
		self.assertEqual(self.test_system.banks[0].number_of_accounts_in_bank , 1)
   
	def test_put_money_System(self):
		self.test_system.new_bank(self.b_name2)
		self.test_system.new_bank_client("Ania", 0)
		self.test_system.put_money(0,100)
		self.assertEqual(self.test_system.banks[0].clients_money[0], 100)
   
	def test_withdraw_money_System(self):
		self.test_system.new_bank(self.b_name2)
		self.test_system.new_bank_client("Ania", 0)
		self.test_system.withdraw_money(0,100)
		self.assertEqual(self.test_system.banks[0].clients_money[0],-100)
   
	def test_transfer_from_client_to_client_System(self):
		self.test_system.new_bank(self.b_name2)
		self.test_system.new_bank_client("Ania", 0)
		self.test_system.new_bank_client("Tomek", 0)
		self.test_system.put_money(0,100)
		self.test_system.transfer_from_client_to_client(0,1,100)
		self.assertEqual(self.test_system.banks[0].clients_money[0],0)
		self.assertEqual(self.test_system.banks[0].clients_money[1],100)