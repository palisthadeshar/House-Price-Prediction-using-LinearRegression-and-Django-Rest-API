from django import forms

class PredictForm(forms.Form):
    area=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter number of areas'}))
    bedrooms=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter number of bedrooms'}))
    bathrooms=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter number of bathrooms'}))
    stories=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter number of stories'}))
    mainroad=forms.ChoiceField(choices=[('yes','yes'),('no','no')])
    guestroom=forms.ChoiceField(choices=[('yes','yes'),('no','no')])
    basement=forms.ChoiceField(choices=[('yes','yes'),('no','no')])
    hotwaterheating=forms.ChoiceField(choices=[('yes','yes'),('no','no')])
    airconditioning=forms.ChoiceField(choices=[('yes','yes'),('no','no')])
    parking=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter number of parking'}))
    prefarea=forms.ChoiceField(choices=[('yes','yes'),('no','no')])
    furnished=forms.ChoiceField(choices=[('semi_furnished','semi_furnished'),('unfurnished','unfurnished')])