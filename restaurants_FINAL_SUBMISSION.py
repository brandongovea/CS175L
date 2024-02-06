#CS175L
#Brandon Govea
#restaurant

vegetarian = False
vegan = False
gluten_free = False

response = input("Is anyone in your party a vegetarian? ")
if response == "Yes":
    vegetarian = True


response = input("Is anyone in your party a vegan? ")
if response == "Yes":
      vegan = True


response = input("Is anyone in your party gluten free? ")
if response == "Yes":
    gluten_free = True

print(" ")


print("Here are your restaurant choices:")
if vegetarian == False and vegan == False and gluten_free == False:
    print("Joe's Gourmet Burgers")
    print("Mama's Fine Italian")
    print("Main Street Pizza Company")
    print("Corner Café")
    print("The Chef's Kitchen")
    
if vegetarian == True and vegan == False and gluten_free == False:
    print("Mama's Fine Italian")
    print("Main Street Pizza Company")
    print("Corner Café")
    print("The Chef's Kitchen")
    
if vegetarian == False and vegan == False and gluten_free == True:
    print("Main Street Pizza Company")
    print("Corner Café")
    print("The Chef's Kitchen")

if vegetarian == True and vegan == False and gluten_free == True:
    print("Main Street Pizza Company")
    print("Corner Café")
    print("The Chef's Kitchen")

if vegetarian == False and vegan == True and gluten_free == False:
    print("Corner Café")
    print("The Chef's Kitchen")

if vegetarian == False and vegan == True and gluten_free == True:
    print("Corner Café")
    print("The Chef's Kitchen")

if vegetarian == True and vegan == True and gluten_free == False:
    print("Corner Café")
    print("The Chef's Kitchen")

if vegetarian == True and vegan == True and gluten_free == True:
    print("Corner Café")
    print("The Chef's Kitchen")
