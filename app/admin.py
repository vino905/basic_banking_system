from django.contrib import admin
from app.models import Person,Transaction_history
# Register your models here.
admin.site.register(Person)
admin.site.register(Transaction_history)