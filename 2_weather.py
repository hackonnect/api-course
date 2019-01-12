# Let's try this with a weather API online.
# This is the US government weather API.
# You do not need to sign up and get an API key to use it.
# When using other API services on your own, you may have to sign up.
# Always read the instructions and documentation.

# We won't be able to edit their data so we only need the GET request.

from requests import get

# https://www.weather.gov/documentation/services-web-api
# Click on Specification for the API documentation
# The API is located at: https://api.weather.gov so let's set that as a variable:

api = 'https://api.weather.gov/' # Make sure there is a backslash! This will be important because of how their API works.

# Check that the api variable is entered correctly:

print(get(api).json()) # {'status': 'OK'}

# Make sure that everyone is setup properly before moving on.
# Guide them through reading the documentation:
# 1. Understand which request to use by looking at the text on the left.
# 2. Know what URL to use for their requests.
# 3. Know what parameters can be used to filter results.
# 4. Interpreting the data model and result.

# Now use alerts as an example.
# We can concatenate the URL with alerts in order to get https://api.weather.gov/alerts
print(get(api + 'alerts')) # A lot of information

# We can use parameters to filter this. Let's try to find alerts with a status of 500:
print(get(api + 'alerts?status=500').json())

# Let's find all test messages:
print(get(api + 'alerts?event=Test Message').json())

# Exercise: Try to find all active alerts in New York.
# (Make sure there are active alerts for New York before the course starts, if not just remove the state restriction)
# Hint: active lets you filter for active alerts, and area lets you use the state code of New York.
# Hint: The state code of New York is NY.

# Solution:
print(get(api + 'alerts?active=true&area=NY').json())

# Of course, this information is still suboptimal because it's hard for us to understand things.

# Let's see what the structure of the response we get first is:
alerts = get(api + 'alerts?active=true&area=NY').json()
for alert in alerts.items():
    print(alert) # @context \n type \n features \n title \n updated

# Let's see what each thing is:
print(alerts['@context']) # Some API settings. Not that useful to us.
print(alerts['type']) # FeatureCollection. So this JSON is a result of us trying to collect features.
print(alerts['features']) # Really long. This is presumably what we need.
print(alerts['title']) # current watches, warning, and advisories for New York. Describes the data we are collecting.
print(alerts['updated']) # <time the two queries are run this>. Gives us the current time.

# Since features is what we need, let's save it as a separate variable
features = alert['features']

# See how many things are inside features:
for feature in features:
    print(feature) # When I made this document, there was only one feature. Check how many features there are.

# Ok if we look through it carefully, we can see that most of the content is stored under 'properties'.
# Let's make a new variable.

properties = features[0]['properties'] # Features is a list of feature. We are retrieving the first feature with [0] then getting its properties.

# Now let's go through each property one by one.

for prop in properties: # We're not using property because it's a Python keyword
    print(prop)

# If we go through the list, we can see there is headline property and a description property.
# Let's print them out
print(properties['headline'])
print(properties['description'])


# Exercise: Try to print out all active alerts.
# Solution: see active_alerts.py
from requests import get
alerts = get('https://api.weather.gov/alerts?active=true').json()['features']
for alert in alerts:
    print(alert['properties']['headline'])
    print(alert['properties']['description'] + '\n')

# Exercise: Using the same API, try to make a dictionary that allows you to look up technical weather terms (in the glossary) and print out the defintion.
# Solution
from requests import get
glossary = get('https://api.weather.gov/glossary').json()['glossary']
while True:
    query = input('Enter term: ')
    try:
        print('Defintion: ' + list(filter(lambda x: x['term'] == query, glossary))[0]['definition'])
    except IndexError:
        print('Term not found.')