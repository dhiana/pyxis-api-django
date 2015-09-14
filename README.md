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

### Set up a database

* This project expects [subunit2sql](https://github.com/openstack-infra/subunit2sql) schema
* You can use [mysql-box](https://github.com/Juraci/mysql-box):
    * Get a dump from a subunit2sql database
    * Clone the repo
    
      ```
      $ git clone git@github.com:Juraci/mysql-box.git
      ```
    * Follow its README

### Clone this repo

  ```
  $ git clone git@github.com:dhiana/pyxis-api-django.git
  ```
### Get this application up and running:
  
#### Using a Vagrant box:

* Provision the vagrant box

    ```
    $ vagrant up
    ```
* Go to [http://192.168.33.43:5000/runs/]

#### Or for local development:

* Create virtualenv

* Activate virtualenv

* Install requirements

    ```
    $ pip install -r requirements.txt
    ```
* Run server!

    ```
    $ cd pyxis_api
    $ python manage.py runserver 5000
    ```
* Go to [http://localhost:5000/runs]

### Start a client application

* Follow README at [https://github.com/dhiana/pyxis-app]

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
