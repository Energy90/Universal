import requests


def getPercentage(querystring):
    ''' get the percentage '''
    
    url = "https://love-calculator.p.rapidapi.com/getPercentage"
    headers = {
        'x-rapidapi-host': "love-calculator.p.rapidapi.com",
        'x-rapidapi-key': "7e7d7618dcmshbc7b50e502a67eep118368jsna05f35e2ad19"
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()
    except requests.RequestException:
        return None

    try:
        love = response.json()
        return {
            "fname": love["fname"],
            "sname": love["sname"],
            "percentage" : love["percentage"],
            "result": love["result"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def get_allcountries():
    ''' get all countries '''

    url = "https://world-population.p.rapidapi.com/allcountriesname"

    headers = {
        'x-rapidapi-host': "world-population.p.rapidapi.com",
        'x-rapidapi-key': "7e7d7618dcmshbc7b50e502a67eep118368jsna05f35e2ad19"
    }
    try:
        response = requests.request("GET", url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        return None

    try:
        countries = response.json()
        return {"all_countries": countries["body"]["countries"]}
    except (KeyError, TypeError, ValueError):
        return None


def get_country_population(querystring):
    ''' get country population '''

    url = "https://world-population.p.rapidapi.com/population"

    headers = {
        'x-rapidapi-host': "world-population.p.rapidapi.com",
        'x-rapidapi-key': "7e7d7618dcmshbc7b50e502a67eep118368jsna05f35e2ad19"
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()
    except requests.RequestException:
        return None

    try:
        country = response.json()
        return {
            "country_name": country['body']['country_name'],
            "population": country['body']['population'],
            "ranking": country['body']['ranking'],
            "world_share": country['body']['world_share']

        }
    except (KeyError, TypeError, ValueError):
        return None


def get_world_population():
    ''' get world population '''
    url = "https://world-population.p.rapidapi.com/worldpopulation"

    headers = {
        'x-rapidapi-host': "world-population.p.rapidapi.com",
        'x-rapidapi-key': "7e7d7618dcmshbc7b50e502a67eep118368jsna05f35e2ad19"
    }
    try:
        response = requests.request("GET", url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        return None

    try:
        population = response.json()
        return { 
            "world_population": population["body"]["world_population"],
            "total_countries": population["body"]["total_countries"]
        }
    except (KeyError, TypeError, ValueError):
        return None

def get_jokes():
    ''' get jokes '''

    url = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "7e7d7618dcmshbc7b50e502a67eep118368jsna05f35e2ad19"
    }
    try:
        response = requests.request("GET", url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        return None

    try:
        joke = response.json()
        return {
            "joke": joke["content"]

        }
    except (KeyError, TypeError, ValueError):
        return None