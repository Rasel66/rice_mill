from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser, Customer, ItemTypes, Items, Uom, PartyInvoices, PartyInvoiceChild, AddItemsDetails

# Authentication form start

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'branch']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username")

class CutomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'customer_name': "Customer Name",
            'customer_name_bn': "Customer Name Bangla",
        }

class ItemTypesForm(forms.ModelForm):
    class Meta:
        model = ItemTypes
        fields = '__all__'
        labels = {
            'item_type_name': "Item Types Name",
            'item_type_name_bn': "Item Types Name Bangla",
            'item_type_id': "Item Types ID"
        }

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'
        labels = {
            'item_types': "Item Types",
            'item_name': "Item Name",
            'item_name_bn': "Item Name Bangla",
            'uom': "UOM",
            'item_description': "Description",
            'sequence_no': "Sequence No"
        }
        widgets = {
            'item_description': forms.Textarea(attrs={'rows': 2, 'cols': 40})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_types'].empty_label = "--SELECT--"
        self.fields['uom'].empty_label = "--SELECT--"

class UomForm(forms.ModelForm):
    class Meta:
        model = Uom
        fields = '__all__'
        labels = {
            'uom_name': "UOM Name",
            'uom_name_bn': "UOM Name Bangla",
            'relative_factor': "Relative Factor"
        }

class PartyInvoiceForm(forms.ModelForm):
    class Meta:
        model = PartyInvoices
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].empty_label = "--SELECT--"
        self.fields['items'].empty_label = "--SELECT--"
        self.fields['uom'].empty_label = "--SELECT--"

class PartyInvoiceChildForm(forms.ModelForm):
    class Meta:
        model = PartyInvoiceChild
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['party_invoice'].empty_label = "--SELECT--"
        self.fields['items'].empty_label = "--SELECT--"
        self.fields['uom'].empty_label = "--SELECT--"


class AddItemsDetailsForm(forms.ModelForm):
    phone_no = forms.CharField(disabled=True, label="Phone No", required=False)
    address = forms.CharField(disabled=True, label="Address", required=False)
    class Meta:
        model = AddItemsDetails
        fields = '__all__'
        labels = {
            'dhan_uom': "UOM",
            'dhan_qty': "Quantity",
            'dhan_unit_price': "Unit Price",
            'khud_uom': "UOM",
            'khud_qty': "Quantity",
            'khud_unit_price': "Unit Price",
            'kura_uom': "UOM",
            'kura_qty': "Quantity",
            'kura_unit_price': "Unit Price",
            'chaul_uom': "UOM",
            'chaul_qty': "Quantity",
            'chaul_unit_price': "Unit Price",
            'chita_uom': "UOM",
            'chita_qty': "Quantity",
            'chita_unit_price': "Unit Price",
        }
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dhan_uom'].empty_label = "--SELECT--"
        self.fields['chaul_uom'].empty_label = "--SELECT--"
        self.fields['kura_uom'].empty_label = "--SELECT--"
        self.fields['chita_uom'].empty_label = "--SELECT--"
        self.fields['khud_uom'].empty_label = "--SELECT--"
        self.fields['customer'].empty_label = "--SELECT--"
