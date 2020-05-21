# web-backend-admin

### Instructions

This is API REST created with Flask and SQLAlchemy

- Run `pip install -r requirements.txt`
- You need a PostGreSQL database running on machine, if you need, you can use the postgres from the docker on the project, see the Docker Section to it;
- Copy the .env.example to .env on docker folder and set the values on vars;
- Run `python manage.py db upgrade` to create the tables;
- If change the models ou new database structure, you need to generate the new migration version, for it, you need use the command `python manage.py db migrate --message 'adding or changing table'`;

### Docker

THe project have docker with different tools, you don't need run all tools on you machine, run only the tools that you need, for instance, if you need a postgresql and a python environment database, you can run: `docker-compose up app postgresql`
