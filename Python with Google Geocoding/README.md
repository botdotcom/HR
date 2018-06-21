## Address to Geocoding using Google API

#### Input
* `address_to_geocode_converter.py` is the program that fetches geocodes for the batch of addresses.
* `Address_List.csv` contains the batch of addresses that need converting to geocodes
* `config.txt` is the file where you store your API key.

#### Output
* The output of this project are 2 CSV files containing geocoding results.
* `Geocodes_List.csv` will contain the final results.
* `Geocodes_List.csv_bak` is the backup file where the results are stored after certain intervals of the runtime of the program.

#### Previous Results
This folder contains all the results from previous runtimes of the program, numbered as per the sequence of their generation, for reference purpose.

#### Considerations
* You will not find any test case file written for this code as the only testing required is for internet connection and validity of API key
* Both these have been tested at the start of runtime of this program. The program doesn't move forward without this.

#### Observations
* During previous runs of the program, it has been observed that some addresses, though being tagged as ROOFTOP quality by Google do not necessarily give accurate results.
* This is evident in, for example, where the location input was in North Dakota (ND), USA but was instead geocoded in South Carolina (SC), USA. A few were even shown in Western Australia instead of Washington (WA), USA.
* This inaccuracy is on the part of the [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/start). To reduce this error, another parameter has been added to the request URL, restricting search region to USA.

#### Usage
Run the program by putting the following command in terminal/CMD of a machine with Python 2.7+ installed:
`$ python address_to_geocode_converter.py`
