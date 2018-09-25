=====
QUIZ
=====

Quiz is a simple Django app to conduct Web-based quizes. For each
question, visitors can choose one of the four options.

Quick start
-----------

1. Add "quiz" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'quiz',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('HomePage/', include('quiz.urls')),

3. Run `python manage.py migrate` to create the quiz models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/HomePage/ to participate in the quiz.
