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

