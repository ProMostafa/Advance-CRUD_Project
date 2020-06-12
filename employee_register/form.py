from django import forms
from .models import Employee
 # interactive Form to User
class EmployeeForm(forms.ModelForm):

	class Meta:
		model= Employee
		#fields='__all__'
		fields=('fullname','mobile','emp_code','position')
		# chanage the label name of fields
		labels={
			'fullname':'Full Name',
			'emp_code':'EMP. Code'
		}
			# for change ------ from postion field (one to many relations)
	def __init__(self,*args,**kwargs):
		super(EmployeeForm,self).__init__(*args,**kwargs)  # excute super constractor of parant class ModelForm
		# change the properities of fields
		self.fields['position'].empty_label="Select"
		self.fields['emp_code'].required=False