from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.views.generic import View,TemplateView,DetailView,ListView
from .models import Person,Transaction_history
from . import forms
from django.template.loader import get_template


from .utils import render_to_pdf 

#Creating our view, it is a class based view

# Create your views here.
def home(request):
    return render(request,"home.html")

class Nameslist(ListView):
    model=Person
    template_name="../templates/Person/person_list.html"

def detail(request):
    All_Names=Person.objects.values_list('name',flat=True)
    All_Credit=Person.objects.values_list('credit',flat=True)
    
    text={"obj":All_Names,
            "obj1":All_cred}
    return render(request,"details.html",text)

def add(request):    
    Person_list_details=Person.objects.all().values()
    context={"Person_list_details":Person_list_details}
    return render(request,"add.html",context)
def addc(request,id):
    try:
        Person_list=Person.objects.all().values().filter(id=id)
        Person_list_details=Person.objects.all().values()
        for i in Person_list:
            names=i['name']
        form=forms.formname()
        form.getform(id)
        Transaction_history_list=Transaction_history.objects.all().values().filter(Sender=id)|Transaction_history.objects.all().values().filter(Reciever=id).order_by('-Time')
        k={}
        for i in Person_list_details:
            k[int(i['id'])]=i['name']
        
        def get(id):
            return k[id]
        for i in Transaction_history_list:
            i['Sender']=get(i['Sender'])
            i['Reciever']=get(i['Reciever'])
        context={"Person_list":Person_list,
        "Person_list_details":Person_list_details,
        'form':form,
        "Transactions":Transaction_history_list,
        "names":names,
        }
        for person in Person_list:
            Senders_credit=person['credit']
       
        
        if request.method=='POST':
            f=forms.formname(request.POST)  
           
            if f.is_valid():
                if int(f.cleaned_data['cred'])<=Senders_credit:

                    
                    Transfered_credit=f.cleaned_data['cred']
                    d=f.cleaned_data['Transfer_to']
                   
                    Sender=Person.objects.filter(id=id)
                    l=[]
                    for k in Sender:
                        l.append(k.id)
                        l.append(k.credit)
                        k.credit-=int(Transfered_credit)
                        
                        k.save()
                    Reciver=Person.objects.filter(id=d)
                    l1=[]
                    for k in Reciver:
                        l1.append(k.id)
                        l1.append(k.credit)
                        k.credit+=int(Transfered_credit)  
                        k.save()
                    p=Transaction_history(Sender=int(l[0]),Sender_Credit=l[1],Reciever=int(l1[0]),Reciever_Credit=l1[1],Credit=Transfered_credit)
                    
                    p.save()
                    
                    return redirect("/home/list")
                else:
                    Person_list=Person.objects.all().values().filter(id=id)
                    Person_list_details=Person.objects.all().values()
                    form=forms.formname()
                    form.getform(id)
                    form["cred"].initial =f.cleaned_data['cred']
                    form["Transfer_to"].initial =f.cleaned_data['Transfer_to']
                    error="negative credits"
                    
                    context={"Person_list":Person_list,
                    "Person_list_details":Person_list_details,
                    'form':form,
                    'err':error,
                    "Transactions":Transaction_history_list,
                    "names":names,}
                    
                    return render(request,"cred.html",context)
            else:
               
                context={"Person_list":Person_list,
                    "Person_list_details":Person_list_details,
                    'form':form,
                    'errMsg':"Enter some positive amount"}
                    
                return render(request,"cred.html",context)
        
        return render(request,"cred.html",context)
    except Exception as e:

       
        print(e)
    

def sucess(request,id):
    return HttpResponse("hello")
class GeneratePdf(View):
     def get(self, request,*args, **kwargs):
        
        #getting the template
        id=3
        Person_list=Person.objects.all().values().filter(id=id)
        Person_list_details=Person.objects.all().values()
        for i in Person_list:
            names=i['name']
        form=forms.formname()
        form.getform(id)
        Transaction_history_list=Transaction_history.objects.all().values().filter(Sender=id)|Transaction_history.objects.all().values().filter(Reciever=id).order_by('-Time')
        k={}
        for i in Person_list_details:
            k[int(i['id'])]=i['name']
        
        def get(id):
            return k[id]
        for i in Transaction_history_list:
            i['Sender']=get(i['Sender'])
            i['Reciever']=get(i['Reciever'])
        context={'form':form,
        "Transactions":Transaction_history_list,
        "names":names,
        }
         
        pdf = render_to_pdf('invoice.html',context)
        return HttpResponse(pdf, content_type='application/pdf')