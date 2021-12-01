import requests
import unittest
import json

# api urls
long_lat_url = "https://api.weather.gov/points/{},{}"


def test_latitude_longitude_api(latitude=39.7456, longitude=-97.0892):
    tester = unittest.TestCase()
    url = long_lat_url.format(latitude, longitude)
    print(f"Trying to hit API URL '{url}'")
    try:
        response = requests.get(url=url, verify=True)
        print("Response code received: {}".format(response))
    except requests.exceptions.Timeout:
        print("Connection to host timed out")
        assert False
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error '{e}'")
        assert False
    except Exception as e:
        print(f"An unexpected error '{e}' while hitting the URL '{url}'")
        assert False

    tester.assertTrue(response.status_code == 200, f"Failed to get 200 response from API and received response code "
                                                   f"'{response.status_code}'")

    try:
        request_response = json.loads(response.text)
        # print(f"Request Response: {request_response}")
    except Exception as e:
        print("An unexpected error '{e}' while fetching the request response")
        assert False

    properties = request_response['properties']

    # added following test assertions based on test requirements.
    tester.assertTrue(request_response['id'] == url,
                      f"The request URL '{url}' is not matched with response ID '{request_response['id']}'")
    tester.assertTrue(request_response['type'] == 'Feature',
                      f"Failed to get the expected type as 'Feature' in response type '{request_response['type']}'")
    tester.assertTrue(properties['relativeLocation']['geometry']['type'] == 'Point',
                      f"Failed to get the expected type as 'Point' in response geometry relativeLocation type "
                      f"'{request_response['type']}'")

    tester.assertIn('forecast', properties.keys(),
                    f"The key 'forecast' does not exists in response properties keys '{properties.keys()}'"),
    tester.assertIsNotNone(properties['forecast'], f"Could not find any value for forecast key in response properties")

    tester.assertIn('forecastHourly', properties.keys(),
                    f"The key 'forecastHourly' does not exists in response properties keys '{properties.keys()}'"),
    tester.assertIsNotNone(properties['forecastHourly'],
                           f"Could not find any value for forecastHourly key in response properties")

    tester.assertIn('forecastGridData', properties.keys(),
                    f"The key 'forecastGridData' does not exists in response properties keys '{properties.keys()}'"),
    tester.assertIsNotNone(properties['forecastGridData'],
                           f"Could not find any value for forecastGridData key in response properties")

    tester.assertIn('observationStations', properties.keys(),
                    f"The key 'observationStations' does not exists in response properties keys '{properties.keys()}'"),
    tester.assertIsNotNone(properties['observationStations'],
                           f"Could not find any value for observationStations key in response properties")

    tester.assertTrue(properties['relativeLocation']['properties']['city'] == 'Linn',
                      f"Failed to get the expected city as 'Linn' in response "
                      f"'{properties['relativeLocation']['properties']['city']}'")
    tester.assertTrue(properties['relativeLocation']['properties']['state'] == 'KS',
                      f"Failed to get the expected state as 'KS' in response "
                      f"'{properties['relativeLocation']['properties']['state']}'")
