import random

def randID():
	id = ''
	for i in range(0,8):
		id += str(random.randint(0,9))
	return id 
def randBed(max):
	return random.randint(0,max)

class Patient(object):
	def __init__(self, ident, name, allergies):
		self.ident = ident
		self.name = name
		self.allergies = allergies
		self.bed = 0

class Hospital(object):
	def __init__(self, name, capacity):
		self.patients = []
		self.name = name
		self.capacity = capacity

	def admit(self, sick_person):
		if len(self.patients) < self.capacity:
			self.patients.append(sick_person)
			sick_person.bed = randBed(self.capacity)
			print 'You are in bed:', sick_person.bed	
			print 'Patients addmitted:', len(self.patients)
		else:
			print 'Sorry you are dead'
			return self

	def discharge(self, name):
		for dis in self.patients:
			if dis.name == name:
				self.patients.remove(dis)
				print 'You are healthy: ', dis.name
				print 'Patients addmitted:', len(self.patients)
				return self


chris = Patient(425, 'Chris', 'penecyllin')
ben = Patient(234, 'Ben', 'none')
alan = Patient(679, 'Alan', 'bees')
frank = Patient(555, 'Frank', 'pepper')


hospital1 = Hospital('Overlake', 3)
print hospital1.capacity
hospital1.admit(chris)
hospital1.admit(ben)
hospital1.admit(alan)
hospital1.admit(frank)

hospital1.discharge('Chris')



		

		