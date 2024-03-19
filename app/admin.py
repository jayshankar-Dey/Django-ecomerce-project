from django.contrib import admin
from .models import cat,product,registers,cart,carts,addaddress,odderss
class CAT(admin.ModelAdmin):
    list_display = ("id","name",)

class PRODUCT(admin.ModelAdmin):
    list_display = ("id","pname","pimg","pdetails","pprice","pdiscount","pcategary","pdelivary_fee",)

class reg(admin.ModelAdmin):
    list_display = ("id","email","password")
class CART(admin.ModelAdmin):
    list_display = ("id","price","user","pname","img")
class CARTS(admin.ModelAdmin):
    list_display = ("id","price","pid","user","pname","img")
class ADDaddress(admin.ModelAdmin):
    list_display = ("id","user","address")

class ODDER(admin.ModelAdmin):
    list_display = ("id","price","pid","user","pname","img","payment","status","order","address")
    search_fields= ("id","price","pid","user","pname","img","payment","status","order","address")

admin.site.register(odderss,ODDER)
admin.site.register(addaddress,ADDaddress)
admin.site.register(carts,CARTS)
admin.site.register(cart,CART)
admin.site.register(registers,reg)
admin.site.register(product,PRODUCT)
admin.site.register(cat,CAT)

# Register your models here.
