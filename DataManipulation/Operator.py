from operator import itemgetter, attrgetter, methodcaller
class Product:
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.weight, self.discount))

    def discountPrice(self):
        return self.price*self.discount

def prodSort(Product):
    return Product.price

prodList = [
    Product("tv",100,10,0.5),
    Product("phone",80,8,0.5),
    Product("watch",90,7,0.1)
]

products = [("A",5),("B",10),("C",3)]
print(sorted(prodList,key=attrgetter("weight"),reverse=True))
print(sorted(prodList,key=methodcaller("discountPrice")))
print(sorted(products,key=itemgetter(1)))