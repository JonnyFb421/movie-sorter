from datetime import datetime

from flask import Flask, jsonify, request, abort


def get_hardcoded_movie_data():
    movies = [
        {
            'id': 1,
            'title': 'Drop Dead Fred',
            'year': 'May 24, 1991',
            'imdb_rating': 5.9,
            'rotten_tomato_rating': .09,
            'gross_box_office': 14.8,
            'budget': 6.788,
        },
        {
            'id': 2,
            'title': 'Death to Smoochy',
            'year': 'February 28, 2002',
            'imdb_rating': 6.3,
            'rotten_tomato_rating': .42,
            'gross_box_office': 8.3,
            'budget': 50,
        },
        {
            'id': 3,
            'title': 'Shrek',
            'year': 'April 22, 2001',
            'imdb_rating': 7.8,
            'rotten_tomato_rating': .88,
            'gross_box_office': 484.4,
            'budget': 60,
        },
        {
            'id': 4,
            'title': 'Serenity',
            'year': 'September 30, 2005',
            'imdb_rating': 7.8,
            'rotten_tomato_rating': .83,
            'gross_box_office': 40.3,
            'budget': 39,
        },
        {
            'id': 5,
            'title': 'Hot Fuzz',
            'year': 'March 14, 2007',
            'imdb_rating': 7.8,
            'rotten_tomato_rating': .91,
            'gross_box_office': 80.7,
            'budget': 16,
        },
        {
            'id': 6,
            'title': 'Eternal Sunshine of the Spotless Mind',
            'year': 'March 19, 2004',
            'imdb_rating': 8.3,
            'rotten_tomato_rating': .93,
            'gross_box_office': 72.3,
            'budget': 20,
        },
        {
            'id': 7,
            'title': 'Spider-Man: Into the Spider-Verse',
            'year': 'December 14, 2018',
            'imdb_rating': 8.4,
            'rotten_tomato_rating': .97,
            'gross_box_office': 375.5,
            'budget': 90,
        },
        {
            'id': 8,
            'title': 'Austin Powers: International Man of Mystery',
            'year': 'May 2, 1997',
            'imdb_rating': 7.0,
            'rotten_tomato_rating': .7,
            'gross_box_office': 67.7,
            'budget': 16.5,
        },
        {
            'id': 9,
            'title': 'Cloudy with a Chance of Meatballs',
            'year': 'September 18, 2009',
            'imdb_rating': 6.9,
            'rotten_tomato_rating': .86,
            'gross_box_office': 243,
            'budget': 100,
        },
        {
            'id': 10,
            'title': 'Terminator 2: Judgment Day',
            'year': 'July 3, 1991',
            'imdb_rating': 8.5,
            'rotten_tomato_rating': .93,
            'gross_box_office': 523.7,
            'budget': 100,
        },
    ]
    return {'movies': movies}


movie_data = get_hardcoded_movie_data()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_movies():
    sort_by = request.args.get('sort_by')
    ascending = request.args.get('sort_order')
    if not ascending or ascending != 'asc':
        reverse = True
    else:
        reverse = False
    if sort_by:
        if sort_by.lower() == 'year':
            movies = sorted(
                movie_data['movies'],
                key=lambda k:  datetime.strptime(k[sort_by], '%B %d, %Y'),
                reverse=reverse
            )
        else:
            movies = sorted(
                movie_data['movies'],
                key=lambda k: k[sort_by],
                reverse=reverse
            )
    else:
        movies = movie_data['movies']
    return jsonify(movies)


@app.route('/', methods=['PUT'])
def add_movie():
    args = request.get_json()
    if (
            args and
            'title' in args and
            'year' in args and
            'imdb_rating' in args and
            'rotten_tomato_rating' in args and
            'gross_box_office' in args and
            'budget' in args
    ):
        new_id = max([movie['id'] for movie in movie_data['movies']]) + 1
        new_movie = {
            'id': new_id,
            'title': args['title'],
            'year': args['year'],
            'imdb_rating': args['imdb_rating'],
            'rotten_tomato_rating': args['rotten_tomato_rating'],
            'gross_box_office': args['gross_box_office'],
            'budget': args['budget']
        }
        movie_data['movies'].append(new_movie)
        return jsonify(new_movie)
    else:
        abort(400, 'Missing required parameters in request body.')


@app.route('/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    if int(movie_id):
        movie_to_delete = [movie for movie in movie_data['movies'] if movie['id'] == movie_id]
        movie_data['movies'].remove(movie_to_delete[0])
        return jsonify(movie_data['movies'])
    else:
        abort(400, 'Missing required parameter: id')


@app.route('/<int:movie_id>', methods=['POST'])
def update_movie(movie_id):
    args = request.get_json()
    if int(movie_id) and args:
        movie_to_update = movie_data['movies'].index(
            [movie for movie in movie_data['movies'] if movie['id'] == movie_id][0]
        )
        if 'title' in args:
            movie_data['movies'][movie_to_update]['title'] = args['title']
        if 'year' in args:
            movie_data['movies'][movie_to_update]['year'] = args['year']
        if 'imdb_rating' in args:
            movie_data['movies'][movie_to_update]['imdb_rating'] = args['imdb_rating']
        if 'rotten_tomato_rating' in args:
            movie_data['movies'][movie_to_update]['rotten_tomato_rating'] = args['rotten_tomato_rating']
        if 'gross_box_office' in args:
            movie_data['movies'][movie_to_update]['gross_box_office'] = args['gross_box_office']
        if 'budget' in args:
            movie_data['movies'][movie_to_update]['budget'] = args['budget']

        return jsonify(movie_data['movies'][movie_to_update])
    else:
        abort(400, 'Missing required parameter: id')


if __name__ == '__main__':
    app.run('0.0.0.0', port='5000', debug=True)
