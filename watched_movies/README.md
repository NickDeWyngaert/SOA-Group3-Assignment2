# Watched movies
This is a REST API where you can view your watched movies.

## CRUD
Import file Postman: [WatchedMovies.postman_collection.json](WatchedMovies.postman_collection.json)

### Create
* POST request
* [/api/movies](http://localhost:4000/api/movies)
```json
{
    "movie": {
        "title": "Interstellar",
        "genre": "science fiction",
        "director": "Christopher Nolan",
        "release": "2014-11-05",
        "duration": 169,
        "about": "In a post-truth 2067, crop blights and dust storms threaten humanity's survival. Joseph Cooper, a widowed engineer and former NASA pilot turned farmer, lives with his father-in-law, Donald; his 15-year-old son, Tom Cooper, and 10-year-old daughter, Murphy Murph Cooper. After a dust storm, strange dust patterns inexplicably appear on Murphy's bedroom floor; she attributes the anomaly to a ghost."
    }
}
```

### Read
* GET request
* Get all watched movies: [/api/movies](http://localhost:4000/api/movies)
* Get the watched movie with ID 1: [/api/movies/1](http://localhost:4000/api/movies/1)

### Update
* PUT/PATCH request
* Update the watched movie with ID 1: [/api/movies/1](http://localhost:4000/api/movies/1)
```json
{
    "movie": 
    {
        "about": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "director": "The Rock"
    }
}
```

### Delete
* DELETE request
* Delete the watched movie with ID: [/api/movies/1](http://localhost:4000/api/movies/1)
