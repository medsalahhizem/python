from Products import Product 

class Store:
  def __init__(self, name,list_product=None):
        self.name = name
        if list_product is None:
            self.list_product = []
        else:
            self.list_product = list_product
  
  
  def add_product(self,new_product):
    self.list_product.append(new_product)
  
  def sell_product(self,id):
      for product in self.list_product:
        if product.id==id:
          self.list_product.remove(product)
  
  
  def Inflation(self, percent_increase):
    for product in self.list_product:
          product.Update_price(percent_increase,False)
      
  
  def set_clearence(self,category,percent_discount):
    for product in self.list_product:
      if product.category==category:
          product.Update_price(percent_discount,True)
        
  def display_product(self):
    for product in self.list_product:
        product.print_info()
        
