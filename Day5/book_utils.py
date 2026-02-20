class book:
    def __init__(self,**kwargs):
        self.title = kwargs.get('title')
        self.author = kwargs.get('author')
        self.price = kwargs.get('price')

    def __str__(self):
        return f'title={self.title!r}, author = {self.author!r}, price = {self.price!r}'
    
    def print(self):
        print(f'Title : {self.title}')
        print(f'Author : {self.author}')
        print(f'Price : {self.price}',end = '\n')
        print('_'*30)
    

if __name__ == '__main__':
    b1 = book(title = 'Let C', author = 'Y kanitar', price = 499)
    b2 = book(title = 'Let Python', author = 'Vinod', price = 999)
    b3 = book()

    print(b1) # the print methos looks fr and invokes __str__ magic method
    print(b2)
    print(b3)
    b1.print() # Book.print(b1)
    b2.print()
    b3.print()

