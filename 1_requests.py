# You might want to teach this course using the live interpreter instead. It's a lot easier to showcase the results of different requests.
# However, this file will still print out the results.

# First let's visit our practice API:
# https://hackonnect-api.herokuapp.com
# API, or Application Programming Interface, allows us to interface with online databases
# As you can see our database has two columns: a data key column and a value column.
# Currently there are only 3 entries, data1, data2 and data3.
# Many APIs will have interfaces like this to let you see its contents.
# However, some don't, and even if they do, displaying the information like this is slightly annoying for us to deal with.
# In Python, there is a requests library that we can use in order for us to request data from APIs.

# Let's import 4 methods from that library now: GET, POST, PUT and DELETE
from requests import get, post, put, delete

# These four methods are the most common methods used to interact with APIs.
# When dealing with online databases, GET is used the most.
# Let's try to retrieve all the entries of our practice database:

print(get(url='https://hackonnect-api.herokuapp.com/api')) # <Response 200>

# Bear in mind that our practice API is very simple and real APIs will be slightly more complicated.
# Different APIs will have different URLs for different methods. It is important to read the API documentation when using them.
# We'll have a practice at this later on.
# Our practice API is very simple: there is only one URL for us to worry about, which is the website URL + /api
# We can call different methods on this URL to get different results.

# Because we will be using the url a lot, let's save it as a variable.

url = 'https://hackonnect-api.herokuapp.com/api'

# When using GET, POST, PUT, DELETE, we don't actually have to put the url=<url> down.
# The requests library will automatically recognise it as an URL.

print(get(url)) # <Response 200>

# In order to get the data inside our HTTPS response, we can add .json() to the end of get().

print(get(url).json()) # This should print a dictionary with our database values.

# What if we want to get a single entry only?
# There are two ways to do this.
# We can also pass data with our GET request like this:

print(get(url, data={'key': 'data1'}).json()) # {'data1': 'value1'}

# Or like this:

print(get(url + '?key=data1').json()) # {'data1': 'value1'}

# In general, the second option is more commonly used because of its simplicity.
# The url becomes: https://hackonnect-api.herokuapp.com/api?key=data1
# The part after the question mark is called the query string, and has this format:
# ?parameter1=value&parameter2=value&parameter3=value... etc.
# This is the format we will be using.

# As you can see, we can pass a dictionary as the data with our GET request. We specificed which key we wanted to retrieve.
# The data we passed are called the 'parameters' of our request.
# The parameter name in this case is key, with a parameter value of data1.
# Our API only accepts two types of parameters: key and value. This is because of the simplicity of our API.
# When we work with an actual API later on, we'll look at how we can use parameters to filter data.
# Now try to do this for the two other data keys:

# Solution should be obvious enough. Give them 1 or 2 minutes to play around with this.
# Tell them to try to retrieve data4 and see what happens. Should get this:
# {'message': 'Internal Server Error'}

# When you try something that doesn't work you will get an error. Now let's try adding data4 in so that it works.
# Usually, we use POST requests in order to create a new entry (URI, universal resource identifier) in database:

post(url + '?key=data4&value=value4')
# After running this, reload the page in order to show how the database changes.
# Post also returns a value

# Now, we can try retrieving data4 again:
print(get(url + '?key=data4').json())

# Let's try to POST something that is already there:

print(post(url + '?key=data4&value=value4').json())

# Oops, we get an error! Our practice API automatically sees if the value is already there and rejects new POST requests.

# Let them try to post different data values
# Reload the page and realise that the chaos happening.
# After a couple of minutes move on to PUT requests.

# In order to modify the data, we need to use PUT requests. Let's try to modify data1:

put(url + '?key=data1&value=new value!')

# Reload the page to see the result.

# What if we try to modify a data entry that isn't there?

put(url + '?key=a key that is not there!&value=new value!')

# Once again, we get an error.
# Let them have fun again for a few minutes.

# Finally, we can use DELETE in order to delete entries:

delete(url + '?key=data1')

# Reload the page and see that the first entry is now gone.
# Mention that it will not work if you try to delete a non-existent entry.

delete(url + '?key=a key that is not there!')

# Let them have fun again. Prepare for the next part of the course.