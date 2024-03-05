# Ex02 Django ORM Web Application
## Date: 05.03.24

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Book_DB,BOOK_DBAdmin
admin.site.register(Book_DB,BOOK_DBAdmin)

models.py

from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
       authorname=models.CharField(max_length=20);
       bookname=models.CharField(max_length=50);
       bookno=models.IntegerField(primary_key="bookno");
       version=models.IntegerField();
       pages=models.IntegerField(default=0);
class BOOK_DBAdmin(admin.ModelAdmin):
      list_display=("bookno","authorname","bookname","version","pages");
      ```

## OUTPUT:

![output](./output.png)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
