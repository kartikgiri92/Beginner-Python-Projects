=====
QUIZ APP
=====

The following is a django Quiz project.  
'users' app handles all the users data, scoring and authentication system.   
'quiz' app handles the Quizes and templates .  

Quick start
-----------

1. Add "appname" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'appname',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('appname/', include('users.urls')),

3. Run `python manage.py migrate` to create the quiz models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/HomePage/ to participate in the quiz.

