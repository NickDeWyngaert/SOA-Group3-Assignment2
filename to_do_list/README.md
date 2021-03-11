# To do list for assignments

This is a REST API that allows you to view, add, remove and alter your assignments

## 

## CRUD

Import file Postman: [WatchedMovies.postman_collection.json](https://github.com/RedaBoussabat/SOA-Group3-Assignment2/blob/main/watched_movies/WatchedMovies_CRUD.postman_collection.json)

### 

### Create

- POST request
- [/to_do_items](http://127.0.0.1:8000/to_do_items/)

```
{
    "id": 1,
    "url": "http://127.0.0.1:8000/to_do_items/1/",
    "name": "SOA: Opdracht 2",
    "course": "SOA",
    "deadline": "2021-03-25",
    "soort": "Make webservice API"
}
```

### 

### Read

- GET request
- Get all to do items: [/to_do_items](http://127.0.0.1:8000/to_do_items/)
- Get the to do item with ID 1: [/to_do_items/1](http://127.0.0.1:8000/to_do_items/1/)

### 

### Update

- PUT/PATCH request
- Update the to do item with ID 1: [/to_do_items/1/](http://127.0.0.1:8000/to_do_items/1/)
- Name, course, deadline en soort mogen niet leeg zijn.

```
{
    "id": 1,
    "url": "http://127.0.0.1:8000/to_do_items/1/",
    "name": "SOA: Opdracht 2",
    "course": "SOA",
    "deadline": "2021-06-15",
    "soort": "Make webservice API- to do list"
}
```

### 

### Delete

- DELETE request
- Delete the to do item with ID: [/to_do_items/1](http://127.0.0.1:8000/to_do_items/1/)