from django import forms
from .models import Course

class CreateForm(forms.ModelForm):
    title = forms.CharField(error_messages = {'required':'Please enter title'}, label="Course Name", max_length=100, widget=forms.TextInput(attrs={'placeholder':'Title','size': 40, "class": "form-control"}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Description','size': 40, "class": "form-control"}))
    imageUrl = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'imageUrl','size': 40,  "class": "form-control"}))
    date = forms.CharField(required=False, widget=forms.SelectDateWidget(attrs={'placeholder':'Date', "class": "form-control"}))
    isActive = forms.CharField(required=False, widget=forms.CheckboxInput)

    class Meta:
        model = Course
        fields = '__all__'



    #title = forms.CharField(error_messages = {'required':'Please enter title'}, label="Course Name", max_length=100, widget=forms.TextInput(attrs={'placeholder':'Title','size': 40, 'style':'width:20%;', 'cols':50,'rows':20,"class": "form-control"}))
    #description = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Description','size': 40, 'style':'width:30%;', 'cols':50,'rows':20, "class": "form-control"}))
    #imageUrl = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'imageUrl','size': 40, 'style':'width:40%;', 'cols':50,'rows':20, "class": "form-control"}))
    #date = forms.CharField(required=False, widget=forms.SelectDateWidget(attrs={'placeholder':'Date', 'cols':50,'rows':20, "class": "form-control"}))
