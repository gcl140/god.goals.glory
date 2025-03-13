# forms.py
from django import forms
from .models import Product, Review, Rating, Testimonial, WaitlistUser, WaitlistEmailTemplate


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'status', 'quantity', 'image', 'image_2', 'image_3', 'image_4']

class PraiseForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['user', 'caption', 'product', 'image', 'image_2', 'image_3', 'image_4']
        
class OrderForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please enter your address'}))
    payment_method = forms.ChoiceField(choices=[('cash', 'Cash')])

class WaitlistSignupForm(forms.ModelForm):
    class Meta:
        model = WaitlistUser
        fields = ['first_name', 'last_name', 'email', 'tel1']

# class EmailTemplateForm(forms.ModelForm):
#     class Meta:
#         model = WaitlistEmailTemplate
#         fields = ['subject', 'content', 'attachment']

class EmailTemplateForm(forms.ModelForm):
    class Meta:
        model = WaitlistEmailTemplate
        fields = ['subject', 'content', 'attachment']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Email content...'}),
        }



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment...', 'class': 'form-control'}),
        }

class RatingForm(forms.ModelForm):
    stars = forms.ChoiceField(choices=[(i, f"{i} Stars") for i in range(1, 6)], widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Rating
        fields = ['stars']
