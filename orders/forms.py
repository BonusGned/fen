from django import forms
from django.contrib.auth.models import User

from shop.models import Order


class OrderForm(forms.ModelForm):

    def __inti__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date'].lbael = 'Date of receipt of order'

    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        )
