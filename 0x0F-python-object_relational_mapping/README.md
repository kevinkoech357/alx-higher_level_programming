# 0x0F-python-object_relational_mapping
Object-Relational Mapping (ORM) is a programming technique used to convert data between incompatible type systems in object-oriented programming languages and relational databases. It provides a way to access your database using a series of attributes and methods attached to objects, instead of writing SQL commands.

ORMs create a "virtual object database" that you can interact with from within your programming language. They automate the transfer of data stored in relational databases into objects that are more commonly used in application code.

There are several benefits to using ORMs. They can save you a lot of time and help control access to your database. For example, they can ensure that whenever and wherever any row or field in your database is accessed, your custom code is executed first.

There are several ORM implementations available in Python, including:

    * SQLAlchemy: This well-regarded ORM gets the abstraction level "just right" and makes complex database queries easier to write.

    * Peewee: This ORM is written to be "simpler, smaller and more hackable" than SQLAlchemy.

    * Pony ORM: This is another Python ORM that is available as open source under the Apache 2.0 license.

    * SQLObject: This ORM has been under active open source development for over 14 years.

Here is a simple example of how you might use SQLAlchemy to interact with a database:
```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create engine
engine = create_engine('sqlite:///example.db')

# create session
Session = sessionmaker(bind=engine)
session = Session()

# query the database
for instance in session.query(MyTable).order_by(MyTable.id):
    print(instance.name, instance.fullname)
```
In this example, MyTable is a SQLAlchemy model representing a table in your database.
The ```session.query(MyTable)``` line is equivalent to ```SELECT * FROM MyTable``` in SQL.
This shows how you can interact with your database using Python objects and methods, rather than writing raw SQL.

