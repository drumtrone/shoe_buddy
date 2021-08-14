# import libraries/dependences

import requests
import json

# import credentials from external text file and convert to a dictionary [include all form elements from a shopify checkout]
options = {}
#url = input("What shopify store do you want to search? ")
#search = input("What are you searching for? ")

url = "https://www.allbirds.com/"
#search = "Men's Tree Dashers - Kilimanjaro (Light Green Sole)"

f = open('options.txt', 'r')
for line in f:
    (key, val) = line.strip().split(':')
    options[key] = val

# Function that searches for key terms in a json product list


def searc_products():
    usr_query = input("What type of product are you looking for? ")
    r = requests.get(f"{url}products.json")
    products = json.loads((r.text))['products']

    found_products = {}
    k = 1
    for product in products:
        if usr_query in product['title']:
            found_products[k] = product['title']
            k += 1

    for choices in found_products:
        print(choices, found_products[choices])

    choice = input("Enter the number of the product you're looking for? ")
    while True:
        try:
            choice = int(choice)
            search = found_products[choice]
            break
        except:
            choice = input("Selection needs to be a number: ")

    return search


# Function to Check if item is available by searching throught the products json (shopname.com/products.json)
# Do this by comparing the desired user input against the 'title' in the json
# append the 'handle' to the url (shopname.com/products)

def check_availability(url, search):
    r = requests.get(f"{url}products.json")
    products = json.loads((r.text))['products']

    for product in products:
        product_name = product['title']

        if product_name == search:
            product_url = f"{url}products/{product['handle']}"
            return product_url
    return False


# If available open the site select size (may need to add a way to search for inputs for buttons and selects as well as a name/label for size)
# Click add to cart
# Click checkout
# fill in form with information from dictionary