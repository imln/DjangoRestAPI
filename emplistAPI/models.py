from django.db import models

# Create your models here.
class Employee(models.Model):  
	eid = models.AutoField(primary_key=True)  
	ename = models.CharField(max_length=100)  
	econtact = models.CharField(max_length=15)
	def __str__(self):
	  	return self.ename

	class Meta:  
		db_table = "employee"