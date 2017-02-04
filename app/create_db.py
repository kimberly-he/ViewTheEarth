from app import db
from app.models import Country

# create the database and the db table
db.create_all()

with open('country_data.txt') as f:
    lines = f.readlines()

for line in lines:
    elements = line.split("\t")
    db.session.add(Country(elements[0], elements[3], elements[5], elements[4], elements[6]))

# commit the changes
db.session.commit()

