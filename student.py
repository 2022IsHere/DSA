
# File: Student.py
# Author(s) = Sebastian Sopola
# Description: Collect and manage student application information etc
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# import database functionality
from database import Queue


class Student(Queue):

    # initialize attributes
    def __init__(self, name : str, age : int, city : str, region : str, hobby: str, ka : float, enGrade : int, maGrade : int, fiGrade : int):
        
        # student info attributes
        self.array = []
        self.name = name
        self.age = age
        self.city = city
        self.region = region
        self.hobby = hobby
        self.ka = float(ka)
        self.enGrade = enGrade
        self.maGrade = maGrade
        self.fiGrade = fiGrade

        # queue database to store student information
        self.queue = []

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
    def getEnglish(self):
        return "English grade is: ", self.array[6]

    # getMath method to get student grade
    def getMath(self):
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









    
