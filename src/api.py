# Make sure to download the requests library before running program
import requests

# Example usage: get_data("api/races/gnome")
def get_data(endpoint) :
    ''' Wrapper function to grab data from the dnd5e API. Returns data as JSON using REST format '''

    api = "http://www.dnd5eapi.co/"
    api += endpoint
    response = requests.get(api)
    response.raise_for_status()
    return response.json()