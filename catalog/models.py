from django.db import models
#import MultiSelectField module
from multiselectfield import MultiSelectField
# Create your models here.
class Customer(models.Model):

#Create list of tuples for each choices field where the first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. 
	
    genderList=(('Male','Male'),('Female','Female'))
    occupationList=(('Arts','Arts'),('Architecture','Architecture'),
  		 ('Advertising','Advertising'),('Accounting','Accounting'),
 		 ('Information Technology','Information Technology'),
 		 ('Clerical','Clerical'),
  		('Sales','Sales'),('Other','Other'))
    mediaList=(('Search Engine','Search Engine'),
    ('Social Network','Social Network'),
    ('Advertisement','Advertisement'),
    ('Friend','Friend'),('Other','Other'))
    
    fname = models.CharField(max_length=30,verbose_name='First Name', blank=False,null=False)
    lname = models.CharField(max_length=30,verbose_name='Last Name', blank=False,null=False)
    email = models.EmailField(null=False,verbose_name='Email',blank=False,primary_key=True)
    phoneNumber = models.CharField(max_length=12,verbose_name='phoneNumber',null=False,blank=False)

#use choices attribute to point to genderList; make sure to set default=None to avoid Django display an empty choice, ex: ----------
    gender = models.CharField(choices=genderList,max_length=6,verbose_name='Gender',null=False,blank=False,default=None)

#use choices attribute to point to occupationList; make sure to set default=None to avoid Django display an empty choice, ex: ----------
    occupation = models.CharField(choices=occupationList,max_length=30,verbose_name='Occupation',null=False,blank=False,default=None)

#change media to a MultiSelectField and use choices attribute to point to mediaList; make sure to set default=None to avoid Django display an empty choice, ex: -----
    media = MultiSelectField(choices=mediaList,max_length=200,verbose_name='Media',null=False,blank=False,default=None)
    
    comments=models.CharField(max_length=200,verbose_name='Comments',null=True,blank=True)
    password=models.CharField(max_length=100,verbose_name='Password', help_text='Please use at least one uppercase and a number', null=False,blank=False)
    registeredDate=models.DateTimeField(auto_now_add=True,auto_now=False)
    updatedDate=models.DateTimeField(auto_now_add=False,auto_now=True)
	
