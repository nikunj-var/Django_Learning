from django import forms

class FeedbackForm(forms.Form):
    title  = forms.CharField(label = 'Title',max_length=54,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label= "Subject Description",max_length=255,widget=forms.Textarea(attrs={'class':'form-control'}))
    email  = forms.CharField(label = 'Email',max_length=54,widget=forms.TextInput(attrs={'class':'form-control'}))