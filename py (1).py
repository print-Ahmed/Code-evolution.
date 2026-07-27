#This is a code that assigns the user thier order based on thier input.It resembles the typical order selection at a restaurant.
print("Do you want a burger, pizza or a wrap?")
x=input()
if x == "burger":
    print("do you want cheese or bacon")
    a=input()
    if a == "cheese":
        print("Cheeseburger for you")
    elif a == "bacon":
        print("pork burger for you")


elif x == "pizza":
    print("pepperoni or vegetables?")
    f=input()
    if f == "pepperoni":
        print("pepperoni pizza. classic")
    elif f == "vegetables":
        print("Veggie supreme pizza!!!")

elif x == "wrap":
    print("chicken or falafel?")
    z=input()
    if z == "chicken":
        print("chicken wrap!")
    elif z == "falafel":
        print("Falafel wrap for yoy")
else:
    print("not on the menu...")
