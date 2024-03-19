from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import product,cat,registers,cart,carts,addaddress,odderss
from django.core.paginator import Paginator


def home(request):
    alls = product.objects.all()
    paginator = Paginator(alls,12)
    page_number = request.GET.get('page')
    all =paginator.get_page(page_number)

    producter = product.objects.filter(pcategary= 1)
    paginators = Paginator(producter,4)
    page_numbers = request.GET.get('page')
    products =paginators.get_page(page_numbers)

    produ = product.objects.filter(pcategary= 4)
    pagina = Paginator(produ,8)
    page_numb = request.GET.get('page')
    produc =pagina.get_page(page_numb)

    pro = product.objects.filter(pcategary= 1)
    pagin = Paginator(pro,4)
    page_num = request.GET.get('page')
    prod =pagin.get_page(page_num)

    catagoeies = cat.objects.all()
    
    return render(request,'home.html',{'all':all,'alls':products,'allss':produc,'allsss':prod,'cat':catagoeies})

#show page

def show(request,id):
    shows = product.objects.filter(id=id)
    for x in shows:

      total = product.objects.filter(pcategary=x.pcategary)
    return render(request,'show.html',{'show':shows,'all':total})
def under(request,id):
   all = product.objects.filter(pprice__lte=id)
   return render(request,'under.html',{'all':all})
def category(request,id):
   all = product.objects.filter(pcategary=id)
   return render(request,'categari.html',{'all':all})
#search page////////////////
def search(request):
   search = request.POST.get('search')
   request.session['search'] = search
   if search != "":
      all = product.objects.filter(pname__icontains=search)
      return render(request,'search.html',{'all':all})
   else:
      return redirect('home')
def login(request):
   return render(request,'login.html')
def register(request):
   return render(request,'register.html')
#register hear//////////////////////
def reg(request):
   email = request.POST.get("email")
   password = request.POST.get("password")
   repassword = request.POST.get("repassword")
   if password == repassword and email != "":
      find = registers.objects.filter(email=email)
      if find:
         return redirect("login")
      else:
         registers.objects.create(email=email,password=password)
         return redirect("login")  
   else:
      return redirect("register")
   
#login page/////////////////
def log(request):
   if request.method == "POST":

     email = request.POST.get("email")
     password = request.POST.get("password")

     find = registers.objects.filter(email=email)
     if find:
       for x in find:
         request.session['id'] = x.id
         return redirect("home")
     else:
        return redirect("register")
#cart page///////////////
def cartss(request):
    all = carts.objects.filter(user=request.session.get("id"))
    count = len(all)

    request.session['cart'] = count
    return render(request,"cart.html",{'all':all})
##add to cart........................
def addcart(request):
   price = request.POST.get("price")
   pid = request.POST.get("pid") 
   user = request.POST.get("user") 
   pname = request.POST.get("pname") 
   img = request.POST.get("img")
    
   if user != "":
    find = carts.objects.filter(img=img,user=user)
    if find:
      return redirect("cart")
    else:
      carts.objects.create(price=price,pid=pid,user=user,pname=pname,img=img)
      return redirect("cart")
   else:
      return redirect("login")
   # if find:
   #    return redirect("cart")
   # else:
   #    carts.objects.create(price=price,pid=pid,user=user,pname=pname,img=img)
   #    return redirect("cart")
#delete cart
def delete_cart(request,id):
   carts.objects.filter(id=id).delete() 
   return redirect("cart")  
#order'''''''''''''''
def order(request):
   all = odderss.objects.filter(user=request.session.get("id")).order_by('-id')
   return render(request,'order.html',{'all':all})
#address'''''''''''''''
def address(request):
   all = addaddress.objects.filter(user=request.session.get("id"))
   return render(request,'address.html',{'all':all})

def add_address(request):
   user = request.POST.get("user")
   address = request.POST.get("address")
   addaddress.objects.create(user=user,address=address)
   return redirect("address")
def delete_address(request,id):
   addaddress.objects.filter(id=id).delete()
   return redirect("address")
def edit_address(request,id):
   all = addaddress.objects.filter(id=id)
   return render(request,"edit_address.html",{'all':all})
def edit_save_address(request):
   id = request.POST.get("id")
   user = request.POST.get("user")
   address = request.POST.get("address")
   addaddress.objects.filter(id=id).update(user=user,address=address)
   return redirect("address")

#payment////////////////////
def payment(request):
   price = request.POST.get("price")
   pid = request.POST.get("pid") 
   user = request.POST.get("user") 
   pname = request.POST.get("pname") 
   img = request.POST.get("img")

   request.session['price'] = price
   request.session['pid'] = pid
   request.session['user'] = user
   request.session['pname'] = pname
   request.session['img'] = img
   all = addaddress.objects.filter(user=request.session.get("id"))
   return render(request,"payment.html",{'all':all})
def user_order(request):
   price = request.POST.get("price")
   pid = request.POST.get("pid") 
   user = request.POST.get("user") 
   pname = request.POST.get("pname") 
   img = request.POST.get("img")
   payment = request.POST.get("payment")
   address = request.POST.get("address")
   if payment and address:
     odderss.objects.create(price=price,pid=pid,user=user,pname=pname,img=img,payment=payment,address=address)
     return redirect("order")
   else:
      return redirect("home")
def show_order(request,id):
   all = odderss.objects.filter(id=id)
   return render(request,"show_order.html",{'all':all})
#conferm cencelle//////////////////
def conferm(request,id):
   return render(request,"conferm.html",{'id':id})    
#save conferm//////////////
def save_conferm(request):
   id = request.POST.get("id")
   odderss.objects.filter(id=id).update(order="cancelled")

   return redirect("order")