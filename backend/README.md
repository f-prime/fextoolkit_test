# Backend

This is a simple web application with a single HTTP endpoint, `/search/`. 

`/search/` takes at least one of three optional query arguments: `firstName`, `lastName`, `state`.

`/search/?firstName=Jack` will return all the people that have a first name of Jack 

`/search/?firstName=Jack&lastName=Dovel&state=NC` will return all people with the first name of Jack and last name of Dovel in the state of North Carolina.

The response body looks like this:

```
[
  {
    "first_name": "Jack", 
    "last_name": "Dovel", 
    "phonenumber": "4141604385", 
    "state": "NC"
  }
]

```

# Install

1. Make sure that you have Python 3.8 and Pip3 installed on your machine.
2. Install the dependencies with `pip3 install -r requirements.txt`
3. Start the server with `python3 app.py`
