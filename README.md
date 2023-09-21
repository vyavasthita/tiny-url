# tiny-url
Url Shortner

# To Do
Caching - Redis

create( long_url, api_key, custom_url)

POST
Tinyrl : POST : https://tinyurl.com/app/api/create
Request Body: {url=long_url}
Return OK (200), with the generated short_url in data

# DB Model
# User (Optional)
    user_id
    email_id
    name
    password

# Shortner
    # long_url
    # short_url
    # creation_date
    # expiry_date
    # user_id

Redirection: Given a short link, our system should be able to redirect the user to the original URL.


## Non-functional requirements
TBD

# Python Packages installed
fastapi
uvicorn
cassandra-driver
