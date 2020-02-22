# Applied

![image](https://user-images.githubusercontent.com/46699116/74805438-ebedf000-5297-11ea-91ac-684201d63747.png)

Applied is a Django project to assist in the job search and application process.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. This project is not in a production state.

### Prerequisites

Applied uses docker-compose to facillitate the development environment.

https://docs.docker.com/compose/install/

### Installing

Clone the repo

```
git clone https://github.com/M-Kruse/Applied.git
cd Applied
```

Prepare the DB

```
docker-compose run web python manage.py migrate
```

You can either set up the SMTP relay in the settings.py file, otherwise for testing purposes you can create a superuser from the command line to log in with.

```
docker-compose run web python manage.py createsuperuser
```

Spin up the docker-compose environment

```
docker-compose up
```

Now you should be able to log in from http://127.0.0.1:8000/

### API

The jobs API endpoint is functional so that a web scraper can send jobs to it. You can manually curl for testing

```
curl --user rusty:supersecret -d '{"source_site":"example.com",\"title":"Button Smasher","company":"Foo Corp","location":"Foo, USA","date_posted":"2 days ago","url":"https://example.com/", "description":{"text":"SUPER LONG TEXT DESCRIPTION"}}' -H "Content-Type: application/json" http://localhost:8000/api/jobs/
```

## Running the tests

TODO

## Deployment

TODO

## Built With

* [django](https://www.djangoproject.com/) - The web framework used
* [django_rest_framework](https://www.django-rest-framework.org/) - REST framework
* [django_adminlte3](https://github.com/d-demirci/django-adminlte3) - Theme & Template provider
* [python-docx-template](https://github.com/elapouya/python-docx-template) - DOCX Jinja2 Templating


## Authors

* **Matthew Kruse** - *Initial work* - [M-Kruse](https://github.com/M-Kruse)


See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
