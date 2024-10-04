# Django-setup-best-practice
Relearn to follow Django best practice

[SSH Key for production]
Phrase 1: Set Up
- build virtual environment
- pip install django
- startproject (with additional '.')
- startapp
- install new app to setting.py
- write simplest view function
- routing urls.py
- migrate model
- check setup with runserver
- pip freeze > requirements.txt
- git init
- new github repo 
- git initial commit & push main

[Hosting: Heroku] - Install & Login Heroku CLI in the local machine
[Server: Gunicorn] or uWSGI
Phrase 2: Heroku Deployment
- pip install gunicorn
- pip freeze > requirements.txt
- ALLOW_HOST=["*"]
    @Same directory as manage.py 
- echo "web : gunicorn PROJECTNAME.wsgi --log-file -" > Procfile
- echo "python-VERSION" -> runtime.txt                        ##all in lowercase
    @within venv
- heroku create                                               (this automatically create git remote 'heroku')
- heroku config:set DISABLE_COLLECTSTATIC=1                   (Ignore Static file)
- git push heroku main                                        (push code to heroku server)
  *possible error: stack version not support python version-> heroku stack:set heroku-VERSION -a APPNAME
- heroku ps:scale web=1                                       (choose service level)
- heroku open
