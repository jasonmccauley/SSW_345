# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None
    __inventory = 0

    def __init__(self, sale: Sale):
        self.__lastSale = sale

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    def setInventory(self, lastSale: Sale):
        self.__inventory += 1

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale
    
    @property
    def getInventory(self) -> int:
        return self.__inventory
    
    def __getitem__(self, item):
        return self

# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product]):  #, saleNumber: int = 1):
        Sale.__saleTimes +=1
        self.__product = product
        self.__saleNumber = Sale.__saleTimes
        for index, product in enumerate(product):
            product[index].setLastSale(self)
            product[index].setInventory(self)

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber
    


productOne = Product(sale=None)
productTwo = Product(sale=None)
productThree = Product(sale=None)

saleOne = Sale([productOne, productTwo])
saleTwo = Sale([productOne])
saleThree = Sale([productTwo])
saleFour = Sale([productOne, productTwo, productOne])
saleFive = Sale([productTwo, productTwo])

print(f"Product One Inventory: {productOne.getInventory} \nProduct Two Inventory: {productTwo.getInventory} \nProduct Three Inventory: {productThree.getInventory}")
