import sqlite3

DATABASE_NAME = "products.db"



def create_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL
        )
    """)

    conn.commit()
    conn.close()


def add_data(db_name, products_list):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products_list)

    connection.commit()
    connection.close()


def read_data(database_name):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, price FROM products")
    records = cursor.fetchall()

    connection.close()
    return records



def main():
    print(f"[{DATABASE_NAME}] database and 'products' tables are being created/being controlled...")
    create_db(DATABASE_NAME)
    print("->  Creation/Control completed.")

    new_products = [
        ("Laptop", 2000.00),
        ("Keyboard", 230.00),
        ("Mouse", 150.75)
    ]

    print("\nDatas are being inserted to the database...")
    add_data(DATABASE_NAME, new_products)
    print(f"-> {len(new_products)} number of products added successfully.")

    print("\nReading all products from the database...")
    all_products = read_data(DATABASE_NAME)

    print("\n--- PRODUCT LIST ---")
    if all_products:
        for id, name, price in all_products:
            print(f"ID: {id}, Name: {name}, Price: {price:.2f} EURO")
    else:
        print("No products found in the database.")
    print("--------------------")


if __name__ == "__main__":
    main()
