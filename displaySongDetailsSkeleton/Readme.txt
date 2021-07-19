Assumptions:
==============
1. I have assumed that all the attributes have same number of key-value pairs.
2. Due to time-constraints, I have not taken care of adding constraints in the memory database table.
3. For adding star-rating, I have assumed that the song for which user is trying to rate exists in database. Hence, I have not implemented logic for adding new song in 'PUT' request.


Steps to run application:
===========================================
1. Need to create virtual environment and install following libraries before running application:
    - flask
    - flask-restful
2. Run app.py.

End-points for the service:
============================
1. /GET: To get all the items in a normalized data set. --> http://127.0.0.1:5000/details 
2. /GET: To get all the details of a given song's title --> http://127.0.0.1:5000/detail/<string:title>
3. /PUT: To rate a particular song  --> http://127.0.0.1:5000/detail/<string:title>


Test-cases for 2nd and 3rd end-points mentioned above:
=====================================================
INPUT:     http://127.0.0.1:5000/detail/3AM
OUTPUT: {
    "Detail": {
        "index": "0",
        "id": "5vYA1mW9g2Coh1HUFUSmlb",
        "title": "3AM",
        "danceability": 0.521,
        "energy": 0.673,
        "mode": 1,
        "acousticness": 0.00573,
        "tempo": 108.031,
        "duration_ms": 225947,
        "num_sections": 8,
        "num_segments": 830,
        "starRating": null
    }
}

   
INPUT:     http://127.0.0.1:5000/detail/3AM
REQUEST_BODY: {
                "Rating" : 4
              }
OUTPUT: {
          "Message": "The start rating has been updated"
        }
		
On requesting details of the above rated song:
------------------------------------------
OUTPUT: {
    "Detail": {
        "index": "0",
        "id": "5vYA1mW9g2Coh1HUFUSmlb",
        "title": "3AM",
        "danceability": 0.521,
        "energy": 0.673,
        "mode": 1,
        "acousticness": 0.00573,
        "tempo": 108.031,
        "duration_ms": 225947,
        "num_sections": 8,
        "num_segments": 830,
        "starRating": 4
    }
}
