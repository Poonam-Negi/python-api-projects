import requests

# API URL
url = "https://fakestoreapi.com/products"

# Fetch data from API
response = requests.get(url)

if response.status_code == 200:

    products = response.json()

    # Total Products
    total_products = len(products)

    # Average Product Price
    total_price = 0

    for product in products:
        total_price += product["price"]

    average_price = total_price / total_products

    # Most Expensive Product
    most_expensive = max(products, key=lambda product: product["price"])

    # Cheapest Product
    cheapest = min(products, key=lambda product: product["price"])

    # Category-wise Product Count
    category_count = {}

    for product in products:

        category = product["category"]

        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1

    # Display Results
    print("\n" + "=" * 50)
    print("E-COMMERCE PRODUCT ANALYSIS")
    print("=" * 50)

    print(f"\nTotal Products: {total_products}")

    print(f"\nAverage Product Price: ${average_price:.2f}")

    print("\nMost Expensive Product:")
    print(f"Title : {most_expensive['title']}")
    print(f"Price : ${most_expensive['price']}")

    print("\nCheapest Product:")
    print(f"Title : {cheapest['title']}")
    print(f"Price : ${cheapest['price']}")

    print("\nCategory-wise Product Count:")
    print("-" * 30)

    for category, count in category_count.items():
        print(f"{category}: {count}")

else:
    print("Failed to fetch data from API.")
