import pickle 
class Student :
	def __init__(self, name, age): 	
		self.name = name
		self.age = age

Student1 = Student("Sita",23)
Student2 = Student("Gita",24)

print (str.format("The details of student 1 are:\nName:{0}\tAge:{1}",Student1.name, Student1.age))

print (str.format("\nThe details of student 2 are:\nName:{0}\tAge:{1}",Student2.name, Student2.age))


Student1_file= open ('Student1.txt',mode='wb')
Student1_pickled = pickle.dump(Student1, Student1_file)
Student1_file.close()

Student2_file= open ('Student2.txt',mode='wb')
Student2_pickled = pickle.dump(Student2, Student2_file)
Student2_file.close()



Student1_file= open ('Student1.txt',mode='rb')
Student1_unpickled = pickle.load(Student1_file)
Student1_file.close()

Student2_file= open ('Student2.txt',mode='rb')
Student2_unpickled = pickle.load(Student2_file)
Student2_file.close()


print (str.format("\nThe details of student 1 after pickling are:\nName:{0}\tAge:{1}",Student1_unpickled.name, Student1_unpickled.age))


print (str.format("\nThe details of student 2 after pickling are:\nName:{0}\tAge:{1}",Student2_unpickled.name, Student2_unpickled.age))
	
