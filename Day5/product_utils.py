class ProductError(Exception): ...
class ProductPriceError(ProductError): ...
class ProductNameError(ProductError): ...


class Product:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    # for every private variable (__prefixed) we can provide a pair of getter/setter
    # for __name the getter would like this:
    @property
    def name(self):
        return self.__name
    # for __name the setter would like this:
    @name.setter
    def name(self, value):
        if value is not None:
            if type(value) != str:
                raise ProductNameError('product name must be a string')
            value = value.strip()
            if len(value) == 0 or len(value) > 50:
                raise ProductNameError('length of product name must be between 1 and 50')

        self.__name = value


    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value is not None:
            if type(value) not in (int, float):
                raise ProductPriceError('product price must be numeric')
            
            if value <= 0 or value > 999999:
                raise ProductPriceError('product price must be between 1 and 999999')
            
        self.__price = value

    def print(self):
        print('Product details: ')
        print(f'Name    = {self.__name}')
        print(f'Price   = {self.__price}')
        print('-'*30)

    
if __name__ == '__main__':
    p1 = Product("Samsung TV 32 Inch", 27500000000)
    p1.print()

    p2 = Product()
    p2.name = 'Sony TV 32 Inch'
    p2.price = 35000
    p2.print()

    print(f'{p1.name = }')