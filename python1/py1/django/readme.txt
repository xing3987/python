1.创建项目指令：a.django-admin startproject name
                b.创建网站相关(进入工程文件夹)：python manage.py startapp appname
                 c.在setting中把app加入工程
                  d.models中写实体类，执行：python manage.py makemigrations 自动生成数据库实体
                   e.创建数据库：执行：python manage.py migrate
                    f.创建超级管理员:python manage.py createsuperuser
2.执行项目(先进入项目后)：python manage.py runserver
	