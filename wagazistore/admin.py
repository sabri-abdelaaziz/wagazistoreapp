from django.contrib import admin
from django.db import connection
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM contact")
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()
        return [dict(zip(columns, row)) for row in data]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Contact,ContactAdmin)



from django.contrib import admin
from django.db import connection
from .models import Product, Person

class ProductAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM product")
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()
        return [dict(zip(columns, row)) for row in data]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Product, ProductAdmin)


class PersonAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM person")
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()
        return [dict(zip(columns, row)) for row in data]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Person, ProductAdmin)
