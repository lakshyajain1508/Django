## Form Add & View

1. **Step 1 - Register your app in setting.py in your project**
    ```bash
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "AppName", // example - Myapp
    ]
    ```

2. **Step 2 - In your app go to the models.py file and mnake a class of employee**
    ```bash
    from django.db import models

    class Employee(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        email = models.EmailField()
        phone_number = models.CharField(max_length=15)
    ```
    **Now go to the admin.py file and register your amployee model**

    ```bash
    from django.contrib import admin
    from .models import Employee

    admin.site.register(Employee)
    ```

3. **Step 3 - make a new file name as forms.py inside your app and add this code.**
    ```bash
    from django import forms
    from .models import Employee

    class EmployeeForm(forms.ModelForm):
        class Meta:
            model = Employee
            fields = ['first_name', 'last_name', 'email', 'phone_number']
    ```

4. **Step 4 - Now create a view in your app file views.py**
    ```bash
    from django.shortcuts import render
    from .forms import EmployeeForm
    from .models import Employee 

    def employee_form(request):
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                # Redirect to a success page or do something else
        else:
            form = EmployeeForm()
        return render(request, 'employee_form.html', {'form': form})

    def employee_list(request):
        employees = Employee.objects.all()
        return render(request, 'employee_list.html', {'employees': employees})
    ```

5. **Step 5 - Create a folder templates in app & make a file employee_form.html**

```bash

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Employee Form</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <!-- Optional Bootstrap theme -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap-theme.min.css">
    <style>
        /* Custom CSS for adjusting label width */
        .form-group label {
            width: 150px; /* Adjust as needed */
            text-align: right;
            margin-bottom: 0;
            padding-right: 10px;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <div class="card">
                    <div class="card-header bg-primary text-white">
                        <h1 class="text-center">Employee Form</h1>
                    </div>
                    <div class="card-body">
                        <form method="post">
                            {% csrf_token %}
                            <div class="form-group row">
                                <label for="id_first_name" class="col-sm-4 col-form-label">First Name:</label>
                                <div class="col-sm-8">
                                    {{ form.first_name }}
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="id_last_name" class="col-sm-4 col-form-label">Last Name:</label>
                                <div class="col-sm-8">
                                    {{ form.last_name }}
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="id_email" class="col-sm-4 col-form-label">Email:</label>
                                <div class="col-sm-8">
                                    {{ form.email }}
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="id_phone_number" class="col-sm-4 col-form-label">Phone Number:</label>
                                <div class="col-sm-8">
                                    {{ form.phone_number }}
                                </div>
                            </div>
                            <div class="form-group row">
                                <div class="col-sm-12">
                                    <button type="submit" class="btn btn-primary btn-block">Submit</button>
                                </div>
                            </div>
                        </form>
                        <br>
                        <a href="{% url 'employee_list' %}"><button>View Employee Data</button></a>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <!-- Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

```

6. **Step 6 - Make oner more file name as employee_list.html**

```bash

    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Employee List</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            padding-top: 5rem;
            background-color: #f4f4f4;
        }
        footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            height: 3rem;
            line-height: 3rem;
            background-color: #f8f9fa;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
        <a class="navbar-brand" href="#">Employee List</a>
    </nav>

    <div class="container mt-5">
        <a href="{% url 'employee_form' %}"><button>Add New Employee</button></a>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Phone Number</th>
                </tr>
            </thead>
            <tbody>
                {% for employee in employees %}
                    <tr>
                        <td>{{ employee.first_name }}</td>
                        <td>{{ employee.last_name }}</td>
                        <td>{{ employee.email }}</td>
                        <td>{{ employee.phone_number }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>


    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

7. **Step 7 - Make urls.py in app**

    ```bash

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.employee_form, name='employee_form'),
        path('list/', views.employee_list, name='employee_list'),
    ]

    ```

8. **Step 8 - In your project there is one urls.py file add this code**
    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('data/', include('Myapp.urls')),
    ]
    ```

9. **Step 9 - Run migrations to apply the model changes to the database :**

    ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```

10. **Step 10 - Run the server**

    ```bash
    python manage.py runserver
    ```
    **Open a web browser and go to http://127.0.0.1:8000/admin.**<br>
    **Log in with the superuser credentials you created earlier.**<br>
    **You should now see the Django admin interface.**<br>
    **Navigate to the “Employees” section to manage employee records.**<br>
    **That’s it! You’ve added the admin interface, created a superuser, and started the development server for your Django project. You can now manage employee records through the admin interface and access the employee form at http://127.0.0.1:8000/data/.**<br>
    **Display employee data. You can access it at http://127.0.0.1:8000/list/. This view will list all employees stored in the database.**