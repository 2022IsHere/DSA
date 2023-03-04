
# File: Student.py
# Author(s) = Sebastian Sopola
# Description: Collect and manage student application information etc
# -------------------------------------------------------------------------------------------------------------------------------------------------------------


class Student(object):

    # initialize attributes
    def __init__(self, name, age, city, region, hobby, ka, enGrade, maGrade, fiGrade):
        

        self.array = []
        self.name = str
        self.age = int
        self.city = str
        self.region = str
        self.hobby = str
        self.ka = float
        self.enGrade = int
        self.maGrade = int
        self.fiGrade = int

    # push method to place student attribute values into array
    def push(self, name = '', age = '', city = '', region = '', hobby = '', ka = int, enGrade = int, maGrade = int, fiGrade = int):
        if ( len(self.array ) > 0 ):
            return None
        else:
            self.array.append(name)
            self.array.append(age)
            self.array.append(city)
            self.array.append(region)
            self.array.append(hobby)
            self.array.append(ka)
            self.array.append(enGrade)
            self.array.append(maGrade)
            self.array.append(fiGrade)

    # giveName method to show student name
    def giveName(self):
        return self.array[0]

    # getMath method to get student grade
    def getEnglsh(self):
        return "English grade is: ", self.array[6]

    # getMath method to get student grade
    def getMAth(self):
        return "Math grade is: ", self.array[7]

    # getMath method to get student grade
    def getFinnish(self):
        return "Finnish grade is: ", self.array[8]

    # getAge method to get student age
    def getAge(self):
        return "Student age is: ", self.array[1]

    # getHobby method to get student hobby information
    def getHobby(self):
        return "Student's hobby is: ", self.array[4]
    
    # return all student information as array
    def returnInfo(self):
        return self.array
    


    

    
    
    
    





    
        
    


