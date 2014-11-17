class Animal:
	def__init__(self,name,age):
		self.name=name
		self.age=age

	def sleep(self):
		print self.name + " age " + self.age + " is sleeping"

	def eat(self):
		print self.name + " age " + self.age + " is eating"

class Bird(Animal):
	def__init__(self, name, age, color_wing):
		Animal.__init__(self, name, age)
		self.color_wing=color_wing
	
	def fly(self):
		print self.name + "is flying"


class Dog(Animal):
	def__init__(self, name, age, num_of_legs):
		Animal.__init__(self,name,age)
		self.num_of_legs=num_of_legs

	def bark(self)
		print self.name + " has " + self.num_of_legs+" legs and he is barking"
		
