class Product:
  def __init__(self,id,name,price,category):
    self.id=id
    self.name = name
    self.price=price
    self.category=category

  def print_info(self):
    print(f"the name of the product is {self.name}\n"
          f"the category {self.category} \n"
          f"the price is {self.price}\n \n")
    
  def Update_price(self,percent_change,Is_incresed):
    if Is_incresed:
      self.price*=(1+percent_change)
    else:
      self.price*=(1-percent_change)
      