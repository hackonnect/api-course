# Make sure this file is named app.py
# Let's try to build a very simple API (an imitation of the practice API we used).
# We need to install a package that will allow us to make a RESTful API.
# pip install flask flask_restful.
# Flask is a Python framework for making web applications.
# Flask_RESTful allows us to use flask in order to make an API.

# First, we need to import the things we will need from the two libraries.
from flask import Flask
from flask_restful import Resource, Api, reqparse

# Now, let's initialise our Flask application and API.
app = Flask(__name__) # Flask app
api = Api(app) # API
parser = reqparse.RequestParser() # Parses (deals with) request parameters (remember those query strings?)
# We won't go into the specifics of what this does as that is out of the scope for this course.

# In order to keep everything simple, we'll just use a dictionary as our database
database = {'data1': 'value1'}

# Let's tell our parser what parameters we have.
# We'll only use two parameters: one for the data key and one for the data value.
parser.add_argument('key')
parser.add_argument('parser')

# Let's make an API Resource:
class API(Resource):
    # Making the get request first:
    def get(self):
        args = parser.parse_args() # This parses the arguments and parameters (query strings and other data)
        key = args['key'] # See if there is a parameter named 'key'
        if key: # If there is
            value = database['key'] # Find its value
            result = {key: value} # This is what we will return.
        else:
            result = database # If we don't get a particular key to search for, just return the whole database
        return result, 200 # Return the result along with a 200 status code (showing that the request was successful)
    
    # Let's make the post request:
    def post(self):
        args = parser.parse_args()
        key, value = args['key'], args['value'] # Save the key and value from the query string
        if key in database: # If the key is already in the database
            error = {'error': 'Entry already exists.'} # Error message
            return error, 404 # Return the error message along with a 404 error
        database[key] = value # Save the new entry
        return {key: value}, 201 # Return the saved key and value again, with a status code of 201 showing that the POST request was successful
    
    # Let's make the put request:
    def put(self):
        args = parser.parse_args()
        key, value = args['key'], args['value']
        if not key in database: # If the key does not exist
            error = {'error': 'Entry does not exist.'}
            return error, 404
        database[key] = value # Modify the original entry
        return {key: value}, 200 # Same as previous
    
    # As you can see, POST and PUT requests are actually very similar in implementation. They are only different because of manual restrictions.
    # The reason these manual restrictions exist is because of conventions of making a RESTful API.
    # Conventions are basically a set of rule everyone agrees on to keep things consistent.
    
    # Now let's make the delete request:
    def delete(self):
        args = parser.parse_args()
        key = args['key']
        if not key in database:
            error = {'error': 'Entry does not exist.'}
            return error, 404
        del database[key] # Delete the database entry with that specific key
        return database, 200 # Return the modified database

api.add_resource(API, '/') # Add our API at the URL '/'
# Now go to the terminal and run this file
# With the Flask app still running in the terminal, open a new terminal and attempt to call the differetn request methods on your database.