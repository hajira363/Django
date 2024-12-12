from django.shortcuts import render,redirect

# Create your views here.


products = [
    {
        "name": "Smartphone",
        "category": "Electronics",
        "description": "A high-end mobile device with advanced features like a touchscreen and powerful cameras.",
        "image": "images/Smartphone.jfif",
        "price": 29999
    },
    {
        "name": "Portable Speaker",
        "category": "Audio",
        "description": "A Bluetooth-enabled, wireless speaker for playing music on the go.",
        "image": "images/portableSpeaker.jfif",
        "price": 1299
    },
    {
        "name": "Electric Toothbrush",
        "category": "Health & Beauty",
        "description": "A toothbrush that uses oscillating or vibrating technology to clean teeth more effectively.",
        "image": "images/Electric toothbresh.jfif",
        "price": 1049  
    },
    {
        "name": "Fitness Tracker",
        "category": "Wearables",
        "description": "A wearable device that monitors physical activity, heart rate, and other health metrics.",
        "image": "images/Fitness Tracker.jfif",
        "price": 1499
    },
    {
        "name": "Wireless Headphones",
        "category": "Audio",
        "description": "Bluetooth-enabled headphones offering a cord-free listening experience.",
        "image": "images/Wireless Headphones.png",
        "price": 899
    },
    {
        "name": "Coffee Maker",
        "category": "Home Appliances",
        "description": "A kitchen appliance for brewing coffee, often with programmable settings for convenience.",
        "image": "images/Coffee Maker.jfif",
        "price": 9299
    },
    {
        "name": "Laptop",
        "category": "Electronics",
        "description": "A portable computer designed for work, study, or entertainment, with various performance levels.",
        "image": "images/Laptop.jfif ",
        "price": 47690
    },
    {
        "name": "Air Fryer",
        "category": "Home Appliances",
        "description": "A kitchen appliance that cooks food using hot air for a crispy texture without deep frying.",
        "image": "images/Air Fryer.jfif",
        "price": 3099
    },
    {
        "name": "Electric Kettle",
        "category": "Home Appliances",
        "description": "A device for quickly boiling water, often with an automatic shut-off feature.",
        "image": "images/Electric Kettle.jfif",
        "price": 699
    },
    {
        "name": "Smartwatch",
        "category": "Wearables",
        "description": "A wearable device that pairs with a smartphone for notifications, fitness tracking, and more.",
        "image": "images/Smartwatch.jfif",
        "price": 2500
    }
    ]

cart=[]

def home(request):
    

    return render(request,'productlist/home.html',{"products":products})

def login(request):
    return render(request,'productlist/login.html')

def register(request):
    return render(request,'productlist/register.html')

def single(request,index):

    product=products[index]

    if request.method == 'POST':
        quantity=request.POST.get('quantity')
        if quantity=="" :
            quantity=1
            
        cart_item={
            "product_index":index,
            "quantity":quantity,
            "price":product['price'],
            "image":product['image'],
            "name":product['name'],
            "subTotal":int(product['price'])* int(quantity)

        }
        cart.append(cart_item)
        return redirect('cart')
    
        

    return render(request,"productlist/sing_page.html",{'product':product})

def addtocart(request):
    Totalprice=0
    for item in cart:
        Totalprice+=item['subTotal']

    return render(request,'productlist/addcart.html',{'cart':cart,'toalprice':Totalprice})

