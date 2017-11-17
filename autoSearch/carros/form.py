from django import forms

from .models import Car

class CarModelForm(forms.ModelForm):
    content = forms.CharField(label='',
                              widget=forms.TextInput(
                                        attrs={'placeholder':"Car",
                                               'class': "input"  }
                              ))

    class Meta:
        model = Car
        fields = [
            "ttype",
            "year",
            "colour",
            "price"
        ]
