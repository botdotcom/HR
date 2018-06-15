'''
The purpose of this assignment is for us to understand how you design 
and develop your code using the best practices you consider important
(i.e. unit tests, automated environment setup, etc). You can use any 
language you are comfortable with(but not Microsoft Tech stack)
The attached csv file has a list of addresses and we want to geocode 
those addresses. However we only want those addresses that have a single
non-partial result and that have a geocode that is of "ROOFTOP" quality.
The geocoding should be managed using the Google geocode service:
 https://developers.google.com/maps/documentation/geocoding/
'''

''' all imports '''
import time
import requests
import pandas as pd


''' all basic configurations '''
# configuration of API key 
API_KEY = "AIzaSyAQIyAog6XR9y_ws1XrYIwUBTpLllaHuuw"      # get this from file later

# define file names for file operations
input_file = "Address_List.csv"
output_file = "Geocodes_List.csv"

# data column name in input file
column_name = "Address"

# single switch to toggle between full results from Google API
return_full_results = False


''' load data '''
input_data = pd.read_csv(input_file, encoding='utf8')

# check for validity of csv file
if column_name not in input_data.columns:
    raise ValueError("Missing column for Addresses")

addresses = input_data[column_name].tolist()    # converting pandas data to data list


''' get geocoding results from Google API '''
def get_results_from_google(address, api_key=None, full_response=False):
    '''
    @param address: String address input
    @param api_key: String API key from Google. None if not available
    @param full_response: Boolean. True if full response required from Google e.g. additional location details for storage

    In case of multiple results from Google for a single address, the first one is returned
    '''
    # geocode url formation
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(address)
    if api_key is not None:
        geocode_url = geocode_url + "&key={}".format(api_key)

    # contact Google for results in JSON
    results = requests.get(geocode_url).json()

    # check if results available
    if len(results['results']) == 0:
        result = {
            "formatted_address": None,
            "latitude" : None,
            "longitude" : None,
            "type": None
        }
    else:                  
        output = results['results'][0]
        # get only results that are of ROOFTOP quality        
        result = {
            "formatted_address" : output.get('formatted_address'),
            "latitude": output.get('geometry').get('location').get('lat'),
            "longitude": output.get('geometry').get('location').get('lng'),
            "type": output.get('geometry').get('location_type')
        }          

    # adding additional details at the end to the result, for our assessment  
    result['input_address'] = address
    result['status'] = results.get('status')
    result['no_of_results'] = len(results['results'])

    # additional code can be added at this point for full results to be returned    
    return result       # only the topmost result is being returned currently

''' process data '''
# check for proper internet access and correct API key before beginning batch geocoding
test_conn_result = get_results_from_google("Pune, India", API_KEY)
if (test_conn_result['status'] != 'OK') or (test_conn_result['formatted_address'] != "Pune, Maharashtra, India"):
    raise requests.ConnectionError("Problems testing results from Google Geocode. Either API key is wrong, or you have poor internet connection")
else:
    print("Connections tested Ok. We are ready to begin!")

# list to hold results
all_results = []

# go through each address for geocoding
for address in addresses:
    is_geocoded = False
    # all possibilities are checked and run till the address is not geocoded OR an error is thrown
    while is_geocoded is not True:
        # geocode the address
        try:
            geocode_result = get_results_from_google(address.encode('utf8'), API_KEY)
        except Exception as e:
            # display error message and move to next address in list
            print("Error occurred while geocoding: {}. Skipping it!".format(address))
            is_geocoded = True

        # if API limit reached already
        if geocode_result['status'] == 'OVER_QUERY_LIMIT':
            print("API limit reached! Going to sleep for some time...")           
            time.sleep(2 * 60)         # sleep for x*60 min, then move to next piece of code
            is_geocoded = False
        else:
            # check for other error codes i.e. add to list only if status = OK
            if geocode_result['status'] != 'OK':
                print("Error in geocoding address {} :- {}".format(address, geocode_result['status']))
            elif geocode_result['type'] == 'ROOFTOP':
                # check for ROOFTOP quality geocode only
                all_results.append(geocode_result)                               
            is_geocoded = True

    # save results after 20 conversions, so as to avoid loss in case of failure    
    if len(all_results) % 20 == 0:
        pd.DataFrame(all_results).to_csv("{}_bak".format(output_file))
        print("Completed {} of {} addresses...".format(len(all_results), len(addresses)))     # show completion status on console

print("Finished geocoding all addresses. Saving to file...")
# write results to a new CSV file using pandas
pd.DataFrame(all_results).to_csv(output_file, encoding='utf8')   
print("Done!")     