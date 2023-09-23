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

# Feature added
Cors
if long url already present in db then read from db and do not gen new short url
If short url is already present in db then keep regenerating short url until we get a unique short url in db
For non logged in user max expiry date is 30 days

## Non-functional requirements
TBD

# Python Packages installed
To Install package using poetry;-
poetry add pydantic-settings --group core

fastapi
uvicorn
cassandra-driver
gunicorn
email-validator
python-multipart

JWT Token; -
python-jose[cryptography]

Password Hashes; -
passlib[bcrypt]
