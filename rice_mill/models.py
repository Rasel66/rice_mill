from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, related_name="branch_name", blank=True, null=True)
    is_superuser = models.BooleanField(default=False)

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_name_bn = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.customer_name
    
class ItemTypes(models.Model):
    item_type_name = models.CharField(max_length=250)
    item_type_id = models.IntegerField()
    item_type_name_bn = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.item_type_name

class Uom(models.Model):
    uom_name = models.CharField(max_length=250)
    uom_name_bn = models.CharField(max_length=250, blank=True, null=True)
    relative_factor = models.FloatField()

    def __str__(self):
        return self.uom_name


class Items(models.Model):
    item_types = models.ForeignKey(ItemTypes, on_delete=models.PROTECT, related_name="items_itemtypes")
    item_name = models.CharField(max_length=250)
    item_name_bn = models.CharField(max_length=250, blank=True, null=True)
    uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name='items_uom')
    item_description = models.TextField(blank=True, null=True)
    sequence_no = models.FloatField()
    charge = models.FloatField()
    remarks = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.item_name

class PartyInvoices(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='party_invoice_customer')
    items = models.ForeignKey(Items, on_delete=models.PROTECT, related_name='party_invoice_items')
    uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name='party_invoice_uom')
    qty = models.FloatField()
    unit_price = models.FloatField()
    total_price = models.FloatField(blank=True, null=True)
    charges = models.FloatField(blank=True, null=True)
    prev_balance = models.FloatField(blank=True, null=True)
    cash_pay = models.FloatField(blank=True, null=True)
    grand_total_balance = models.FloatField(blank=True, null=True)
    current_due = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    base_unit_qty = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.customer.customer_name

    def save(self, *args, **kwargs):
        self.total_price = self.qty * self.charges
        super().save(*args, **kwargs)


class PartyInvoiceChild(models.Model):
    party_invoice = models.ForeignKey(PartyInvoices, on_delete=models.PROTECT, related_name='party_invoice_child_party_invoice')
    items = models.ForeignKey(ItemTypes, on_delete=models.PROTECT, related_name='party_invoice_chaild_items')
    uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name='party_invoice_chaild_uom')
    unit_price = models.FloatField()
    qty = models.FloatField()
    charges = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.charges = self.qty * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.party_invoice


class AddItemsDetails(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='addItemDetails_customer')
    date = models.DateTimeField()
    cash_pay = models.FloatField(blank=True, null=True)
    dhan_uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name="additems_uom_dhan")
    dhan_qty = models.FloatField()
    dhan_unit_price = models.FloatField()
    dhan_total = models.FloatField(blank=True, null=True)
    chaul_uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name="additems_uom_chaul")
    chaul_qty = models.FloatField(blank=True, null=True)
    chaul_unit_price = models.FloatField(blank=True, null=True)
    chaul_total = models.FloatField(blank=True, null=True)
    khud_uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name="additems_uom_khud")
    khud_qty = models.FloatField(blank=True, null=True)
    khud_unit_price = models.FloatField(blank=True, null=True)
    khud_total = models.FloatField(blank=True, null=True)
    kura_uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name="additems_uom_kura")
    kura_qty = models.FloatField(blank=True, null=True)
    kura_unit_price = models.FloatField(blank=True, null=True)
    kura_total = models.FloatField(blank=True, null=True)
    chita_uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name="additems_uom_chita")
    chita_qty = models.FloatField(blank=True, null=True)
    chita_unit_price = models.FloatField(blank=True, null=True)
    chita_total = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        if self.dhan_uom.uom_name == "MON":
            self.dhan_total = self.dhan_qty * self.dhan_unit_price
        elif self.dhan_uom.uom_name == "KG":
            self.dhan_total = (self.dhan_qty / 40) * self.dhan_unit_price
        else:
            self.dhan_total = 0

        if self.chaul_uom.uom_name == "MON":
            self.chaul_total = self.chaul_qty * self.chaul_unit_price
        elif self.chaul_uom.uom_name == "KG":
            self.chaul_total = (self.chaul_qty / 40) * self.chaul_unit_price
        else:
            self.chaul_total = 0

        if self.khud_uom.uom_name == "MON":
            self.khud_total = self.khud_qty * self.khud_unit_price
        elif self.khud_uom.uom_name == "KG":
            self.khud_total = (self.khud_qty / 40) * self.khud_unit_price
        else:
            self.khud_total = 0

        if self.kura_uom.uom_name == "MON":
            self.kura_total = self.kura_qty * self.kura_unit_price
        elif self.kura_uom.uom_name == "KG":
            self.kura_total = (self.kura_qty / 40) * self.kura_unit_price
        else:
            self.kura_total = 0

        if self.chita_uom.uom_name == "MON":
            self.chita_total = self.chita_qty * self.chita_unit_price
        elif self.chita_uom.uom_name == "KG":
            self.chita_total = (self.chita_qty / 40) * self.chita_unit_price
        else:
            self.chita_total = 0
        super().save(*args, **kwargs)

        if is_new:
            from .models import Stocks
            stock, created  = Stocks.objects.get_or_create(id=1)
            
            stock.chaul_qty = (stock.chaul_qty or 0) + (self.chaul_qty or 0)
            stock.khud_qty = (stock.khud_qty or 0) + (self.khud_qty or 0)
            stock.kura_qty = (stock.kura_qty or 0) + (self.kura_qty or 0)
            stock.chita_qty = (stock.chita_qty or 0) + (self.chita_qty or 0)

            stock.save()
        
    def delete(self, *args, **kwargs):
        from .models import Stocks
        stock = Stocks.objects.first()

        if stock:
            stock.chaul_qty = (stock.chaul_qty or 0) - (self.chaul_qty or 0)
            stock.khud_qty = (stock.khud_qty or 0) - (self.khud_qty or 0)
            stock.kura_qty = (stock.kura_qty or 0) - (self.kura_qty or 0)
            stock.chita_qty = (stock.chita_qty or 0) - (self.chita_qty or 0)

            stock.save()

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.customer.customer_name
    

class SellCustomers(models.Model):
    customer_name = models.CharField(max_length=250)
    customer_name_bn = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.customer_name

class Stocks(models.Model):
    chaul_qty = models.FloatField(blank=True, null=True)
    khud_qty = models.FloatField(blank=True, null=True)
    kura_qty = models.FloatField(blank=True, null=True)
    chita_qty = models.FloatField(blank=True, null=True)

class SellsInvoices(models.Model):
    customer = models.ForeignKey(SellCustomers, on_delete=models.PROTECT)
    advance_amount = models.FloatField(blank=True, null=True)
    total_bill_amount = models.FloatField(blank=True, null=True)
    cash_pay = models.FloatField()
    balance = models.FloatField(blank=True, null=True)
    prev_due = models.FloatField(blank=True, null=True)
    current_due = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    chaul_uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name="chaul_invoices")
    chaul_qty = models.FloatField(blank=True, null=True)
    chaul_unit_price = models.FloatField(blank=True, null=True)
    chaul_total = models.FloatField(blank=True, null=True)
    khud_uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name="khud_invoices")
    khud_qty = models.FloatField(blank=True, null=True)
    khud_unit_price = models.FloatField(blank=True, null=True)
    khud_total = models.FloatField(blank=True, null=True)
    kura_uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name="kura_invoices")
    kura_qty = models.FloatField(blank=True, null=True)
    kura_unit_price = models.FloatField(blank=True, null=True)
    kura_total = models.FloatField(blank=True, null=True)
    chita_uom = models.ForeignKey(Uom, on_delete=models.PROTECT, related_name="chita_invoices")
    chita_qty = models.FloatField(blank=True, null=True)
    chita_unit_price = models.FloatField(blank=True, null=True)
    chita_total = models.FloatField(blank=True, null=True)
    date = models.DateField()

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        if self.chaul_uom.uom_name == "MON":
            self.chaul_total = self.chaul_qty * self.chaul_unit_price
        elif self.chaul_uom.uom_name == "KG":
            self.chaul_total = (self.chaul_qty / 40) * self.chaul_unit_price
        else:
            self.chaul_total = 0

        if self.khud_uom.uom_name == "MON":
            self.khud_total = self.khud_qty * self.khud_unit_price
        elif self.khud_uom.uom_name == "KG":
            self.khud_total = (self.khud_qty / 40) * self.khud_unit_price
        else:
            self.khud_total = 0

        if self.kura_uom.uom_name == "MON":
            self.kura_total = self.kura_qty * self.kura_unit_price
        elif self.kura_uom.uom_name == "KG":
            self.kura_total = (self.kura_qty / 40) * self.kura_unit_price
        else:
            self.kura_total = 0

        if self.chita_uom.uom_name == "MON":
            self.chita_total = self.chita_qty * self.chita_unit_price
        elif self.chita_uom.uom_name == "KG":
            self.chita_total = (self.chita_qty / 40) * self.chita_unit_price
        else:
            self.chita_total = 0
        super().save(*args, **kwargs)

        if is_new:
            from .models import Stocks
            stock = Stocks.objects.first()
            if stock:
                stock.chaul_qty = (stock.chaul_qty or 0) - (self.chaul_qty or 0)
                stock.khud_qty = (stock.khud_qty or 0) - (self.khud_qty or 0)
                stock.kura_qty = (stock.kura_qty or 0) - (self.kura_qty or 0)
                stock.chita_qty = (stock.chita_qty or 0) - (self.chita_qty or 0)

                stock.save()

    def delete(self, *args, **kwargs):
        from .models import Stocks
        stock = Stocks.objects.first()

        if stock:
            stock.chaul_qty = (stock.chaul_qty or 0) + (self.chaul_qty or 0)
            stock.khud_qty = (stock.khud_qty or 0) + (self.khud_qty or 0)
            stock.kura_qty = (stock.kura_qty or 0) + (self.kura_qty or 0)
            stock.chita_qty = (stock.chita_qty or 0) + (self.chita_qty or 0)

            stock.save()

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.customer.customer_name


