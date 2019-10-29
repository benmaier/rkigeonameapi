Beware! This is a whole django project. If you want to install the database as an app to your project, please check out https://github.com/benmaier/django-rkigeonameapi/.

# RKI-GeonameAPI

Django-webapp for easy access to a hierarchical geo-location database.

## License

This project is published under the MIT license. It uses the [geoname-data](http://www.geonames.org/) which is licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).

## Install and Deployment

Only tested with Python 3.7.

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

Note that this project renames the `name` property of all locations to contain their most common German name. If you **don't** want this, you should
edit the file `sql_setup_files/geonamemigration.sql` and replace all occurrences of `isoLanguage = 'de'` for the language you want to use. In order to 
use the original English name, set `isoLanguage = 'XXXXX'` or something similarly non-sensical (the script automatically uses the English name for any
location for which it cannot find a name in the demanded language).

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

### Geonames

A Geoname is a main geographical entity. It could be a populated place, a country or something else.

#### API endpoints

Admin: http://localhost:8000/admin/geonameapi/geoname/ 

REST:

| Action | Link | Description |
| ------ | ---- | ----------- |
| list/create | http://localhost:8000/geonameapi/geoname/ | Show a JSON list of all Geoname-objects and add an entry |
| view/update | http://localhost:8000/geonameapi/geoname/<int:pk> | Show a single Geoname-object associated with the primary key as JSON |
| search | http://localhost:8000/geonameapi/geonamesearch/SEARCHSTRING | Show all Geoname-objects whose `name` and `englishname` contain the `SEARCHSTRING` |
| exhaustive search | http://localhost:8000/geonameapi/geonameexhaustivesearch/SEARCHSTRING | Show all Geoname-objects whose `alternatenames` or `englishname` start with the `SEARCHSTRING` |
| search by feature code | http://localhost:8000/geonameapi/geonamesearch/SEARCHSTRING?fcode=ADM1,PCLI | As above, but only show geonames whose feature code is in the list of feature codes provided in the URL |
| exhaustive search by feature code| http://localhost:8000/geonameapi/geonameexhaustivesearch/SEARCHSTRING?fcode=ADM1,PCLI | See definitions above |

A Geoname can always contain multiple children (think of a US state containing cities). Here's how you control those hierarchical relationships

Admin: http://localhost:8000/admin/geonameapi/hierarchy/

REST:

| Action | Link | Description |
| ------ | ---- | ----------- |
| update | http://localhost:8000/geonameapi/geonamechildren/<int:pk> | Show (`GET`) and update (`PATCH`) the children of a single Geoname-object |
| view specific | http://localhost:8000/geonameapi/geonamefcodechildren/<int:pk>?fcode=ADM1,ADM2 | Show all children of a single Geoname-object that are associated with any of the specified feature codes |


### Feature codes

Each Geoname is associated with a feature code. Here are the most relevant ones with explanations

Admin: http://localhost:8000/admin/geonameapi/featurecode

REST: 

* list/create: http://localhost:8000/geonameapi/featurecode
* view/update: http://localhost:8000/geonameapi/featurecode/<str:pk>

#### Continents and regions

These are objectes that usually contain multiple countries

fcode | name | description
----- | ---- | -----------
CONT | continent | continent: Europe, Africa, Asia, North America, South America, Oceania, Antarctica
RGN | region | an area distinguished by one or more observable physical or cultural characteristics

A region might also contain other places but this won't be of interest in this application. 

#### Countries

These are used as synonyms for countries

| fcode | name 
| ----- | ---- 
| PCLI | independent political entity
| TERR | territory
| PCLD | dependent political entity

#### Places

These are used as synonyms for cities/villages/places that are neither countries nor regions nor administrative sections.

| fcode | name | description
| ----- | ---- | -----------
| PPLC | capital of a political entity | |
| PPL | populated place | a city, town, village, or other agglomeration of buildings where people live and work
| PPLA | seat of a first-order administrative division | seat of a first-order administrative division (PPLC takes precedence over PPLA) 
| PPLX | section of populated place | |

#### Administrative divisions

These are hierarchically decreasing administrative divisions of a country

| fcode | name | description
| ----- | ---- | -----------
| ADM1| first-order administrative division | a primary administrative division of a country, such as a state in the United States
| ADM2| second-order administrative division | a subdivision of a first-order administrative division
| ADM3| third-order administrative division | a subdivision of a second-order administrative division
| ADM4| fourth-order administrative division | a subdivision of a third-order administrative division
| ADM5| fifth-order administrative division | a subdivision of a fourth-order administrative division


### Regions

Custom regions are shortcuts for improved handling/grouping of countries.

Admin: http://localhost:8000/admin/geonameapi/region/

REST:

* list/create: http://localhost:8000/geonameapi/region/
* view/update: http://localhost:8000/geonameapi/region/<str:pk>

You may want to alter a region's children countries by using

* http://localhost:8000/geonameapi/regioncountries/<str:pk>

### Countries

The database holds specific info about countries.

Admin: http://localhost:8000/admin/geonameapi/country/

REST:

* list/create: http://localhost:8000/geonameapi/country/
* view/update: http://localhost:8000/geonameapi/country/<str:pk>

### Continents

The database holds specific info about continents.

Admin: http://localhost:8000/admin/geonameapi/continent/

REST:

* list/create: http://localhost:8000/geonameapi/continent/
* view/update: http://localhost:8000/geonameapi/continent/<str:pk>

