from django.db import models

# Create your models here.
class tbl_students(models.Model):
    S_id=models.IntegerField()
    Name=models.CharField(max_length=30)
    Student_class=models.IntegerField()
    Marks=models.IntegerField()
    Status=models.CharField(max_length=30)
    Parent_Name=models.CharField(max_length=30)
    Contact_Number=models.IntegerField()
    class Meta:
        db_table='tbl_students'

class tbl_teacher(models.Model):
    T_id=models.IntegerField()
    Name=models.CharField(max_length=30) 
    
    Phone=models.IntegerField()
    Email=models.EmailField()
    Address=models.CharField(max_length=30)
    Salary=models.IntegerField()
    Subject=models.CharField(max_length=30)
    class Meta:
        db_table='tbl_teacher'
    
class tbl_staff(models.Model):
    St_id=models.IntegerField()
    Name=models.CharField(max_length=30)
    Department=models.CharField(max_length=30)
    Experience=models.IntegerField()
    Phone=models.IntegerField()
    Email=models.EmailField()
    Salary=models.CharField(max_length=30)
    class Meta:
        db_table='tbl_staff'


