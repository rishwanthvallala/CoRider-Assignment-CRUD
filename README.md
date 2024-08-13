# Flask MongoDB CRUD Application

This is a Flask application that performs CRUD operations on a MongoDB database for a User resource using a REST API.

## Prerequisites

- Docker
- Docker Compose

## Setup and Running the Application

1. Clone this repository:
   ```
   git clone https://github.com/rishwanthvallala/CoRider-Assignment-CRUD.git
   cd flask-mongodb-crud
   ```

2. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

3. The application will be available at `http://localhost:5000`.

## API Endpoints

- GET /users - Returns a list of all users.
- GET /users/<id> - Returns the user with the specified ID.
- POST /users - Creates a new user with the specified data.
- PUT /users/<id> - Updates the user with the specified ID with the new data.
- DELETE /users/<id> - Deletes the user with the specified ID.



## Running Tests

To run the tests, execute the following command:

```
docker-compose run test
```

This will run all the tests in the `tests` directory.

