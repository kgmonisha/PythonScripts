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
    Product("phone",100,8,0.5),
    Product("watch",90,7,0.1)
]

print(sorted(prodList,key=prodSort))
print(sorted(prodList,key=lambda p:p.price))
print(sorted(prodList,key=lambda p:p.name))
print(sorted(prodList,key=lambda p:p.discountPrice()))
print("-----------------------------")
#reverse sorting using price
print(sorted(prodList,key=lambda p:p.price,reverse=True))
print("-----------------------------")
#dual sorting(reverse sorting using price but with increasing weights)
result = sorted(prodList,key=lambda p:p.weight)
print(sorted(result,key=lambda p:p.price,reverse=True))