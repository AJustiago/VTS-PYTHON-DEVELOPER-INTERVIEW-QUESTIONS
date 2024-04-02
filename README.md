# VTS-PYTHON-DEVELOPER-INTERVIEW-QUESTIONS

# Movie Rating API

This is a Flask-based RESTful API for managing movie ratings.

## Getting Started

To get started with this API, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application by executing `python app.py`.
4. The API will be available at `http://localhost:5000`.

## Endpoints

### User Authentication

- **POST /login**: Authenticate users. Requires email and password.

### Movie Management

- **POST /add-movies**: Add a new movie to the database.
- **GET /movies**: Retrieve all movies in the database.
- **GET /movie/<int:movie_id>**: Retrieve details of a specific movie by its ID.

### Rating Management

- **POST /rate_movie**: Rate a movie. Requires user ID, movie ID, and rating.

## Data Files

- **user.json**: Contains user data.
- **movies.json**: Contains movie data.
- **rating.json**: Contains rating data.

## Usage Examples

### Login

**POST /login**
```
{
"email": "example@example.com",
"password": "password123"
}
```

### Add Movie

**POST /add-movies**
```
{
"id": 1,
"name": "Inception",
"genre": "Science Fiction",
"rating": 4.5,
"release_date": "2010-07-16"
}
```

### Rate Movie

**POST /rate_movie**
```
{
"user_id": 1,
"movie_id": 1,
"rating": 4.0
}
```

### Get Movie Details

**GET /movie/1**
```
{
    "average_rating": 3.87,
    "genre": "Comedy",
    "id": 1,
    "name": "Home Alone",
    "rating": "PG",
    "release_date": "01-04-1996"
}
```

## Dependencies

- Flask: Web framework for building APIs.
- json: For handling JSON data.

## Authors

- Alexander Justine Santiago
