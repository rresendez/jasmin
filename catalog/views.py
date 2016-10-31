from django.shortcuts import render
#import CustomerForm from forms
from catalog.forms import CustomerForm

def register(request):
    #Create a form instance from POST data
    message1='Welcome to Jasmines'
    message2='Please register by entering the below information:'
    #if this is a POST request, process the data
    if request.method == 'POST':
          #create a form instance and populate it with data from the request
          form = CustomerForm(request.POST)
          #check if this form is valid based on the rules provided to the fields under the customer model
          if (form.is_valid()):
               #save() method accepts an optional commit keyword argument,
               #which accepts either True or False, where commit is true by default.
               #if commit=false, then it will return an object that hasn’t yet been 
               #saved to the database.  This is useful if you want to preprocess the data or change it
               newCustomer=form.save(commit=False)
               #you can modify the input data at this point if needed or use it 
               customerName=newCustomer.fname + ' ' + newCustomer.lname       
               #save record to Customer Model
               newCustomer.save(commit=True)
               #go to welcome.html template if customer record was added successfully
               return render(request, 'welcome.html', locals())
    else:
          #If not POST then set form to BLANK Customer form (with no POST variables)
          form = CustomerForm()
    return render(request, 'register.html', locals())

#import HttpResponse and HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
     #Create a form instance from POST data
    message1='Welcome to Car Catalog'
    message2='Please sign in or register to Car Catalog:'

    #if this is a POST request, process the data
    if request.method == 'POST':
        #if submit is Sign In, then redirect to signin url
        if(request.POST.get('submit')=='Sign In'):
            return HttpResponseRedirect('/signin/')
        #if submit is Register, then redirect to register url
        elif(request.POST.get('submit')=='Register'):
            return HttpResponseRedirect('/register/')
         
    return render(request, 'index.html', locals())

#import  SignInForm from forms
from catalog.forms import SignInForm
def signin(request):
    #Create a form instance from POST data
    message1='Welcome to Car Catalog'
    message2='Please enter your username and password to access Car Catalog:'

    #if this is a POST request, process the data
    if request.method == 'POST':
        #create a form instance and populate it with data from the request
        form = SignInForm(request.POST)
        #check if this form is valid based on field rules
        if (form.is_valid()):
            #if is_valid() method returns true, the form's data is place
            #in its cleaned_data attribute
            #Query Customer table to find out if the email address and password provided exists in Customer table
            registeredUser=Customer.objects.filter(email=form.cleaned_data['email'],
                                                    password=form.cleaned_data['password'])

            #user exists in Customer table then retrieve customer name and redirect to welcome url
            if registeredUser.exists():
                 for user in registeredUser:
                    customerName=user.fname + ' ' + user.lname
                 return render(request, 'welcome.html', locals())
            else:
                #else ask the user to try again
                message2='Incorrect username or password, please try again:'
                form=SignInForm()            
    else:
        form = SignInForm()
         
    return render(request, 'signin.html', locals())
