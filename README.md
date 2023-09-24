<a name="readme-top"></a>

<!-- [![Contributors][contributors-shield]][contributors-url] -->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/vyavasthita/tiny-url">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Url Shortner</h3>
</div>

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

# About the project
This project generates short url for long url.

Details:
* This project has been implemented using Python and FastAPI web framework.

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

## Built With

Softwares/libraries used in this project.

* [![Python][Python]][Python-url]
* [![Docker][Docker]][Docker-url]
* [![DockerCompose][DockerCompose]][Docker-Compose-url]
* [![Makefile][Makefile]][Makefile-url]

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

## :hammer: Testing
### System Environment
- OS - Ubuntu 22.04
- Docker Compose version v2.17.3
- Docker version 23.0.6
- GNU Make 4.3
- Datastax DSE Cassandra 6.0.2
- Python 3.10

### Assumptions
- TBD.

### Scope
- Tested with docker environment only on Ubuntu 22.04 LTS host system.
- Tested with Fastapi swagger documentation only.
- Tested auth flow with chrome browser only.

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

### :pencil: Notes
TBD

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

### Validations done
TBD

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>


# Feature added
- Cors
- Redis Cache
- If long url already present in db then read from db and do not gen new short url
- If short url is already present in db then keep regenerating short url until we get a unique short url in db
- For non logged in user max expiry date is less than logged in users.
- Redirection: Given a short link, our system should be able to redirect the user to the original URL.

## Design Goals
### Multiple build environments
An application should support multiple build environments which should be completely independent to each other.

I have added support for multiple build environments.
- development
- qa
- production

We can switch between multiple environment sjust by exporting an environment variable. It's so easy.

  ```
  export BUILD_ENV development
  ```
  or
  ```
  export BUILD_ENV qa
  ```
  or
  ```
  export BUILD_ENV production
  ```
<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

### Independent Components
Application should be divided into multiple small components which do one particular task.
This application is divided into few small components.

1. **Auth**
  - Authenticates using Oauth2 password flow.

2. **dao**
  - Data Access Layer.
  - All communication to database happens through this layer.

3. **service**
  - All business logic.
  - All communication to database happens through this layer.

4. **utils**
  - Utility functions common to all other modules.

5. **config**
  - Reads configuration data which is shared across application.

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

### Simplicity
- Source code and Database table structure should be less complex or say should be simple to understand.
- I have followed all possible best practices to make code structure simple.

### Design Patterns
- Single Responsibility design pattern of SOLID principle is followed.
- Each class does one thing only.
- Singletone design pattern is followed for python logging.

### Flexible
- Ability of the application to adapt and evolve to accommodate new requirements without affecting the existing operations. 
- This application is modularized into small python modules which allow us to add new requirements or modify existing ones.

### Readable and Understandable
- Software is meant for modification/improvements. Fellow developers should be able to understand the code.

- This could be achieved by
    • Coding guidelines.
    • Comments/Description of classes and methods used.
    • Documentation (Doc string comments in Python), README document.

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>


## :art: Best Practices
#### :white_check_mark: Use of Makefile to ease running various commands
#### :white_check_mark: Docker with docker compose used
#### :white_check_mark: Different configurations for differnent environments like Dev, test, QA, Production
#### :white_check_mark: Manual steps are minimal while testing the app. Make file and docker compose help us in achieving this
#### :white_check_mark: Proper directory and file structure of source code
#### :white_check_mark: Applicationi is modularized into small logical components.
#### :white_check_mark: Use of decorators, dataclasses
#### :white_check_mark: Use of environment variables
#### :white_check_mark: Poetry for managing different run environments
#### :white_check_mark: Python Logging - Console and File with proper log level
#### :white_check_mark: Use of exception handling
#### :white_check_mark: Unit tests with coverage report
#### :white_check_mark: Proper git commit messages. Every commit is done post completing a functionality
#### :white_check_mark: Pep8 naming convention for modules, classes, methods, functions and variables
#### :white_check_mark: Comments added wherever required
#### :white_check_mark: Import statements are in order
Python core -> Third party -> Application modules
#### :white_check_mark: Detailed README file

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

## Issues and Limitations
  1. TBD

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

## :large_orange_diamond: Technical Details

### Python Packages
```
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
fastapi-cache2
redis
```
<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

### DB Schema

```
CREATE TABLE IF NOT EXISTS {1}.user(
    first_name text,
    last_name text,
    email text PRIMARY KEY,
    password text
)

create_url_table = """
    CREATE TABLE IF NOT EXISTS {keyspace}.url(
        long_url text,
        short_url text PRIMARY KEY,
        email text,
        expiry_date date,
        is_active boolean
)
```
<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

### Source Code Folder Structure

```bash
TBD
```
<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- Getting Started -->
# 	:toolbox: Getting Started

This projects supports multiple build environments.
1. Development
2. QA
3. Production

Follow below steps to install the app.

<!-- Prerequisites -->
## :bangbang: Prerequisites

1. Docker must be installed
2. Docker compose must be installed
3. Git Version Control
4. GNU Make

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- Installation -->
## :gear: Installation

Install my-project with npm

1. Clone the repo
   ```sh
   git clone https://github.com/vyavasthita/tiny-url.git
   ```

2. Go to root directory 'tiny-url'.
   ```sh
   cd tiny-url
   ```

3. Checkout master branch
   ```sh
   git checkout master
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Choose one the below build environments for testing;-
Steps are similar for all the environments.

## :gem: Development Build Environment
<!-- Env Variables -->
### :key: Environment Variables and Configuration

To run this project, you need to configure environment variables and configuration files

1. Set BUILD_ENV
   Set following environment variable.
   ```sh
   export BUILD_ENV=development
   ```
   #### :pencil: Default build environment is 'development' and hence if we do not set BUILD_ENV variable, we will be treated in development environment.

2. Go to directory 'app/configuration/development'
   ```sh
   cd app/configuration/development
   ```
<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

3. Create .env files
    In this directory you will find two sample env files named '.env.app.sample' and '.env.test.sample'.

    From these two sample files we need to create two .env files

    a) .env.app
    This is used when running our application
    
    Rename '.env.app.sample' to '.env.app'.
    ```sh
    mv .env.app.sample .env.app
    ```

    b) .env.test
    This is used when running unit tests

    Rename '.env.test.sample' to '.env.test'.
    ```sh
    mv .env.test.sample .env.test
    ```

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

4. Update .env files
  - Update '.env.app' 
  - Update '.env.test' 

<p align="right">(<a href="#readme-top">back to top</a>)</p>
   
<!-- Run -->
### :running: Start Containers

Now you are ready to start the application

1. Go back to project root directory 'tiny-url'.
   
   ```sh
   cd ../../..
   ```

2. Start containers

```bash
  make all
```

This will start 4 docker containers.
- Python App
- Cassandra DB
- Cassandra Studio DB
- Redis DB

Go to following URL to see mysql database tables and data.

```bash
  http://127.0.0.1:9091/
```

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>
    
<!-- Usage -->
### :eyes: Usage
#### Create Users
TBD

##### 2. Auth 
###### :pencil: This is an optional step. 

TBD

##### 3. Url
###### :pencil:

TBD

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- Running Tests -->
### :test_tube: Running Tests

To run tests, run the following command

```bash
  make test
```

### :pencil:
TBD

```bash
make testv
```
<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- Tests Coverage -->
### :test_tube: Unit Test Coverage

To run tests, run the following command

```bash
  make testcov
```
<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- Stop containers -->
### :test_tube: Stop Containers

To stop all running containers, run the following command

```bash
  make stop
```

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- Clean containers -->
### :test_tube: Clean Containers

To clean all running containers, run the following command

```bash
  make clean
```

It will run following commands
	docker network prune -f
	docker container prune -f
	docker image prune -f

Note: Be careful before you clean containers

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

## :gem: QA Build Environment
- To run project in QA environment, you need to configure environment variables and configuration files

- Steps are similar to development environment mentioned above.
Only thing to be done is update the configuration for qa environment in below path.

```
app/configuration/qa
```
- Update .env.app and .env.qa as done in development environment

- Set BUILD_ENV
   Set following environment variable.
   ```sh
   export BUILD_ENV=qa
   ```
   #### :pencil: Default build environment is 'development' and hence if we do not set BUILD_ENV variable, we will be treated in development environment.

Other installation steps are similar to development environment mentioned above.

#### :eyes: Usage
##### Starting Application

Steps to start the application are same as development environment.

## :gem: production Build Environment
- To run project in production environment, you need to configure environment variables and configuration files

- Steps are similar to development environment mentioned above.
Only thing to be done is update the configuration for production environment in below path.

```
app/configuration/production
```

- Update .env.app and .env.qa as done in development environment

- Set BUILD_ENV
   Set following environment variable.
   ```sh
   export BUILD_ENV=production
   ```
   #### :pencil: Default build environment is 'development' and hence if we do not set BUILD_ENV variable, we will be treated in development environment.

Other installation steps are similar to development environment mentioned above.

#### :eyes: Usage
##### Starting Application

Steps to start the application are same as development environment.

<!-- Deployment -->
# :triangular_flag_on_post: Deployment

TBD

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- Roadmap -->
# :compass: Roadmap

It has some limitations;-
- [ ] TBD

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- Contributing -->
## :wave: Contributing

<a href="https://github.com/vyavasthita/grhakarya/graphs/contributors">
  Contribution
</a>

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- Code of Conduct -->
### :scroll: Code of Conduct

TBD

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/badge/-contributors-red?logo=github&logoColor=white&style=for-the-badge
[contributors-url]: https://github.com/vyavasthita/grhakarya/graphs/contributors
[forks-shield]: https://img.shields.io/badge/-forks-pink?logo=github&logoColor=white&style=for-the-badge
[forks-url]: https://github.com/vyavasthita/tiny-url/network/members
[stars-shield]: https://img.shields.io/badge/-stars-yellow?logo=github&logoColor=white&style=for-the-badge
[stars-url]: https://github.com/vyavasthita/tiny-url/stargazers
[license-shield]: https://img.shields.io/badge/-license-blue?logo=license&logoColor=white&style=for-the-badge
[license-url]: https://github.com/vyavasthita/tiny-url/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/diliplakshya/
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Docker]: https://img.shields.io/badge/Docker-4A4A55?style=for-the-badge&logo=docker&logoColor=FF3E00
[Docker-url]: https://www.docker.com/
[linkedin-url]: https://www.linkedin.com/in/diliplakshya/
[DockerCompose]: https://img.shields.io/badge/-Docker%20Compose-blue?logo=docker&logoColor=white&style=for-the-badge
[Docker-Compose-url]: https://docs.docker.com/compose/
[Makefile]: https://img.shields.io/badge/-makefile-red?logo=gnu&logoColor=white&style=for-the-badge
[Makefile-url]: https://www.gnu.org/software/make/
