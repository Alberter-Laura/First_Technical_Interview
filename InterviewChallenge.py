# Author some code that will pull the data from the API
# (https://fakestoreapi.com/products) and display the
# id, title, and rating for items that have a rating greater than
# 3 and more than 100 ratings to either the console or an output file (CSV?)


import json
import requests

# Pulling data from API
fakeStore_API = requests.get('https://fakestoreapi.com/products')
data = fakeStore_API.json()

# Testing
# print(data)
# print(fakeStore_API.status_code)

# Declaring new array
filtered_items = []

# iterating through JSON data
for item in data:
    # filtering the key-value pair objects
    if item['rating']['rate'] > 3 and item['rating']['count'] > 100:
        # adding object to new array
        filtered_items.append({'id' : item['id'], 'title' : item['title'], 'rating' : item['rating']['rate']} )
        # print(item)

print(json.dumps(filtered_items, indent=3))