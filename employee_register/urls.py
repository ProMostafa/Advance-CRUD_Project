from django.urls import path 
from .import views
urlpatterns = [
# when route by http://127.0.0.1:8000/employee excute fun employee_form 
# HomePage Of employee_register app ,''is empty becuase is define in urls project level 
    path('', views.employee_form,name='employee_insert'),# Get and Post req for insert operations
    path('<int:id>/', views.employee_form,name='employee_update'), # Get and Post req for update operation
    path('delete<int:id>/', views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list')  # Get req to retrieve and display all records
      # when route by http://127.0.0.1:8000/employee/list excute fun employee_list

      # Get request : retrieve data from DataBase
      #Post request : Update or Saving Data In DataBase
]
