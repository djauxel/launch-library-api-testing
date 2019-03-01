import json
import urllib2

launch_api = 'https://launchlibrary.net/1.4/launch/next/15'

url = launch_api
response = urllib2.urlopen(url)
json_data = json.loads(response.read())

# Print the API URL
print('\nAPI URL: ' + url)

# The next 15 launches
launch_count = json_data['count']
print('Launch Count: ' + str(launch_count))

# Get "launches" object
launch_list = json_data['launches']

# Launch Information
for i in range(0, launch_count):

    for j in range(0, 50):
        print '=',

    print('\nLAUNCH INFORMATION')

    # Order of launch
    print('\nLaunch Sequence: ' + str(i + 1))

    # The name of the rocket
    rocket_name = launch_list[i]['name']
    print('Rocket Name: ' + rocket_name)

    # The estimated launch time
    launch_net = launch_list[i]['net']
    print('NET: ' + launch_net) # NET = "No Earlier Than"

    # The probobility of the launch occuring
    # If launch_probability == -1, then the probability is
    # unknown to us.
    # If launch_probability != -1, then the probability will
    # be displayed.
    launch_probability = launch_list[i]['probability']
    if launch_probability == -1:
        print('Launch Probability: Unknown')
    else:
        print('Launch Probability: ' + str(launch_probability) + '%')

    # Check if the time is accurate.
    # If tbd_time = 0, then we're 100% sure on the time.
    # If tbd_time = 1, then we're not 100% sure on the time.
    tbd_time = launch_list[i]['tbdtime']
    if tbd_time == 0:
        print('Time Accuracy: We\'re 100% sure on the time')
    elif tbd_time == 1:
        print('Time Accuracy: We\'re not 100% sure on the time')
    else:
        print('Time Accuracy: Couldn\t interpret tbd_time')

    # Check if the date is accurate.
    # If tbd_date = 0, then we're 100% sure on the time.
    # If tbd_date = 1, then we're not 100% sure on the time.
    tbd_date = launch_list[i]['tbddate']
    if tbd_date == 0:
        print('Date Accuracy: We\'re 100% sure on the date')
    elif tbd_date == 1:
        print('Date Accuracy: We\'re not 100% sure on the date')
    else:
        print('Date Accuracy: Couldn\t interpret tbd_date')

    # Check if the video url array is empty.
    # If it's not empty, it will print the video URL.
    if len(launch_list[i]['vidURLs']) != 0:
        video_url = launch_list[i]['vidURLs'][0]
        print('Video URL: ' + video_url)

    # Check for a hold reason if there is one.
    # If there is no hold, display "Null".
    hold_reason = launch_list[i]['holdreason']
    if not hold_reason:
        print('Hold Reason: Null')
    if hold_reason:
        print('Hold Reason: ' + hold_reason)

    # Check for fail reason if tehre is one.
    # If there is no fail, display "Null".
    fail_reason = launch_list[i]['failreason']
    if not fail_reason:
        print('Fail Reason: Null')
    if fail_reason:
        print('Fail Reason: ' + fail_reason)

    # Launch location
    launch_location = launch_list[i]['location']['name']
    print('Launch Location: ' + launch_location)

    # Check if the launch pad is determined.
    # If it is determined, print the pad information
    if len(launch_list[i]['location']['pads']) != 0:
        pad_name = launch_list[i]['location']['pads'][0]['name']
        pad_wiki_url = launch_list[i]['location']['pads'][0]['wikiURL']
        pad_map_url = launch_list[i]['location']['pads'][0]['mapURL']
        pad_latitude = launch_list[i]['location']['pads'][0]['latitude']
        pad_longitude = launch_list[i]['location']['pads'][0]['longitude']
        print('Pad Name: ' + pad_name)
        print('Pad Wiki URL: ' + pad_wiki_url)
        print('Pad Google Maps URL: ' + pad_map_url)
        print('Pad Latitude: ' + str(pad_latitude))
        print('Pad Longitude: ' + str(pad_longitude))
    else:
        print('Launch Pad: Indetermined')

    # TODO: Print the launch_list[i]['rocket']
    #       and launch_list[i]['missions'] information

    print('\nROCKET INFORMATION')
    
    # The name of the rocket
    print('\nRocket Name: ' + rocket_name)

    # The rocket's configuration
    rocket_config = launch_list[i]['rocket']['configuration']
    print('Rocket Config: ' + rocket_config)

    # The rocket's family name
    rocket_family = launch_list[i]['rocket']['familyname']
    print('Rocket Family: ' + rocket_family)

    # The rocket's wiki URL
    rocket_wiki_url = launch_list[i]['rocket']['wikiURL']
    print('Wiki URL: ' + rocket_wiki_url)

    # The image URL of the rocket
    rocket_image_url = launch_list[i]['rocket']['imageURL']
    print('Rocket Image URL: ' + rocket_image_url)

    # The image sizes array
    image_sizes_array = launch_list[i]['rocket']['imageSizes']
    print('Image Sizes Array: ' + str(image_sizes_array))

    # The size of the "imageSizes" array
    image_sizes_length = len(image_sizes_array)
    print('Image Sizes Length: ' + str(image_sizes_length))

    print('\nMISSION INFORMATION')

    # If the "missions" array size is not 0, it'll 
    # print the mission information.
    # If the "missions" array size is 0, there 
    # is no mission information available.
    if len(launch_list[i]['missions']) != 0:

        # The mission name
        mission_name = launch_list[i]['missions'][0]['name']
        print('\nMission Name: ' + mission_name)

        # The mission description
        mission_description = launch_list[i]['missions'][0]['description']
        print('Mission Description: ' + mission_description)

        # The mission type
        mission_type = launch_list[i]['missions'][0]['typeName']
        if not mission_type:
            print('Mission Type: Null')
        if mission_type:
            print('Mission Type: ' + mission_type)
        
    else:
        print('Mission Name: No mission information available')

    print('\nLAUNCH SERVICE PROVIDER INFORMATION')

    # The LSP name
    lsp_name = launch_list[i]['lsp']['name']
    print('\nLSP Name: ' + lsp_name)

    # The LSP abbreviation
    lsp_abbrev = launch_list[i]['lsp']['abbrev']
    print('LSP Abbrev: ' + lsp_abbrev)

    # The LSP country code
    lsp_country_code = launch_list[i]['lsp']['countryCode']
    print('LSP Country Code: ' + lsp_country_code)

    # The LSP wiki URL
    lsp_wiki_url = launch_list[i]['lsp']['wikiURL']
    print('LSP Wiki URL: ' + lsp_wiki_url)

    print('\n')