import pytest
def product_details(name, id,Quantity,Price):
    result=(
        f"Product Name: {name}\n"
        f"Product ID: {id}\n"
        f"Quantity: {Quantity}\n"
        f"Price: {Price}\n"    )
    return result
    
if __name__=="__main__":
    name="Dell Laptop"
    id="P1001"
    Quantity="10"
    Price=75000
    print(product_details(name, id, Quantity, Price))    