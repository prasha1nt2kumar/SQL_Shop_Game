# missions.py

missions = [
    {
        "id": 1,
        "question": "List all products.",
        "expected_query": "SELECT * FROM products;"
    },
    {
        "id": 2,
        "question": "List all customers.",
        "expected_query": "SELECT * FROM customers;"
    },
    {
        "id": 3,
        "question": "Show the names and prices of all products.",
        "expected_query": """
            SELECT name, price FROM products;
            
        """
    },
    {
        "id": 4,
        "question": "Show the names of customers in alphabetical order.",
        "expected_query": """
             select name FROM customers order by name asc;
        """
    },
    {
        "id": 5,
        "question": "Show the names of products that cost more than 100.",
        "expected_query": """
            select name FROM products where price > 100;
        """
    },
    {
       "id": 6,
        "question": "Show all orders placed after January 1, 2023.",
        "expected_query": """
            select  * FROM orders where order_date > '2023-01-01';
        """ 
    },
    {
       
       "id": 7,
        "question": "Show the total number of orders in the database. Use Alias name as ""total_orders""",
        "expected_query": """
            SELECT COUNT(*) AS total_orders FROM orders;
        """  
    },
    {
        "id": 8,
        "question": "Show the average price of all products. Use Alias name as ""average_price"" ",
        "expected_query": """
            SELECT AVG(price) AS average_price FROM products;
        """  
    },
    {
        "id": 9,
        "question": "Show the most expensive product and its price.Hint use limit ",
        "expected_query": """
            SELECT name, price
            FROM products
            ORDER BY price DESC
            LIMIT 1;
        """  
    }
    
]
