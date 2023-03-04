
# File: database.py
# Author(s) = Sebastian Sopola
# Description: Implement school system database and application
# -----------------------------------------------------------------------------------------------------------------------------------------------------

from student import Student



# Create the Queue class and inherit object class
class Queue(Student):

    #initialize attributes
    def __init__(self):

        # I would need to place array from student class with student information to this database queue but don't know how.
        # self.queue = Student.array not working
        self.queue = []

    # rear method to get last item of queue
    def rear(self):
        if ( len(self.queue) > 0 ):
            return ( self.queue[-1] )
        else:
            return None
        
    # front method to get item front of the queue
    def front(self):
        if ( len(self.queue) > 0 ):
            return ( self.queue[0] )
        else:
            return None

    # enqueue method to add new item back of the queue
    def enqueue(self, item = ''):
        self.queue.append(item)

    # dequeue method to delete item front of the queue
    def dequeue(self):
        if ( len(self.queue) < 1 ):
            return None
        else:
            self.queue.pop(0)

    # empty method to check whether queue is empty
    def empty(self):
        if ( len(self.queue) < 1 ):
            return True
        else:
            return False


        

    
