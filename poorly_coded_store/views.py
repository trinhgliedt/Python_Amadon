from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def display_order(request, order_id):
    all_orders = Order.objects.all()
    all_orders_price = 0
    for order in all_orders:
        all_orders_price += order.total_price
    context = {
        "this_order": Order.objects.get(id=order_id),
        "all_orders": Order.objects.all(),
        "all_orders_price": all_orders_price,
    }
    return render(request, "store/checkout.html", context)

def process_order(request):
    if request.method == "POST":
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = Product.objects.get(id=int(request.POST["id"])).price
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        this_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

        this_order_id = this_order.id

        return redirect(f"/order-summary/{this_order_id}")
    else: 
        return redirect("/")