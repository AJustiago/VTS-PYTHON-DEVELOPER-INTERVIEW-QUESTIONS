from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load user data from JSON file
with open('user.json', 'r') as f:
    users = json.load(f)

# Load movie data from JSON file
with open('movies.json', 'r') as f:
    movies = json.load(f)

# Load rating data from JSON file
with open('rating.json', 'r') as f:
    ratings = json.load(f)

# User authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    for user in users:
        if user['email'] == email:
            if user['password'] == password:
                return jsonify({"message": "Login successful", "user_id": user['id']}), 200
            else:
                return jsonify({"message": "Wrong password"}), 401
    return jsonify({"message": "Email not found"}), 404

# Add a movie
@app.route('/add-movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    required_fields = ['id', 'name', 'genre', 'rating', 'release_date']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"message": f"Missing fields: {', '.join(missing_fields)}"}), 400

    if None in data.values():
        return jsonify({"message": "One or more fields contain None"}), 400

    movies.append(data)

    with open('movies.json', 'w') as f:
        json.dump(movies, f, indent=4)

    return jsonify({"message": "Movie added successfully"}), 201


# View all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

# Rate a movie
@app.route('/rate_movie', methods=['POST'])
def rate_movie():
    data = request.get_json()
    user_id = data.get('user_id')
    movie_id = data.get('movie_id')
    rating = data.get('rating')

    if not any(user['id'] == user_id for user in users):
        return jsonify({"message": "User ID does not exist"}), 404

    if not (0.1 <= rating <= 5.0):
        return jsonify({"message": "Rating must be between 0.1 and 5.0"}), 400

    for m in movies:
        if m['id'] == movie_id:
            ratings.append({"user_id": user_id, "movie_id": movie_id, "rating": rating})
            with open('ratings.json', 'w') as f:
                json.dump(ratings, f, indent=4)
            return jsonify({"message": "Rating added successfully"}), 201
    return jsonify({"message": "Movie not found"}), 404


# Search for a specific movie and see its details along with the average rating
@app.route('/movie/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    for m in movies:
        if m['id'] == movie_id:
            movie_ratings = [rating['rating'] for rating in ratings if rating['movie_id'] == movie_id]
            average_rating = round(sum(movie_ratings) / len(movie_ratings), 2) if movie_ratings else 0
            movie_details = {"id": m['id'], "name": m['name'], "genre": m['genre'], "rating": m['rating'],
                             "release_date": m['release_date'], "average_rating": average_rating}
            return jsonify(movie_details)
    return jsonify({"message": "Movie not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
