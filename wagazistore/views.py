from django.shortcuts import render
import pyodbc
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Product
# Create your views here.





def create(request):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE satisfaction (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_user INT,
                stars INT,
                FOREIGN KEY (id_user) REFERENCES person(id)
            )
        """)
    
    return redirect("index")

def index(request):
    return render(request,"index.html")

from django.db import connection
from django.shortcuts import render, redirect

def registre(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        rpassword = request.POST['password']
        if password!=rpassword:
            return redirect("contact")
        address = request.POST['address']
        telephone = request.POST['telephone']

        with connection.cursor() as cursor:
            # Insert the data into the table
            sql = "INSERT INTO person (name, email, password, address, telephone) VALUES (%s, %s, %s, %s, %s);"
            cursor.execute(sql, (name, email, password, address, telephone))
            
        return redirect('index')
    return render(request,"registre.html")

def about(request):
    return render(request,"about.html")

from .forms import ContactForm,ProductForm

# contact 

def contact(request):
    from django.db import connection
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            with connection.cursor() as cursor:
                cursor.execute("""
                INSERT INTO contact (name, email, message)
                VALUES (%s, %s, %s)
            """, [name, email, message])
            return redirect('index')
        return redirect('contact')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def cart(request):
    return render(request,"cart.html")

def shop(request):
    from django.db import connection
    sql = "SELECT * FROM Person"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        products = cursor.fetchall()

   
    return render(request,"shop.html",{'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, 'create_product.html', {'form': form})


def createtables(request):
    from django.db import connection
    with connection.cursor() as cursor:
         cursor.execute("""
        CREATE TABLE person (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL,
            address VARCHAR(200) NOT NULL,
            telephone VARCHAR(20) NOT NULL
        );
    """)
    return redirect("index")


def voir(request):
    from django.db import connection

# Get all table names in the database
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

# Print the table names
        for table in tables:
          print(table[0])
      
    return redirect('index')


from django.db import connection

def satisfaction(request):
    if request.method == "POST":
        stars = request.POST.get("nbr_stars")
        idclient = request.session.get("id")
        stars = int(stars)
        
        with connection.cursor() as cursor:
            sql = "INSERT INTO satisfaction(id_user, stars) VALUES (%s, %s)"
            values = (idclient, stars)
            cursor.execute(sql, values)
        
        request.session["err_cart"] = "Thanks for your opinion, we will try to improve your shopping"
        return redirect("/cart")
    
    return redirect("login")




def cart(request):

    from django.db import connection
    from datetime import date
    # Check if the user is logged in
    if 'email' in request.session and 'password' in request.session:
        email = request.session['email']
        tel = request.session['tel']
        
        conn = connection
        
        # Handle the POST request to add a product to the cart
        if request.method == "POST":
            quantity = request.POST.get("quantity")
            id_product = request.POST.get("id_product")
            id_client = request.session['id']
            date_today = date.today()
        
            with conn.cursor() as cursor:
                sql = "INSERT INTO cart (id_client, id_product, dateAdd, quantity) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (id_client, id_product, date_today, quantity))
                conn.commit()
            
            # Add product and show the cart
            request.session["err_cart"] = "You added the product successfully."
            return redirect("cart")
        
        # Join the product and the cart by id_product
        with conn.cursor() as cursor:
            sql = "SELECT * FROM cart c JOIN product p ON c.id_product = p.id WHERE c.id_client = %s"
            id_client = request.session['id']
            cursor.execute(sql, (id_client,))
            results = cursor.fetchall()
            
            # Calculate the total price for each product in the cart
            total_sql = "SELECT SUM(p.price * c.quantity) FROM cart c JOIN product p ON c.id_product = p.id WHERE c.id_client = %s"
            cursor.execute(total_sql, (id_client,))
            sum_total = cursor.fetchone()[0]
        
        return render(request, "cart.html", {"buyProduct": results, "total": sum_total, "email": email, "tel": tel})
    
    # If the user is not logged in, redirect to the shop page
    return redirect("shop")



        

