from Pets import Pet,Dog
from Ninjas import Ninja

def main():
    pet = Pet(name="snow", type="Dog", tricks=["sit", "roll over"])
    ninja = Ninja(first_name="John", last_name="Smith", treats=["bone", "biscuit"], pet_food="🍖", Pet=pet)
    
    dog= Dog(name="snow", tricks=["sit", "roll over"])
    salah = Ninja(first_name="John", last_name="Smith", treats=["bone", "biscuit"], pet_food="🍖", Pet=dog)

    ninja.walk()
    ninja.feed()
    
    print("so see here the difference between an subclass and a class for the both function when the noice function is called")
    ninja.bathe()
    salah.bathe()

if __name__ == "__main__":
    main()
