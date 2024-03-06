from django.db import models
from  django.contrib  import admin 
class Student_DB(models.Model):
   regno=models.IntegerField(primary_key="regno"); 
   name=models.CharField(max_length=20);
   email=models.EmailField();
   DoB=models.DateField();
   cgpa=models.IntegerField();
class Student_DBAdmin(admin.ModelAdmin):
    list_display=("regno","name","email","DoB","cgpa");
