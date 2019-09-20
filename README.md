# Movie Sorter
> Flask API that sorts hardcoded movie data

## Usage
Prerequisite: Install Flask with `pip install flask`  
Start Server: `python movie_sorter.py`  

### Endpoints
#### GET /
##### Returns all movies  
Possible path parameters:  
```
sort_by: title, year, imdb_rating, rotten_tomato_rating, budget, gross_box_office, id

sort_order: asc, desc (defaults to desc)
```  
Example: 
```
 curl -i -X GET http://0.0.0.0:5000/?sort_by=year&sort_order=asc
```


#### POST /\<id\>
##### Updates existing movie attributes by id
At-least one of the following parameters is required in the body of the request:
```
title
year
imdb_rating
rotten_tomato_rating
budget
gross_box_office
```
Example:
```
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Jonnys Big Break", "year":"April 21, 1992"}' http://0.0.0.0:5000/3
```


#### PUT /
##### Adds new movie  
All of the following parameters are required in the body of the request:
```
title
year
imdb_rating
rotten_tomato_rating
budget
gross_box_office
```
Example:
```
curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"Clover: Big Paw Kitty Cat", "year":"June 3, 2020", "imdb_rating":10, "rotten_tomato_rating":1.0, "budget":1, "gross_box_office":9999 }' http://0.0.0.0:5000/
```


#### DELETE /\<id\>
##### Deletes a movie by id
This endpoint only requires the ID of the movie to delete  
Example:  
```
curl -i -X DELETE http://0.0.0.0:5000/6
```
