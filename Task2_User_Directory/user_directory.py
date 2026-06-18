import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Fetch data
response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    users_data = []

    # Extract required information
    for user in users:

        user_info = {
            "Name": user["name"],
            "Email": user["email"],
            "Phone": user["phone"],
            "Company": user["company"]["name"],
            "City": user["address"]["city"]
        }

        users_data.append(user_info)

    # Create DataFrame
    df = pd.DataFrame(users_data)

    # Display DataFrame
    print("\nUser Directory:")
    print(df)

    # Save CSV
    df.to_csv("users.csv", index=False)

    print("\nCSV file saved as users.csv")

    # Search User by Name

    search_name = input("\nEnter a name to search: ").strip()

    name_result = df[
        df["Name"].str.contains(search_name, case=False, na=False)
    ]

    print("\nSearch Result (Name):")

    if not name_result.empty:
        print(name_result)
    else:
        print("No user found.")

    # Search User by Company

    search_company = input("\nEnter a company name to search: ").strip()

    company_result = df[
        df["Company"].str.contains(search_company, case=False, na=False)
    ]

    print("\nSearch Result (Company):")

    if not company_result.empty:
        print(company_result)
    else:
        print("No company found.")

else:
    print("Failed to fetch data from API.")
