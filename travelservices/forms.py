from django import forms
from travelservices.models import Travelservices
class TravelservicesForm(forms.ModelForm):
    class Meta:
        model = Travelservices
        fields = "__all__"