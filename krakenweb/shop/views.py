
from sqlite3.dbapi2 import OperationalError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import sqlite3
import logging

con=sqlite3.connect('/var/www/html/kraken/db.sqlite3',check_same_thread=False)
# Create your views here.

class Item:
    def __init__(self,id,title,price,image):
        self.id=id
        self.title=title
        self.price=price
        self.image=image



def resulttomodel(result):
    return Item(result[0],result[1],result[2],result[3])

def home(request):
    cursor=con.cursor()
    search_param=request.GET.get('search')
    if(search_param!=None):
        try:
            cursor.execute(f"Select id,title,prize,image from shop_items where title like '{search_param}%'")
        except OperationalError:
            logging.error(f"There is an operation error")
            
    else:   
        cursor.execute("Select * from shop_items")
    context={
        "items":map(resulttomodel,cursor.fetchall())
    }
    
    return render(request,template_name='index.html',context=context)

def product_page(request):
    if(request.method=="GET"):
        title=request.GET.get("title")
        cursor=con.cursor()
        cursor.execute(f"select * from shop_items where shop_items.title='{title}' LIMIT 1")
        context={
            "item":resulttomodel(cursor.fetchall()[0])
        }
        return render(request,template_name='single.html',context=context)

    
