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

Login as an admin at http://localhost:8000/admin or http://localhost:8000/login

## Logic

The Geoname-Database is an open-source dataset containing an exhaustive list of places on earth.
The database contains information about a variety of properties and relationships of these places
such as alternative names in multiple languages, positional data, and hierarchical relationships
(e.g. to which country oder administrative division a place belongs).

This project provides a simple interface to this database which allows a user to easily
retrieve data and to edit hierarchical relationships.


### Feature codes

Each place is associated with a feature code. Here are the most relevant ones with explanations

#### Continents and regions

These are the ones that usually contain countries

fcode | name | description
----- | ---- | -----------
CONT | continent | continent: Europe, Africa, Asia, North America, South America, Oceania, Antarctica
RGN | region | an area distinguished by one or more observable physical or cultural characteristics

#### Countries

These are used as synonyms for countries

| PCLI | independent political entity
| TERR | territory
| PCLD | dependent political entity

#### Places

These are used as synonyms for cities/villages/places that are neither countries nor regions nor administrative sections.

| PPLC | capital of a political entity | |
| PPL | populated place | a city, town, village, or other agglomeration of buildings where people live and work
| PPLA | seat of a first-order administrative division | seat of a first-order administrative division (PPLC takes precedence over PPLA) 
| PPLX | section of populated place | |

#### Administrative divisions

These are hierarchically decreasing administrative divisions of a country

| ADM1| first-order administrative division | a primary administrative division of a country, such as a state in the United States
| ADM2| second-order administrative division | a subdivision of a first-order administrative division
| ADM3| third-order administrative division | a subdivision of a second-order administrative division
| ADM4| fourth-order administrative division | a subdivision of a third-order administrative division
| ADM5| fifth-order administrative division | a subdivision of a fourth-order administrative division

