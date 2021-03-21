from django import forms

class SearchForm(forms.Form):
    zipcode = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': "form-control me-2",
            'type': "search",
            'placeholder': "ZIP Code",
            'aria-label': "Search",
        }
        ),
        required=True,
        
    )

    # def clean_zipcode(self):
    #     data = self.cleaned_data['zipcode']
    #     return data