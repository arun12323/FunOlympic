from django.forms import ModelForm
from .models import *

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control focus'
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control focus'
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control focus'
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['game', 'message']