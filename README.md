# RKI-GeonameAPI

Django-webapp for easy access to a hierarchical geo-location database.

## Deployment

Create a virtual environment

```bash
python -m venv env
source env/bin/activate
```

## Database

Make sure to have installed the modified version of the [Geoname-DB](https://github.com/benmaier/GeoNames-MySQL-DataImport) beforehand. This app expects an instance of MySQL 8.0. The configuration file should look like this

```sql
CREATE SCHEMA `rkigeonames` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;
CREATE USER 'rkigeonames'@'localhost' IDENTIFIED BY 'REPLACETHISWITHTHERIGHTPASSWORD';
GRANT ALL PRIVILEGES ON rkigeonames.* TO 'rkigeonames'@'localhost';
GRANT SELECT ON geonames.* TO 'rkigeonames'@'localhost';
```

```config
[client]
host = ...
port = ...
user = ...
password = ...
database = rkigeonames
default-character-set = utf8mb4
```

and has to be located at `$(HOME)/.inig/mysql/db.cnf`.

## Django-specific things

The secret key has to be located at `$(HOME)/.inig/secret_key_geonames.txt`.
