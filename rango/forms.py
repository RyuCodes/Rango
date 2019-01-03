from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    # setting the field without giving control to the user, but the form will
    # still provide the value to the model
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        #Provides association between ModelForm and Model
        model = Category
        #must provide fields in Meta otherwise exception will occur
        fields = ('name', 'views', 'likes')

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        # cleaned_data is a dict, so .get will search for a key:value pair, where
        # 'url' is the key
        # .get is better because will return None instead of KeyError if key does not exist
        url = cleaned_data.get('url')

        #if url is not empty and doesn't start with 'http://', add 'http://'
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Page
        #can choose to only include some fields in the form
        #foreign key is not a field
        fields = ('title', 'url', 'views')

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username")
    email = forms.CharField(help_text="Please enter an email")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Please enter your website", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload", required=False)

    class Meta:
        model = UserProfile
        #by Default django renders all fields within associated Model unless specified
        fields = ['website', 'picture']
