import bootstrap_datepicker_plus as datetimepicker
from django import forms

from .models import LeaveTable, LeaveType

class LeaveForm(forms.ModelForm):

    class Meta:
        model = LeaveTable
        fields = ('date', 'ltype', 'text')
        widgets = {
            'date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }
