"""
import pandas as pd
import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=UHRCRU;DATABASE=Bike;Trusted_Connection=no;')

# Query 3.1: List all products
print("\nList all products:")
products_df = pd.read_sql("SELECT * FROM production.products", conn)
print(products_df.head())

# Query 3.2: Products by price descending
price_desc_df = pd.read_sql(
    "SELECT product_name, list_price FROM production.products ORDER BY list_price DESC", 
    conn
)
print("\nProducts by price descending:")
print(price_desc_df.head())

# Query 3.3: Top 3 most expensive
top3_df = pd.read_sql(
    "SELECT TOP 3 product_name, list_price FROM production.products ORDER BY list_price DESC", 
    conn
)
print("\nTop 3 most expensive products:")
print(top3_df)

conn.close()
"""
import pyodbc

def execute_sql_operations():
    
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=UHRCRU;'
        'DATABASE=Bike;'
        'Trusted_Connection=no;'
    )
    cursor = conn.cursor()

    try:
       
        print("1. Masking phone numbers...")
        cursor.execute("""
            UPDATE sales.customers
            SET phone = 
                CASE 
                    WHEN phone IS NULL THEN NULL
                    WHEN LEN(phone) >= 10 THEN '***-***-' + RIGHT(phone, 4)
                    ELSE phone
                END
            WHERE phone IS NOT NULL
        """)
        conn.commit()
        print(f"→ Updated {cursor.rowcount} phone numbers")

        cursor.execute("""
            SELECT TOP 5 customer_id, phone 
            FROM sales.customers 
            WHERE phone LIKE '***-***-%'
        """)
        print("\nSample masked phones:")
        for row in cursor:
            print(f"{row.customer_id}: {row.phone}")

        print("\n2. Creating test order...")
        
        cursor.execute("""
            INSERT INTO sales.customers 
            (first_name, last_name, email, phone)
            OUTPUT INSERTED.customer_id
            VALUES ('Test', 'Python', 'python@test.com', '***-***-9999')
        """)
        customer_id = cursor.fetchone()[0]
        print(f"→ Created customer ID: {customer_id}")

        cursor.execute("""
            INSERT INTO sales.orders 
            (customer_id, order_status, order_date, required_date, store_id, staff_id)
            OUTPUT INSERTED.order_id
            VALUES (?, 1, GETDATE(), DATEADD(day, 7, GETDATE()), 1, 1)
        """, customer_id)
        order_id = cursor.fetchone()[0]
        print(f"→ Created order ID: {order_id}")

        items = [
            (order_id, 1, 1, 1, 299.99, 0.1),  
            (order_id, 2, 2, 1, 499.99, 0.0)   
        ]
        cursor.executemany("""
            INSERT INTO sales.order_items 
            (order_id, item_id, product_id, quantity, list_price, discount)
            VALUES (?, ?, ?, ?, ?, ?)
        """, items)
        conn.commit()

        print("\n3. Verification:")
        cursor.execute("""
            SELECT 
                c.customer_id, o.order_id, 
                p.product_name, oi.quantity, oi.list_price, oi.discount
            FROM sales.orders o
            JOIN sales.customers c ON o.customer_id = c.customer_id
            JOIN sales.order_items oi ON o.order_id = oi.order_id
            JOIN production.products p ON oi.product_id = p.product_id
            WHERE o.order_id = ?
        """, order_id)
        print("\nOrder details:")
        for row in cursor:
            print(f"Customer {row.customer_id}, Order {row.order_id}:")
            print(f"- {row.product_name}: {row.quantity} × ${row.list_price} (Discount: {row.discount*100}%)")

    except Exception as e:
        print(f"\nError: {str(e)}")
        if conn:
            conn.rollback()
    finally:
        cursor.close()
        conn.close()
        print("\nConnection closed.")

if __name__ == "__main__":
    execute_sql_operations()