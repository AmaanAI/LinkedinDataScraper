import json

#from linkedin_api import Linkedin
from linkedinapi_MA import Linkedin
# Authenticate using any Linkedin account credentials
api = Linkedin('harrisonforf@gmail.com', 'Fordharrison@')

users = ["harrison-ford-156b"]
    #["dany-rosalie-edmond-rottiers-77068911", "laurent-chabrut-a20790121", "svrmg"]

for user in users:
    # GET a profile
    profile = api.get_profile(user)
    posts = api.get_profile_posts(user, post_count=20)
    print(profile)

    # Write the list of dictionaries to the JSON file
    with open(f"../../Output/LinkedIn_Extracts/{profile['lastName']}_profile.json", 'w') as json_file_:
        json.dump(profile, json_file_, indent=4)

    # Writing feed post data of the user
    with open(f"../../Output/LinkedIn_Extracts/{profile['lastName']}_posts.json", 'w') as json_file_:
        json.dump(posts, json_file_, indent=4)
    # GET a profiles contact info
    contact_info = api.get_profile_contact_info(user)
    #print(contact_info)

    with open(f"../../Output/LinkedIn_Extracts/{profile['lastName']}_contact_info.json", 'w') as json_file_:
        json.dump(contact_info, json_file_, indent=4)
    # # GET 1st degree connections of a given profile
    # connections = api.get_profile_connections(user)
    # with open(f"./output/{profile['lastName']}_connections.json", 'w') as json_file_:
    #     json.dump(connections, json_file_, indent=4)
    # #print(connections)