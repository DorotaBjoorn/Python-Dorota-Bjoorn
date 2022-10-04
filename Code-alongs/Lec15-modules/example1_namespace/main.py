import os, sys

os.system("cls||clear")                 # ger nytt space i terminalen (Ctrl L ger samma)

print(f"{'='*30}main.py{'='*30}")       # snyggare utskrift ===========main.py============

#code imported from another module is executed when imoroted
import module1

# note __name__ is module1 when ran from outside of module1.py
# when module1.py is ran -> __name__ = "__main__"

#when improting a module - a refereance will be created in sys.modules
#print(globals())                        # dictionary som håller koll på våra variabler
print("global namespace")
print(globals()["module1"])                # printar en av keys inom dic globals

# when improting a module - it will be sotred in sys.modules
print("sys.modules")
print(sys.modules["module1"])




print(f"{'='*30}main.py{'='*30}")
