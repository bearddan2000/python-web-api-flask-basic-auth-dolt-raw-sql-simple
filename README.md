# python-web-api-flask-basic-auth-dolt-raw-sql-simple

## Description
Creates an api of `dog` by using raw sql for a flask project.
Has the ability to query by parameters.
If path is not found, will default to 404 error.

Requires basic authentication for CRUD opperations.

| username | password |
| ------- | -------- |
| *user* | *pass* |

Remotely tested with *testify*.

## Tech stack
- python
  - flask
  - sqlalchemy
  - testify
  - requests

## Docker stack
- python:latest
- dolthub/dolt-sql-serverdb:latest

## To run
`sudo ./install.sh -u`
- Get all dogs: http://localhost/dog
  - Schema id, breed, and color
- CRUD opperations
  - Create: curl -i -X PUT localhost/dog/<id>  -u 'user:pass'
  - Read: http://localhost/dog/<id> -u 'user:pass'
  - Update: curl -i -X POST localhost/dog/<id>/<breed>/<color>  -u 'user:pass'
  - Delete: curl -i -X DELETE localhost/dog/<id>  -u 'user:pass'

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
