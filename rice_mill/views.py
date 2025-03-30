from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Page, PageNotAnInteger, Paginator, EmptyPage

from .models import Customer, ItemTypes, Items, Uom, PartyInvoices, PartyInvoiceChild, AddItemsDetails
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CutomerForm, ItemTypesForm, UomForm, ItemsForm, PartyInvoiceForm, PartyInvoiceChildForm, AddItemsDetailsForm

# Create your views here.

def register_view(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration Successfull!!!")
            return redirect("login")
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'authentication/register.html', context)

def login_view(request):
    form = CustomAuthenticationForm()
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home_page")
        else:
            print(form.errors)
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'authentication/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_page_view(request):
    return render(request, "pages/home_page.html")

# Customer start

@login_required(login_url='login')
def ledger_page_view(request):
    customer_list = Customer.objects.all().order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(customer_list, 20)
    try:
        customer_list = paginator.page(page)
    except PageNotAnInteger:
        customer_list = paginator.page(1)
    except EmptyPage:
        customer_list = paginator.page(paginator.num_pages)

    context = {
        'customer_list': customer_list
    }
    return render(request, 'pages/customer/index.html', context)

@login_required(login_url='login')
def customer_creation_view(request):
    form = CutomerForm()
    if request.method == "POST":
        form = CutomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Created Successfully!!!")
            return redirect('ledger')
        else:
            print(form.errors)
    else:
        form = CutomerForm()
    context = {
        'form': form
    }
    return render(request, 'pages/customer/create.html', context)

@login_required(login_url='login')
def customer_update_view(request, pk):
    customer_obj = Customer.objects.get(id=pk)
    form = CutomerForm(instance=customer_obj)
    if request.method == "POST":
        form = CutomerForm(request.POST, instance=customer_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Information Updated Successfully!!!")
            return redirect('ledger')
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'pages/customer/update.html', context)

@login_required(login_url='login')
def customer_delete_view(request, pk):
    customer_obj = get_object_or_404(Customer, id=pk)
    customer_obj.delete()
    messages.success(request, "Customer Deleted Successfully!!!")
    return redirect('ledger')

# Customer end
# Items Type start
@login_required(login_url='login')
def items_types_index_view(request):
    item_types_obj = ItemTypes.objects.all()
    context = {
        'item_types': item_types_obj
    }
    return render(request, 'pages/item_types/index.html', context)

@login_required(login_url='login')
def items_types_create_view(request):
    form = ItemTypesForm()
    if request.method == "POST":
        form = ItemTypesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Items Types Created Successfully!!!")
            return redirect('item_types_index')
        else:
            print(form.errors)
    else:
        form = ItemTypesForm()
    context = {
        'form': form
    }
    return render(request, 'pages/item_types/create.html', context)

@login_required(login_url='login')
def items_types_update_view(request, pk):
    item_types_obj = ItemTypes.objects.get(id=pk)
    form = ItemTypesForm(instance = item_types_obj)
    if request.method == "POST":
        form = ItemTypesForm(request.POST, instance=item_types_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Item Types Updated Successfully!!!")
            return redirect('item_types_index')
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request,'pages/item_types/update.html', context)

@login_required(login_url='login')
def items_types_delete_view(request, pk):
    get_obj = get_object_or_404(ItemTypes, id=pk)
    get_obj.delete()
    messages.success(request, 'Item Types Deleted Successfully!!!')
    return redirect('item_types_index')

# Items Start
@login_required(login_url='login')
def items_index_view(request):
    items_obj = Items.objects.all()
    context = {
        'items': items_obj
    }
    return render(request, 'pages/items/index.html', context)

@login_required(login_url='login')
def items_create_view(request):
    form = ItemsForm()
    if request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Items Created Successfully!!!")
            return redirect('items_index')
        else:
            print(form.errors)
    else:
        form = ItemsForm()
    context = {
        'form': form
    }
    return render(request, 'pages/items/create.html', context)

@login_required(login_url='login')
def items_update_view(request, pk):
    item_obj = Items.objects.get(id=pk)
    form = ItemsForm(instance = item_obj)
    if request.method == "POST":
        form = ItemsForm(request.POST, instance=item_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Item Updated Successfully!!!")
            return redirect('items_index')
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request,'pages/items/update.html', context)

@login_required(login_url='login')
def items_delete_view(request, pk):
    get_obj = get_object_or_404(Items, id=pk)
    get_obj.delete()
    messages.success(request, 'Item Deleted Successfully!!!')
    return redirect('items_index')


# UOM start
@login_required(login_url='login')
def uom_index_view(request):
    uom_obj = Uom.objects.all()
    context = {
        'uom_obj': uom_obj
    }
    return render(request, 'pages/uom/index.html', context)

@login_required(login_url='login')
def uom_create_view(request):
    form = UomForm()
    if request.method == "POST":
        form = UomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "UOM Created Successfully!!!")
            return redirect('uom_index')
        else:
            print(form.errors)
    else:
        form = UomForm()
    context = {
        'form': form
    }
    return render(request, 'pages/uom/create.html', context)

@login_required(login_url='login')
def uom_update_view(request, pk):
    uom_obj = Uom.objects.get(id=pk)
    form = UomForm(instance = uom_obj)
    if request.method == "POST":
        form = UomForm(request.POST, instance=uom_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "UOM Updated Successfully!!!")
            return redirect('uom_index')
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'pages/uom/update.html', context)

@login_required(login_url='login')
def uom_delete_view(request, pk):
    get_obj = get_object_or_404(Uom, id=pk)
    get_obj.delete()
    messages.success(request, 'UOM Deleted Successfully!!!')
    return redirect('uom_index')

# Party invoice start
@login_required(login_url='login')
def party_invoice_index_view(request):
    party_invoice_obj = PartyInvoices.objects.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(party_invoice_obj, 20)
    try:
        party_invoice_obj = paginator.page(page)
    except PageNotAnInteger:
        party_invoice_obj = paginator.page(1)
    except EmptyPage:
        party_invoice_obj = paginator.page(paginator.num_pages)

    context = {
        'party_invoice_obj': party_invoice_obj
    }
    return render(request, 'pages/party_invoice/index.html', context)

@login_required(login_url='login')
def party_invoice_create_view(request):
    form = PartyInvoiceForm()
    if request.method == "POST":
        form = PartyInvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Party Invoice Created Successfully!!!")
            return redirect('party_invoice_index')
        else:
            print(form.errors)
    else:
        form = PartyInvoiceForm()
    context = {
        'form': form
    }
    return render(request, 'pages/party_invoice/create.html', context)

@login_required(login_url='login')
def party_invoice_update_view(request, pk):
    uom_obj = PartyInvoices.objects.get(id=pk)
    form = PartyInvoiceForm(instance = uom_obj)
    if request.method == "POST":
        form = PartyInvoiceForm(request.POST, instance=uom_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Party Invoice Updated Successfully!!!")
            return redirect('party_invoice_index')
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'pages/party_invoice/update.html', context)

@login_required(login_url='login')
def party_invoice_delete_view(request, pk):
    get_obj = get_object_or_404(PartyInvoices, id=pk)
    get_obj.delete()
    messages.success(request, 'Party Invoice Deleted Successfully!!!')
    return redirect('party_invoice_index')


# Party Invoice Child
@login_required(login_url='url')
def party_invoice_child_index_view(request):
    obj_list = PartyInvoiceChild.objects.all()
    return render(request, 'pages/party_invoice_child/index.html', {'obj_list': obj_list})

@login_required(login_url='login')
def party_invoice_child_create_view(request):
    form = PartyInvoiceChildForm()
    if request.method == "POST":
        form = PartyInvoiceChildForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Buying Items Created Successfully!!!")
            return redirect('party_invoice_child_index')
        else:
            messages.error(request, "Invalid form")
    else:
        form = PartyInvoiceChildForm()
    context = {
        'form': form
    }
    return render(request, 'pages/party_invoice_child/create.html', context)

@login_required(login_url='login')
def party_invoice_child_update_view(request, pk):
    party_obj = PartyInvoiceChild.objects.get(id=pk)
    form = PartyInvoiceChildForm(instance = party_obj)
    if request.method == "POST":
        form = PartyInvoiceChildForm(request.POST, instance=party_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Party Invoice Child Updated Successfully!!!")
            return redirect('party_invoice_child_index')
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'pages/party_invoice_child/update.html', context)

@login_required(login_url='login')
def party_invoice_child_delete_view(request, pk):
    get_obj = get_object_or_404(PartyInvoiceChild, id=pk)
    get_obj.delete()
    messages.success(request, 'Party Invoice Child Deleted Successfully!!!')
    return redirect('party_invoice_child_index')


@login_required(login_url='login')
def addItems_details_index_view(request):
    items = AddItemsDetails.objects.all()
    context = {
        'items': items
    }
    return render(request, 'pages/add_Items_details/index.html', context)

@login_required(login_url='login')
def addItems_details_create_view(request):
    form = AddItemsDetailsForm()
    if request.method == "POST":
        form = AddItemsDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Items is Saved Successfully!!")
            return redirect('add_items_details_index')
        else:
            messages.error(request, "Invalid Form!! Please Check The Form")
    else:
        form = AddItemsDetailsForm()
    context = {
        'form': form
    }
    return render(request, 'pages/add_Items_details/create.html', context)

@login_required(login_url='login')
def addItems_details_update_view(request, pk):
    get_obj = AddItemsDetails.objects.get(id=pk)
    form = AddItemsDetailsForm(instance=get_obj)
    if request.method == "POST":
        form = AddItemsDetailsForm(request.POST, instance=get_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Items Details Updated Successfully!!!")
            return redirect("add_items_details_index")
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'pages/add_Items_details/update.html', context)

@login_required(login_url='login')
def addItems_sigle_details_view(request, pk):
    get_obj = AddItemsDetails.objects.get(id=pk)
    context = {
        'get_obj': get_obj
    }
    return render(request, 'pages/add_Items_details/details.html', context)

@login_required(login_url='login')
def addItems_details_delete_view(request, pk):
    get_obj = get_object_or_404(AddItemsDetails, id=pk)
    get_obj.delete()
    messages.success(request, 'Items Deleted Successfully!!!')
    return redirect('add_items_details_index')

@login_required(login_url='login')
def party_invoice_generation_view(request, pk):
    get_data = AddItemsDetails.objects.get(id=pk)
    item_total = get_data.chaul_total + get_data.khud_total + get_data.kura_total + get_data.chita_total
    grand_total = get_data.dhan_total - (get_data.cash_pay + item_total)
    print("tita", item_total)

    context = {
        'get_data': get_data,
        'item_total': item_total,
        'grand_total': grand_total,
    }
    
    return render(request, 'pages/invoice.html', context)