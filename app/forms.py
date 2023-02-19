from django import forms


class StudentForm(forms.Form):
    name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    email=forms.EmailField(max_length=100)
