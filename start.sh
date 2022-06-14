# heroku config:set API_KEY=123334979696849
# heroku config:set API_SECRET=Jvd78nFKUziejHAW-b5Qn0gLuHk
# heroku config:set CLOUDINARY_URL=cloudinary://123334979696849:Jvd78nFKUziejHAW-b5Qn0gLuHk@da7srpwm6
# heroku config:set CLOUD_NAME=da7srpwm6
# heroku config:set DEBUG=False
# heroku config:set DISABLE_COLLECTSTATIC=1
# heroku config:set MODE=prod
# heroku config:set SECRET_KEY='django-insecure-h-4_vq % @6x462t8ly = k = +8os_54n7_lziad!i4 *$_rey9b@1mb'
# heroku config:set ALLOWED_HOSTS=project-accolades.herokuapp.com

git switch master
# python manage.py collectstatic
pip freeze > requirements.txt
git add .
git commit -m "heroku deployment"
git push heroku master
# heroku run python manage.py makemigrations
# heroku run python manage.py migrate
# heroku pg:reset
heroku pg:push accolades DATABASE_URL --app project-accolades
heroku open