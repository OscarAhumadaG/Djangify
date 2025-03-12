# Verify Django version
"""
python -m django --version
"""

# Update Django version
"""
pip install --upgrade django
"""

# Start Project
"""
django-admin startproject name_of_the_project
"""

# Run development server
"""
python manage.py runserver
"""

# Creates a new Django app named 'main' within the project.
"""
python manage.py startapp main
"""

# Applies pending migrations to the database to ensure the schema is up to date with the defined models.
"""
python manage.py migrate
"""

# Creates migration files for the 'main' app based on model changes.
"""
python manage.py makemigrations main 
"""

# To open python shell in Django
"""
python manage.py shell 
"""

# To create the superuser in the admin tab
"""
http://127.0.0.1:8000/admin/

python manage.py createsuperuser
"""


# To add a ToDoList into the database
"""
from main.models import Item, ToDoList
t = ToDoList(name="Oscar\'s List")
t.save()
ToDoList.objects.all()
<QuerySet [<ToDoList: Oscar's List>]>
oDoList.objects.get(id=1)
<ToDoList: Oscar's List>
oDoList.objects.get(name="Oscar's List)
<ToDoList: Oscar's List>
"""

# To add an item into the ToDoList
"""
 t.item_set.create(text="Go to the mall", complete=False)
<Item: Go to the mall>
t.item_set.all()
<QuerySet [<Item: Go to the mall>]>
t.item_set.get(id=1)
<Item: Go to the mall>
"""

# To delete a  ToDoList
"""
del_object = t.get(id=1)
del_object.delete()
"""


"""
quit()
"""



# https://www.youtube.com/watch?v=ZxMB6Njs3ck&t=206s

#  https://www.youtube.com/watch?v=sm1mokevMWk
