
# Django rest api authentication

Simple authentication app made in django rest framework. The idea of application was to 
implement token based authentication in django and postgresql database.



## Setup

Install Django on your computer

Install Django rest framework with pip
```bash 
pip Install djangorestframework
```
Run migrations to create database migrations.
```bash 
py manage.py makemigrations
```
```bash 
py manage.py migrate
```
Create superuser to manage program
```bash
py manage.py createsuperuser
```
Run the server 
```bash
py manage.py runserver
```
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.
Name, user, password, host and port are required to login to postgresql database and secret is django
secret key.

`NAME`
`USER`
`PASSWORD`
`HOST`
`PORT`
`SECRET`

## Authors

- [@Szymon Cwynar](https://www.github.com/szymcwy)


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/szymon-cwynar-b1b4b5232/)


