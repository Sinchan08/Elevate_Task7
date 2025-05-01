import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # e.g., "root"
    password="Sinchana@26",   # replace with your MySQL password
    database="sales_db"
)

# Step 2: Run SQL query
query = """
    SELECT 
        product,
        SUM(quantity) AS total_quantity,
        SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
"""

df = pd.read_sql(query, conn)
print("Sales Summary:\n", df)

# Step 3: Plot revenue by product
df.plot(kind='bar', x='product', y='revenue', color='orange')

plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Step 4: Close connection
conn.close()
