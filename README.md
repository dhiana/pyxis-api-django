# pyxis-api-django [![Build Status](https://snap-ci.com/dhiana/pyxis-api-django/branch/master/build_image)](https://snap-ci.com/dhiana/pyxis-api-django/branch/master)
RESTful API on top of [subunit2sql](https://github.com/openstack-infra/subunit2sql).

## Requirements

* Python 2.7
* Pip
* [Virtualenv](https://virtualenv.pypa.io/en/latest/)
* MySQL (client)

Optional:

* [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

## Getting Started

1. Set up a database with [subunit2sql](https://github.com/openstack-infra/subunit2sql) schema

1.1. You can use [mysql-box](https://github.com/Juraci/mysql-box):

1.1.1. Get a dump from a subunit2sql database

1.1.2. Clone the repo

  ```
  $ git clone git@github.com:Juraci/mysql-box.git
  ```
1.1.3. Follow its README

2. Clone [pyxis-api-django](https://github.com/dhiana/pyxis-api-django) (That's me!)

  ```
  $ git clone git@github.com:dhiana/pyxis-api-django.git
  ```
3. Get this application up and running:
  
3.1. Using a Vagrant box:

3.1.1. Provision the vagrant box
```
$ vagrant up
```
3.1.2. Go to (http://192.168.33.43:5000/runs/)[http://192.168.33.43:5000/runs/]

3.2. Or for local development:

3.2.1. Create virtualenv

3.2.2. Activate virtualenv

3.2.3. Install requirements

  ```
  $ pip install -r requirements.txt
  ```
3.2.4. Run server!

  ```
  $ cd pyxis_api
  $ python manage.py runserver 5000
  ```
3.2.5. Go to (http://localhost:5000/runs/)[http://localhost:5000/runs]

4. Start a client application

4.1. Follow README at (https://github.com/dhiana/pyxis-app)[https://github.com/dhiana/pyxis-app]

## Testing

### Server tests
```
$ vagrant up
$ rake spec
```

### Unit tests
```
$ cd pyxis_api
$ python manage.py test
```
