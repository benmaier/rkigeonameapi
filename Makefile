CNF=$(HOME)/.inig/mysql/rki_geonames_db.cnf
#MYSQL=mysql
MYSQL=/usr/local/mysql/bin/mysql
PYTHON=/Users/bfmaier/Sites/django-inig/env/bin/python
SQLFILES=sql_setup_files

geonamemigrate:
	$(MYSQL) --defaults-file=$(CNF) -v < $(SQLFILES)/geonamemigration.sql

cleanmigrate:
	rm geonameapi/migrations/*.py

# before you run this you have to manually drop tables
resetdatabase:
	make cleanmigrate
	make prepmigrate
	make migrate
	make geonamemigrate

droptables:
	$(PYTHON) manage.py migrate geonameapi zero

prepmigrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py makemigrations geonameapi

migrate:
	$(PYTHON) manage.py migrate

superuser:
	$(PYTHON) manage.py createsuperuser

runserver:
	$(PYTHON) manage.py runserver

