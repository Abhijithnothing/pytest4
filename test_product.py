from product import product_details
def test_product_details():
    expected_output=(
    "Product Name: Dell Laptop\n"           
    "Product ID: E1001\n"
    "Quantity: IT\n"
    "Price: 75000\n"
    )
    assert product_details("Dell Laptop","P1001","10",75000) == expected_output
