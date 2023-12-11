# EMAIL EVENT CATCHER

## Overview

This project is developed using [FastAPI](https://fastapi.tiangolo.com/), Docker, SQLAlchemy, Alembic, and PostgreSQL.

### Architecture

The choice of tools and technologies for this project is driven by specific requirements. FastAPI is chosen for its efficiency in creating REST APIs quickly. PostgreSQL, a relational database, is selected to establish relationships between customers, emails, products, and events.

## Getting Started

Follow these steps to set up and run the project:

1. Extract the project from the provided archive.
2. Open Docker Desktop (compatible with macOS and Windows).
3. Open a terminal in the project's root path and run the following commands:

```bash
docker-compose build
docker-compose up
```

4. Open a browser and navigate to http://localhost:8080/docs to access the API documentation.


# Testing

Testing is done using [pytest](https://docs.pytest.org/en/stable/). The test cases are located in the `test` folder.

## Test Details

The tests are designed as follows:

- **Test Data:** Utilizing the provided .json examples to create comprehensive testing cases.
- **Objective:** Each test is intended to achieve a response code of 200 for the JSON payload sent to the POST endpoint.

## Running Tests

To run the tests, follow these steps:

1. Create a bash session into the container:

    ```bash
    docker-compose exec backend bash
    ```

2. Run pytest:

    ```bash
    pytest
    ```

Basically i took the .json examples that you sent me for creating the testing cases, so, this test hopes to get response code 200 for each json as a payload for the post endpoint.


