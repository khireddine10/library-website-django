from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrower)
admin.site.register(Memoire)

