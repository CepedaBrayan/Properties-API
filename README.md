# PROPERTIES API

## Overview

This project is developed using [FastAPI](https://fastapi.tiangolo.com/), Minio, Docker, SQLAlchemy, Alembic, and PostgreSQL.

### Architecture

The choice of tools and technologies for this project is driven by specific requirements. FastAPI is chosen for its efficiency in creating REST APIs quickly. PostgreSQL, a relational database, is selected to establish relationships between properties and owners. Minio is used to store images of properties. Docker is used to containerize the application and its dependencies. SQLAlchemy is used as the ORM to interact with the database. Alembic is used to manage database migrations.

## Getting Started

Follow these steps to set up and run the project:

1. Open Docker Desktop (compatible with macOS and Windows).
2. Open a terminal in the project's root path and run the following commands:

```bash
docker-compose build
docker-compose up
```

3. Open a browser and navigate to http://localhost:9001/login to access the Minio web interface.
4. Sign in with the credentials:

```bash
username: minio_user
password: minio_password
```

5. Go to identity -> Service Accounts -> Create Service Account and button create.
6. Copy the access key and the secret key given just once.
7. Create a .env file following the structure like the .env.example file and paste the access key and the secret key.
8. kill the docker-compose process and run again the docker-compose up command given in the step 2.
9. Open a browser and navigate to http://localhost:8080/docs to access the API documentation.
10. Just play with the API.


# Migrations

If you want to make changes to the database, changing or adding new models, you must import the model file into the `alembic/env.py` file and run the following commands:

```bash
docker-compose exec backend bash
make make-migrations NAME="your migration name"
make run-migrations
```


# Testing

Testing is done using [pytest](https://docs.pytest.org/en/stable/). The test cases are located in the `test` folder.

## Test Details

The made tests are for the endpoints and test their correct functionality.

## Running Tests

To run the tests, follow these steps:

1. Create a bash session into the container:

    ```bash
    docker-compose exec backend bash
    ```

2. Run pytest:

    ```bash
    pytest  
    or
    make run-test
    ```



