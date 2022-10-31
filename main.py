# Kaitlyn O'Flaherty
# Broad Institute of MIT and Harvard
# 26 October 2022
# Filename: main.py
# Description: Broad DSP Engineering Interview Take-Home

# Import requests library
import requests

# Get MBTA routes, stop data from type 1 and 0, 'Heavy Rail' and 'Light Rail'
# Returns a requests.Response object
r = requests.get('https://api-v3.mbta.com/routes?filter[type]=0,1')
s = requests.get('https://api-v3.mbta.com/stops?filter[route_type]=0,1&include=route')


def get_data(x):
    """ Function to convert to JSON Object
    Params: x - request object
    Returns: x.json(), JSON Object """
    return x.json()


def get_attribute(data, attribute):
    """ Function to find a specific attribute from a JSON object
    Params: data - JSON object
    Returns: lines - list of long names """
    # Initialize empty list
    attribute_list = []

    # Loop through the value of 'data' key - list of attributes
    for i in range(len(data['data'])):
        # Iterate through each set of attributes
        new_data = data['data'][i]

        # Append each attribute to list
        attribute_list.append(new_data['attributes'][attribute])

    return attribute_list


def get_stops_lines(data):
    """Function to get list of stops for
    Params: data - JSON object
    Returns: stops_lines - list of the name of each line at each stop
    Note: I was not able to use another technique to solve this problem, so I
    used the line name from the description. Inconsistencies in formatting prevented
    me from getting the correct numbers, and I know this is not the most efficient solution."""
    # Initialize empty lists
    stops_lines = []

    # Add all instances of each line to a list
    for i in range(len(data['data'])):
        new_data = data['data'][i]
        desc = new_data['attributes']['description']
        line = desc.strip().split('-')
        stops_lines.append(line[1])

    return stops_lines


def most_frequent(L):
    """Function to find most frequent element in a list
    Params: L - list
    Returns: most_freq - most frequent element in L"""
    count = 0
    most_freq = L[0]

    for i in L:
        curr_freq = L.count(i)
        if curr_freq > count:
            count = curr_freq
            most_freq = i

    num = L.count(most_freq)

    return most_freq, num


def least_frequent(L):
    """Function to find the least frequent element in a list
    Params: L - list
    Returns: least_freq - the least frequent element in L
    Note: Due to inconsistent spacing of the names in my list (line_stops),
    the incorrect number is printed."""

    count = 10000
    least_freq = L[0]

    for i in L:
        least = L.count(i)
        if least <= count:
            count = least
            least_freq = i

    num = L.count(least_freq)
    return least_freq, num


def main():
    # Convert response objects to JSON
    routes = get_data(r)
    stops = get_data(s)

    # Question 1: Print long names
    lines = get_attribute(routes, 'long_name')
    print(*lines, sep=', ')

    # Question 2: Find most and least stops
    list_stops = get_stops_lines(stops)
    most_stops, num = most_frequent(list_stops)
    least_stops, num2 = least_frequent(list_stops)

    print('The line with the most stops is', most_stops, 'with ', num, ' total stops.')
    print('The line with the least stops is', least_stops, 'with ', num2, ' total stops.')


if __name__ == "__main__":
    main()