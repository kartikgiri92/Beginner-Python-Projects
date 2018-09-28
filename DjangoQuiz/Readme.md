QUIZ APP

The following is a django Quiz project. It contains two apps.      
'users' app handles all the users data, scoring and authentication system.   
'quiz' app handles the Quizes and templates .  

Quick start
-----------
0. Copy and paste the two apps into the project folder(same as that of manage.py).  

1. Add appnames to your INSTALLED_APPS setting like this::  
  
    INSTALLED_APPS = [  
        ...  
        'quiz',  
        'users',  
    ]  
  
2. Include the appname URLconf in your project urls.py like this::  
    path('HomePage/', include('quiz.urls')),  
    path('users/', include('users.urls')),  

3. Run **python manage.py makemigrations** and **python manage.py migrate** to create the app models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to add data (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/HomePage/ to participate in the quiz.

