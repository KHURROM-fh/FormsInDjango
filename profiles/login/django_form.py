from django import forms 
from django.core import validators

# widget == field to html input
class djangoLoginForm(forms.Form):
    name= forms.CharField(label= "User Name : ", help_text= "Total length must be within 70 characters", required= False, widget= forms.Textarea(attrs= {'id' : 'text_area', 'class' : 'class1 class 2', 'placeholder' : 'Enter your full name'}), validators=[validators.MinLengthValidator(8, message="Enter a name with at least 8 characters")])
    email= forms.EmailField(label= "User Email")
    #age= forms.IntegerField()
    #age= forms.CharField(widget= forms.NumberInput)
    age= forms.IntegerField(validators=[validators.MaxLengthValidator(34, message="Age must be maximum 34"), validators.MinLengthValidator(21, message="age must be at least 21")])
    birthday= forms.CharField(widget= forms.DateInput(attrs={'type' : 'date'}))
    appontment= forms.CharField(widget= forms.DateInput(attrs={'type' : 'datetime-local'}))
    check= forms.BooleanField()
    file= forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message='File EWxtension must be ended with .pdf')])
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size= forms.ChoiceField(choices = CHOICES, widget= forms.RadioSelect)
    balance= forms.DecimalField()
    MEAL= [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B','Beef')]
    pizza= forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
