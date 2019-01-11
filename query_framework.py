import os
import sqlite3
import time

## making a framework in which SQL query is written in a text file,
## and then imported and excuted in this python script


path = r"D:\Users\703143501\Documents\Genpact Internal\H\learning_sql\Jan_2019"
os.chdir(path)


### connecting to the database
db = 'tables.db'
conn = sqlite3.connect(db)


### importing the query from the text file
query_file = 'query.txt'
query = ''

for each in open(query_file, 'r'):
    query = query + each

newline = '\n'
query = " ".join(query.split(newline))


### executing the query
cursor = conn.execute(query)

### printing out some information about the query
print("Query Executed:")
print(query)
print("-" * 100)

### printing out the result
print("Query Result:")
for each in cursor:
    print(each)


### closing the connection to the database
conn.close()

### find the log version number
log_version = open('log_version.txt', 'r')
v = eval(log_version.read())
## new version number
v = str(v + 1)
