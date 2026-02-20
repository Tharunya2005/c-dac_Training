#by default every class inherits from a base clas called objects
class Book(object):
    def __init__(self):
        print('Book Initializer Method Called')

if __name__ == '__main__':
    b1 = Book() #Object Creation -> using classname with() instructs python to instanstiate the class
    print("Attributes of b1 are: ",dir(b1))