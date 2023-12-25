# Python program to illustrate destructor
class Employee:
	def __init__(self):
		print('Employee created.')
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj