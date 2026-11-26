products = [10,20,30,40]
try:
    print(products[8])
except IndexError as e:
    print("Product does not exist:",e)
print("Inventory checked")