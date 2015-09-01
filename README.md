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

1. Clone [mysql-box](https://github.com/Juraci/mysql-box)
  ```
  $ git clone git@github.com:Juraci/mysql-box.git
  ```
2. Follow it's README

3. Clone [pyxis-api-django](https://github.com/dhiana/pyxis-api-django) (That's me!)
  ```
  $ git clone git@github.com:dhiana/pyxis-api-django.git
  ```
4. Create virtualenv

5. Activate virtualenv

6. Install requirements

  ```
  $ pip install -r requirements.txt
  ```
7. Run server!

  ```
  $ cd pyxis_api
  $ python manage.py runserver
  ```

## Testing
```
$ cd pyxis_api
$ python manage.py test
```

## Authors

[Dhiana Deva](https://github.com/dhiana)

[Juraci Vieira](https://github.com/Juraci)

[Rafael Portela](https://github.com/rafaelportela)
