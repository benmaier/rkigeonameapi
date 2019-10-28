# RKI-GeonameAPI

Django-webapp for easy access to a hierarchical geo-location database.

## Install and Deployment

### Deployment

Create a virtual environment

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Django-specific things

The secret key has to be located at `$(HOME)/.inig/secret_key_geonames.txt`.

### Database

Make sure to have installed the modified version of the [Geoname-DB](https://github.com/benmaier/GeoNames-MySQL-DataImport) beforehand. This app expects an instance of MySQL 8.0. The configuration file should look like this

```sql
CREATE SCHEMA `rkigeonames` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;
CREATE USER 'rkigeonames'@'localhost' IDENTIFIED BY 'REPLACETHISWITHTHERIGHTPASSWORD';
GRANT ALL PRIVILEGES ON rkigeonames.* TO 'rkigeonames'@'localhost';
GRANT SELECT ON geonames.* TO 'rkigeonames'@'localhost';
```

The configuration file should look like this.

```config
[client]
host = ...
port = ...
user = ...
password = ...
database = rkigeonames
default-character-set = utf8mb4
```

and has to be located at `$(HOME)/.inig/mysql/rki_geonames_db.cnf`.

### Initialize the project

After installing [Geoname-DB](https://github.com/benmaier/GeoNames-MySQL-DataImport), edit the following line in the `Makefile` according to your needs:

```Makefile
CNF=$(HOME)/.inig/mysql/rki_geonames_db.cnf
MYSQL=/usr/local/mysql/bin/mysql
PYTHON=/env/bin/python
SQLFILES=sql_setup_files
```

Start the data migration and initialization by running

    make resetdatabase

Create a superuser

    make superuser

Run the server

    make runserver

Login as an admin at http://localhost:8000/admin

## Logic

The Geoname-Database is an open-source dataset containing an exhaustive list of places on earth.
The database contains information about a variety of properties and relationships of these places
such as alternative names in multiple languages, positional data, and hierarchical relationships
(e.g. to which country oder administrative division a place belongs).

This project provides a simple interface to this database which allows a user to easily
retrieve data and to edit hierarchical relationships.


