#!#!usr/bin/env python2.7




		

class Client:


	def __init__(self, name, id):
		self.name = name
		self.id = id
		self.accounts = 0

	def info(self):
		return self.name, self.id, self.accounts

class Bank():


	def __init__(self, name, id):
		self.name = name
		self.id = id
		self.clients_ids = []
		self.clients_money = {} #client_id : amount
		self.number_of_accounts_in_bank = 0

	def add_client(self, client, input = 0):
		self.clients_money[client.id] = input
		client.accounts = input
		self.clients_ids.append(client.id)
		self.number_of_accounts_in_bank +=1

	def put_money(self, client_id, amount):
		self.clients_money[client_id] += amount

	def withdraw_money(self, client_id, amount):
		self.clients_money[client_id] -= amount


class System():


	def __init__(self):
		self.banks = []
		self.clients = []
		self.number_of_banks = 0
		self.number_of_clients = 0


	def new_bank(self, name):
		self.banks.append(Bank(name,self.number_of_banks))
		self.number_of_banks += 1

	def new_bank_client(self, clients_name, bank_id):
		self.clients.append(Client(clients_name,self.number_of_clients))
		self.banks[bank_id].add_client(Client(clients_name,self.number_of_clients))
		self.number_of_clients += 1

	def put_money(self, client_id, amount):
		bank_id = -1
		for B in self.banks:
			if B.clients_ids.count(client_id) > 0:
				bank_id=B.id
		if bank_id == -1:
			raise ValueError("Client is not in any bank")
		self.banks[bank_id].put_money(client_id, amount)
		self.clients[client_id].accounts += amount

	def withdraw_money(self, client_id, amount):
		bank_id = -1
		for B in self.banks:
			if B.clients_ids.count(client_id) > 0:
				bank_id=B.id
		if bank_id == -1:
			raise ValueError("Client is not in any bank")
		self.banks[bank_id].withdraw_money(client_id, amount)
		self.clients[client_id].accounts -= amount

	def transfer_from_client_to_client(self, client_id_1, client_id_2, amount):
		self.withdraw_money(client_id_1, amount)
		self.put_money(client_id_2, amount)




if __name__ == "__main__":

	SYS = System()
	SYS.new_bank("FISBANK")
	SYS.new_bank("CERNBANK")
	SYS.new_bank_client("Adam", "FISBANK", 0)
	SYS.new_bank_client("Barbara", "CERNBANK", 1)
	SYS.put_money(0,2000)
	SYS.withdraw_money(0,100)
	SYS.transfer_from_client_to_client(0,1,1000)
	print(SYS.clients[0].info())
	print(SYS.clients[1].info())