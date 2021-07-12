from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    credit=models.IntegerField(null=False)

    def __str__(self):
        return self.name
    def getname(self):
        return self.name
class Transaction_history(models.Model):
    Sender=models.IntegerField(null=True)
    Sender_Credit=models.IntegerField(null=True)
    Reciever=models.IntegerField(null=True)
    Reciever_Credit=models.IntegerField(null=True)
    Credit=models.IntegerField(null=True)
    Time=models.DateTimeField(auto_now=True)

    def __str__(self):

        return "Transaction"