from django import forms
from .models import ToDoItem
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class ToDoItemForm(forms.ModelForm):
    is_done = forms.BooleanField(required=False)
    class Meta:
        model = ToDoItem
        fields = ['todo_list', 'title', 'description', 'due_date']

        widgets = {
            'due_date': DateTimePickerInput(attrs={'class': 'post-form'}, options={
                "format": "YYYY-MM-DD",
                "showClose": True,
                "showClear": True,
                "showTodayButton": True,
            }),
            'is_done' : forms.CheckboxInput(attrs={'class': 'required checkbox form-control'}),
        }