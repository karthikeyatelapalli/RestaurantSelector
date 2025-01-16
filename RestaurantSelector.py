#Restaurant Selector 
#Description
'''This program uses user input to inform the user and programmer Of the list of restaurants the user could potentially go
to depending on their dietary restrictions. This helps us narrow down the choice of restaurants we would like to go.'''    

vegetarian = input("Is anyone in your party a vegetarian? (Yes/No)").lower()
vegan = input("Is anyone in your party a vegan? (Yes/No)").lower()
gluten_free = input("Is anyone in your party gluten-free? (Yes/No)").lower()

#takes user input for vegitarian, vegan and gluten free options


restaurants = []

#creates empty list named restaurants

if vegetarian == "yes":
    restaurants += ["Bella's Italian Restaurant", "Gourmet Pizza Company", "True Food Kitchen"]
if vegan == "yes":
    restaurants = ["True Food Kitchen"]
if gluten_free == "yes":
    restaurants += ["Gourmet Pizza Company", "True Food Kitchen"]

restaurants = list(set(restaurants))

#updates list with user choices and removes any duplicate results

if restaurants:
    print("Here are your restaurant choices:")
    for r in restaurants:
        print(r)
else:
    print("Sorry, there are no restaurant options for your party.")

#if none are matched then else will be printed
