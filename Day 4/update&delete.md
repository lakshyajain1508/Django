## Create, Retrieve, Update, and Delete

1.  **Step 1 - Register your app in your project in `setting.py` file**
    ```bash
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "contact_app",  // Changes is here.
    ]
    ```
2.  **Step 2 - Create a templates folder in app than make three files in folder**
    **`dashboard.html`**
    **`index.html`**
    **`edit.html`**

3.  **Step 3 - Go to the `models.py` file\*and make a class a class**

    ```bash
    class Msg(models.Model):
        name = models.CharField(max_length=100)
        email = models.CharField(max_length=100)
        mobile= models.BigIntegerField()
        msg = models.TextField()
    ```

4.  **Step 4 - Migrate the files using terimal**

    ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```

5.  **Step 5 - Go to the `views.py` in your app and connect with templates files.**

    ```bash
    from django.shortcuts import render , redirect
    from django.http import HttpResponse
    from .models import Msg

    def create (request):
        if(request.method == "GET"):
            return render(request,"index.html")
        else:
            username = request.POST["uname"]
            contact = request.POST["mobile"]
            email = request.POST["uemail"]
            msg = request.POST["msg"]

            m = Msg.objects.create(name=username,email=email,mobile=contact,msg=msg)
            m.save()

            return render(request,"index.html")

    def dashboard(request):
        context = {}
        m = Msg.objects.all() # Fetch all data
        context['data'] = m
        #print(m)

        return render(request,"dashboard.html",context)

    def edit(request,sid):
        if request.method == "GET":
            m = Msg.objects.filter(id = sid)
            context = {}
            context['data'] = m
            return render(request,"edit.html",context)
        else :
            username = request.POST["uname"]
            contact = request.POST["mobile"]
            email = request.POST["uemail"]
            msg = request.POST["msg"]

            m = Msg.objects.filter(id = sid).update(name=username,email=email,mobile = contact , msg = msg)
            return redirect("/")

    def delete(request,did):
        m = Msg.objects.filter(id=did)
        m.delete()
        return redirect("/")
    ```

6.  **Step 6 - Go the `dashboard.html` file in you templates folder.**

    ````bash
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <title>Lakshya Jain</title>
    </head>
    <body>

        <nav class="navbar navbar-expand-lg bg-warning">
            <div class="container-fluid">
              <a class="navbar-brand" href="https://github.com/lakshyajain1508">Lakshya Jain</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                  <li class="nav-item">
                    <a class="btn btn-primary" aria-current="page" href="{% url 'create' %}">Add Data</a>
                  </li>

                </ul>
              </div>
            </div>
          </nav>



          <div class="container mt-5">
                <div class="row">
                    <div class="col">
                        <table class="table table-bordered border-primary">
                            <thead class="table-warning">
                                <tr>
                                    <th>Sr. No.</th>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Mobile</th>
                                    <th>Message</th>
                                    <th>Edit</th>
                                    <th>Delete</th>
                                </tr>
                            </thead>


                            {% for d in data %}
                            <tr>
                                <td>{{ forloop.counter }}</td>
                                <td>{{ d.name }}</td>
                                <td>{{ d.email }}</td>
                                <td>{{ d.mobile }}</td>
                                <td>{{ d.msg }}</td>
                                <td><a href="/edit/{{d.id}}"><i class="bi bi-pencil-square"></i></a></td>
                                <td><a href="/delete/{{d.id}}"><i class="bi bi-trash"></i></a></td>
                            </tr>
                            {% endfor %}
                        </table>
                    </div>
                </div>
          </div>




        </body>
        </html>
    ```

7.  **Step 7 - Go the `edit.html` file in you templates folder.**

    ```bash
    <!DOCTYPE html>

    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lakahya Jain</title>
       
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        
        </head>
        <body>
        
            <nav class="navbar navbar-expand-lg bg-warning">
                <div class="container-fluid">
                  <a class="navbar-brand" href="https://github.com/lakshyajain1508">Lakshya Jain</a>
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                      <li class="nav-item">
                        <a class="btn btn-primary" aria-current="page" href="{% url 'dashboard' %}">Dashboard</a>
                      </li>
                 
                    </ul>
                  </div>
                </div>
            </nav>
        
            <div class="container mt-5">
                <div class="row justify-content-center">
                    <div class="col-sm-6 ">
                        <h1>Update Data</h1>

                        <form action="" method="POST">
                            {% csrf_token %}

                            <label class="form-label">Enter name</label>
                            <br>
                            <input type="text" class="form-control" name="uname" value="{{ data.0.name }}">
                            <br>
                            <label class="form-label">Email id</label>
                            <br>
                            <input type="email" class="form-control" name="uemail" value="{{ data.0.email }}">
                            <br>
                            <label class="form-label">Mobile Number </label>
                            <br>
                            <input type="number" class="form-control" name="mobile" value="{{ data.0.mobile }}">
                            <br>
                            <label class="form-label">Message</label>
                            <br>
                            <textarea name="msg" class="form-control" cols="30" rows="10" >
                                {{ data.0.msg }}
                            </textarea>
                            <br>
                            <input type="submit" value="send" class="btn btn-primary"/>

                        </form>

                    </div>
                </div>
            </div>
    </body>
    </html>
    ```

8.  **Step 8 - Go the `index.html` file in you templates folder.**

    ```bash
    <!DOCTYPE html>

    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <title>Lakshya Jain</title>
    </head>
    <body>

        <nav class="navbar navbar-expand-lg bg-warning">
            <div class="container-fluid">
              <a class="navbar-brand" href="https://github.com/lakshyajain1508">Lakshya Jain</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                  <li class="nav-item">
                    <a class="btn btn-primary" aria-current="page" href="{% url 'dashboard' %}">Dashboard</a>
                  </li>

                </ul>
              </div>
            </div>
          </nav>

          <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-sm-6 ">
                    <h1>Add new Data</h1>
                    <form action="" method="POST">
                        {% csrf_token %}

                        <label class="form-label">Enter name</label>
                        <br>
                        <input type="text"  name="uname" class="form-control">
                        <br>
                        <label class="form-label">Email id</label>
                        <br>
                        <input type="email" class="form-control" name="uemail">
                        <br>
                        <label class="form-label">Mobile Number </label>
                        <br>
                        <input type="number" class="form-control" name="mobile">
                        <br>
                        <label class="form-label">Message</label>
                        <br>
                        <textarea name="msg" cols="30" rows="10" class="form-control"></textarea>
                        <br>
                        <input type="submit" value="send" class="btn btn-primary"/>

                    </form>
                </div>
            </div>
        </div>

    </body>
    </html>
    ```

9.  **Step 9 - Make new file named `urls.py` in app and paste this code.**
    ```bash
    from django.urls import path
    from . import views

    urlpatterns=[
        path("create",views.create,name='create'),
        path("",views.dashboard,name='dashboard'),
        path("edit/<sid>",views.edit),
        path("delete/<did>",views.delete),
    ]
    ```
10. **Step 10 - Now go to project `urls.py` file and update it.**
    ```bash
    from django.contrib import admin
    from django.urls import path , include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("",include("contact_app.urls")),   
    ]
    ```

11. **Step 11 - repeat step 4 in terminal**
    ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```

12. **Step 12 - Run your server with this command**
    ```bash
    python manage.py runserver
    ```

