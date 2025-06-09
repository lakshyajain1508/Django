# Django Create App

In Django, a project is typically made up of one or more apps. Each app is a self-contained module that encapsulates a specific functionality of the overall project. Here's how you can create a new app within a Django project:

### Steps to Create a Django App:

1. **Navigate to Your Project Directory:**
   Open a terminal or command prompt and change your working directory to the root directory of your Django project.

   ```bash
   cd projectname
   ```

   Replace `projectname` with the actual name of your Django project.

2. **Run the Create App Command:**
   Use the following command to create a new app within your Django project:

   ```bash
   python manage.py startapp appname
   ```

   Replace `appname` with the desired name for your app. This command will create a new directory with the specified app name and the necessary files and directories inside.

3. **Run the Development Server:**
   Start the development server to see your app in action:

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your web browser and explore the functionality provided by your app.

That's it! You've successfully created a Django app and integrated it into your project. You can now continue building the app by defining views, templates, and adding more functionality as needed.