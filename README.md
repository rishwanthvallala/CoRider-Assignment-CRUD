# Flask MongoDB CRUD Application

This is a Flask application that performs CRUD operations on a MongoDB database for a User resource using a REST API.

## Prerequisites

- Docker
- Docker Compose

## Setup and Running the Application

1. Clone this repository:
   ```
   git clone <repository-url>
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

## Testing with Postman

1. Open Postman and create a new HTTP request for each of the REST API endpoints.
2. Set the appropriate HTTP method (GET, POST, PUT, DELETE) and URL for each request.
3. For POST and PUT requests, set the request body to raw JSON and include the necessary user data.
4. Send the requests and verify the responses.

Example POST request body:
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123"
}
```

## Running Tests

To run the tests, execute the following command:

```
docker-compose run test
```

This will run all the tests in the `tests` directory.

## Running Individual Tests

If you want to run a specific test file or test case, you can use the following command:

```
docker-compose run test python -m unittest tests.test_user_resource.UserResourceTest.test_create_user
```

Replace `tests.test_user_resource.UserResourceTest.test_create_user` with the path to the specific test you want to run.