FROM python:3.6.13
WORKDIR KubernetesManagerWeb
RUN pip install pipenv -i https://pypi.douban.com/simple
RUN pip install pymysql -i https://pypi.douban.com/simple
RUN pip install django -i https://pypi.douban.com/simple
RUN pip install djangorestframework -i https://pypi.douban.com/simple
RUN pip install django-cors-headers -i https://pypi.douban.com/simple
RUN pip install cryptography -i https://pypi.douban.com/simple
WORKDIR api/
COPY . .
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]