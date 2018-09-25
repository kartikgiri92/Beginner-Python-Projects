=====
Users
=====

users is a simple Django app to store the score of the users of the quiz app.

Quick start
-----------

1. Add "users" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'users',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('users/', include('users.urls')),

3. Run `python manage.py migrate` to create the users models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a user and score (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/HomePage/ to participate in the quiz.
