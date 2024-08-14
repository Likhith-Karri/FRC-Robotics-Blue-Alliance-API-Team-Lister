"""
Author: Sai Likhith Karri
Description: Utilized The Blue Alliance API To Get A List Of 
Teams Present During A Specific FRC Match & Event, Alongside
Several Other Functionalities. 

"""

import requests

# My API Key
apiKey = "gObylt24UUMcLdGboGWoggAaib9EWEFzGwzCehrtp75WwxN8thhvuTupnWc1fwqY"

headers={'X-TBA-Auth-Key': apiKey}

# Having The User Enter A Team 
teamNumber = input("Enter The Team Number: ")


# The Base URL For The TBA API
baseURL = 'https://www.thebluealliance.com/api/v3'

eventsEndpoint = f'/team/frc{teamNumber}/events/2023/simple'

teamsEndpoint = '/event/EVENT_KEY/teams/simple'


events_response = requests.get(baseURL + eventsEndpoint, headers)
events = events_response.json()


# Going Through The Events And Added Each Unique Team
uniqueTeams = set()

for event in events:
    # Getting The Event Key - Used To Update The Event
    eventKey = event['key']

    # Grabbing The List Of Teams From The Event
    teams_response = requests.get(baseURL + teamsEndpoint.replace('EVENT_KEY', eventKey), headers)
    teams = teams_response.json()

    # Extracting The Team Numbers From The Event And Storing Them
    uniqueTeams.update(team['team_number'] for team in teams)

uniqueCountries = set()
uniqueStatesProvinces = set()
uniqueCities = set()

for team in uniqueTeams:
  url = f'https://www.thebluealliance.com/api/v3/team/frc{team}/simple'
  response = requests.get(url, headers)
  teamData = response.json()

  # Extract country, state, and city information
  uniqueCountries.add(teamData.get('country'))
  uniqueStatesProvinces.add(teamData.get('state_prov'))
  uniqueCities.add(teamData.get('city'))
  
# Displaying The Unique Team Numbers, Countrues, States / Provinces, and Cities
print("\nUnique Teams:")
for team in uniqueTeams:
    print(f"{team}")

print("\nUnique Countries:")
for country in uniqueCountries:
    print(f"{country}")

print("\nUnique States / Provinces:")
for state in uniqueStatesProvinces:
    print(f"{state}")

print("\nUnique Cities:")
for city in uniqueCities:
    print(f"{city}")