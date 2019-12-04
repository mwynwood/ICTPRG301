# Examples of how to use a SQLite Database
import sqlite3

# Connect to a Database
# db = sqlite3.connect('example.db') # Creates or Opens a database called "example.db"
db = sqlite3.connect(':memory:') # Create a database in RAM

# Setup a cursor to allow us to do things with the database
cursor = db.cursor()

# Execute an SQL statemant, in this case we're creating a table
cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, email TEXT)
''')

# Commit the changes we've made to the database
db.commit()

# Let's get some data...
name1 = "Geordi La Forge"
email1 = "geordi@enterprise.com"
name2 = "William Riker"
email2 = "number1@enterprise.com"
name3 = "Worf"
email3 = "worf@enterprise.com"
name4 = "Beverly Crusher"
email4 = "bev@enterprise.com"
name5 = "Deanna Troi"
email5 = "deanna@enterprise.com"
name6 = "Jean-Luc Picard"
email6 = "captain@enterprise.com"

# Now let's store that info in our database
# The ? is used as a placeholder for our variables
# A query where placeholders are used for parameters is called a "parameterized query"
# Parameterized Queries reduce execution time and prevent SQL injection attacks
# Don't just put strings directly into your query, that's a massive security risk!
cursor.execute('''INSERT INTO users(name, email) VALUES(?,?)''', (name1, email1))
cursor.execute('''INSERT INTO users(name, email) VALUES(?,?)''', (name2, email2))
cursor.execute('''INSERT INTO users(name, email) VALUES(?,?)''', (name3, email3))
cursor.execute('''INSERT INTO users(name, email) VALUES(?,?)''', (name4, email4))
cursor.execute('''INSERT INTO users(name, email) VALUES(?,?)''', (name5, email5))
cursor.execute('''INSERT INTO users(name, email) VALUES(?,?)''', (name6, email6))

# Commit the changes we've made to the database
db.commit()

# To get data from the database, we can run a SELECT statement
cursor.execute('''SELECT * FROM users''')
# If we want just the first result returned, then we can use fetchone()
user1 = cursor.fetchone()
# We can return the whole row
print(user1)
# We can return any column
print(user1[1])

print("")

# If we want all the results from our query, then we can use fetchall()
cursor.execute('''SELECT * FROM users''')
all_rows = cursor.fetchall()
# We can then loop through the results and print out each row
for row in all_rows:
    print(row)

print("")

# Another way is to iterate throught the cursor object - it calls fetchall() automatically for us
cursor.execute('''SELECT * FROM users''')
for row in cursor:
    print(row)

print("")

# To include a variable in an SQL statement, use the ? placeholder
user_id = 2
cursor.execute('''SELECT name, email FROM users WHERE id=?''', (user_id,))
user = cursor.fetchone()
print(user)

# When you're finished, close the database connection
db.close()
