from django import forms

class MainForm1(forms.Form):

   code = forms.CharField(required=False ,
                                widget=forms.Textarea(
                                   attrs={
                                      "class":"new-class-name two",
                                      "rows":30,
                                      "cols":90
                                   }

   ))
