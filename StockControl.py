## Advanced Programming, coursework 1: Object Orientation
## test
## The stock control system classes are unfinished.
## Work through the 14 steps of the coursework to
## implement and extend the methods and classes.
##
##

## Student's Name:
## Student's Number:

from datetime import date

"""A stock control system"""



class StockControlSystemError(Exception):
    """Base class for exceptions in this module."""
    pass

class SoldOutOfStockError(StockControlSystemError):
    """Raised when an item is sold that isn't in stock
    Attributes:
    item -- item being sold
    """
    def __init__(self, item):
        self.item = item

class ItemNotFoundError(StockControlSystemError):
    """Raised when an item is sold that isn't in the stock list
    Attributes:
    barcode -- barcode of item being sold
    """
    def __init__(self, barcode):
        self.barcode = barcode


class StockItem(object):
    """Provides the basic stock item class for the stock control system"""
    
    def __init__(self, name, barcode, quantity):
        """Provides the basic stock item class for the stock control system
        name     -- name of product (string)        
        barcode  -- barcode of product item (string)        
        quantity -- number of items in stock (integer)
        """
        self.name = name;
        self.barcode = barcode;
        self.quantity = quantity;        

    def toString(self):
        """Returns a string describing the stock item, its barcode and the quantity remaining"""
        #TODO complete this method
        itemdetails = "Item Name: " + self.name + " Barcode: " + self.barcode + " Quantity: " + str(self.quantity)
        return itemdetails
        #pass 
    
    def needRestock(self):
        """Returns true if this item needs restocking (i.e. the quantity<a threshold)"""
        #TODO check if the quantity<threshold and return true if it is
        #we'll set for now the threshold at *five* items
        #so we need to check if self.quantity is less than five.
        if self.quantity < 5:
            return True
        #pass
        
    
    def sell(self):
        """Process the sale of an item, generates an exception if an item is sold when its stock is zero"""
        #TODO
        #hint: use the raise method to create an exception.
        #it will return the error sold out if stock is zero
        if self.quantity > 0:
            self.quantity -= 1
        else:
            raise SoldOutOfStockError(self)
        #pass
       
    def restockItem(self, quantity):
        """Processes the restocking of item of any quantity"""
        self.quantity = self.quantity + quantity
        
    
class StockControl(object):
    """The stock control system"""
    
    def __init__(self):
        """The stock control system"""
        #note: we could have implemented the list as a dictionary, with
        #the barcode as the key, however if the barcode for the item
        #changes we might have problems.
        self.stocklist = [] #a list of stock items
        self.Restocklist = [] #a list of item that need restocking
    
    def listRestock(self):
        """Return a string listing items that need restocking"""
        #TODO return a list of items that need restocking
        #hint: Need to loop through the stocklist
         for item in self.stocklist:
            #StockItem
            if StockItem.needRestock(item):
                print(StockItem.toString(item))
                self.Restocklist.append(StockItem.toString(item))
        if len(self.Restocklist) == 0:
            print("All items stocked")
        #pass
    
    def addStockType(self,item):
        """Add an item to the stock list"""
        #TODO
        #hint: add an item to this.stocklist
        self.stocklist.append(item)
        #pass
    
    def sellStock(self,barcode):
        """Process the sale of one item"""
        #TODO
        #hint: look through the list of items,
        #and call the 'sell' method of the relevant item
        #return an error if the product isn't found
        #pass
        objectitem = []
        for item in self.stocklist:
            if item.barcode == barcode:
                objectitem.append(item)
        if len(objectitem) >0:
            for item in objectitem:
                if item.quantity > 0:
                   item.quantity = item.quantity - 1
                   objectitem = []
                else:
                   raise SoldOutOfStockError(item)
        else:
            raise ItemNotFoundError(barcode)
            
    def restock(self, barcode, quantity):
        """Processes the restocking of any quantity of an item, raises an exception if the barcode of an item is not found"""
        objectitem = []
        for item in self.stocklist:
            if item.barcode == barcode:
                objectitem.append(item)

        if len(objectitem) >0:
            item.restockItem(quantity)
            objectitem = []
        else:
            raise ItemNotFoundError(barcode)
            
#Below is some code to test the classes. Feel free
#to alter this test-code to test your submission
#more thoroughly.

#Populate the stock control system
stockctrl = StockControl()
stockctrl.addStockType(StockItem('Bag of Coffee','1234',23))
stockctrl.addStockType(StockItem('Salt and Vinegar Crisps','4434',3))
stockctrl.addStockType(StockItem('Museli','0191',2))
stockctrl.addStockType(StockItem('Flour (1kg)','1191',24))
#uncomment to test the PerishableStockItem class for milk
#stockctrl.addStockType(PerishableStockItem('Milk (500ml)','1191',24,date(2013, 10, 26)))
stockctrl.addStockType(StockItem('Cookies','2312',6))
stockctrl.addStockType(StockItem('Bags of grapes','1111',0))

#Find out what needs restocking
print("Items that need restocking:\n")
print(stockctrl.listRestock())

#Sell some items
print("\n")
print("Testing sales:")
for barcode in ['1234','2312','1112','1111','2312','1191','0191','2312']:
    try:
        stockctrl.sellStock(barcode)    
    except SoldOutOfStockError as (e):
        print("Stock sold which isn't in stock:" + e.item.toString())
    except ItemNotFoundError as (e):
        print("Item not found:" + e.barcode)

print("\nItems that need restocking:\n")
print(stockctrl.listRestock())

#Uncomment this section to test the restock method
#print("\nRestocking...\n")
#for barcode in ['1111','0191','2312','4434','2312','9999']:
#    try:
#        stockctrl.restock(barcode,10)    
#    except ItemNotFoundError as (e):
#        print("Item not found:" + e.barcode)
    

