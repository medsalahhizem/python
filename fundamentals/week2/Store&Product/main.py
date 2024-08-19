from Products import Product 
from Store import Store 
def main():
  article1=Product(1,"pull",70,"polo")
  article2=Product(2,"chemise",110,"9amraya")
  
  Shop1=Store("zen",list_product=None)
  
  Shop1.add_product(article1)
  Shop1.add_product(article2)
  Shop1.display_product()
  
  Shop1.sell_product(2)
  print("the store after selling chemise")
  Shop1.display_product()
  
  Shop1.Inflation(0.2)
  Shop1.display_product()
  


if __name__ == "__main__":
    main()