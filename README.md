# Test-applicationtask-django

The simple web application demonstrates how I develop a web application with Django, Bootstrap, and Docker.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to run with docker & docker-compose:

```
docker
docker-compose
```

In order to run with standard Django ways:

```
pip
virtaulenv (optional)
virtualenvwrapper (optional)
```

### Installing

A step by step series of examples that tell you have to get a development env running

Change to the project directory

Build the docker image
```
docker build image_name:1.0 .
```

Start the service
```
docker-compose up
```

Now you can access the web by the Url
```
http://localhost/
```
Note: This configuration is based on port 80, if you have any issue you could change it in docker-compose.py file.
## Running the tests

There are two sets of tests, the unit test and the view test.

```
python manage.py test
```

## Deployment
This demo is up and running on the following url: 
```
https://test-applicationtask.herokuapp.com/
```