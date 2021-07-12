from django import forms
from .models import Person
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator 

def validate_credit(value):
    if value < 0:
        raise ValidationError("Enter some positive amount")

class getid:
    def __init__(self,id):
        self.id=id
    
def getAllOptions():
    det=Person.objects.all().values()
    options = []
    for (index,item) in enumerate(det):
        options.append((item['id'],item['name']))
    return options


def gett(*argv):
    try:
        det=Person.objects.all().values()
        k=0
        for i in argv:
            k=i
        options = []
        for (index,item) in enumerate(det):
            if(item['id']==int(k)):
                pass
            else:
                options.append((item['id'],item['name']))
    except Exception as e:
        print(e)
    
    return options

class formname(forms.Form):

    cred=forms.IntegerField(validators=[MinValueValidator(1)])
    Transfer_to=forms.ChoiceField(choices=(getAllOptions()))

    def getform(self,id):
        self.fields["Transfer_to"]=forms.ChoiceField(choices=(gett(id)))
        
    # cred=forms.IntegerField(validators=[validate_credit])
    # Transfer_to=forms.ChoiceField(choices=(gett(0)
    # ))
