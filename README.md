# Project Name

_Ami Coding Pari Na_

## About

Your project has contain 3 sections

- Section 1: User Authentication/Registration Page
- Section 2: Khoj the search Page
- Section 3: API Endpoints

## Tools used in this project

- python3,
- django,
- django_rest_framework
- postgreSQL,
- Docker
- git

## Installation

### App to install before running this project

- Docker

```json
$ git clone https://github.com/nuruddinsayeed/ami-code-parina-project.git
$ cd (enter the downloaded directory)
$ docker build .
$ docker-compose build
$ docker-compose up
```

## Project Detail:

_If Poject setup is successfull, then you can follow the steps bellw_

### Video Link:

<p align="center">
  <a href="https://youtu.be/TbacbAHp7H8"><img src="https://github.com/nuruddinsayeed/ami-code-parina-project/blob/main/zzzz.png" width="290"></a>
</p>

## Section One (Authentication/Registration Page):

```json
Login URL: http://127.0.0.1:8000/user/login/
Registration URL: http://127.0.0.1:8000/user/login/
```

After login user will be directed to home page

```json
http://127.0.0.1:8000/
```

### Section One - API (API Token Authentications)

#### Create User API endpoint:

```json
http://127.0.0.1:8000/api/user/create/
```

#### Create User Token endpoint:

```json
http://127.0.0.1:8000/api/user/token/
```

#### User Profile Update endpoint with token based authentication:

_For that user needs to send a token through header section of the request. We can achieve this by adding an extension to chrome called HeaderMod. [Get HeaderMod From here](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en)_

```json
http://127.0.0.1:8000/api/user/profile/
```

## Section Two (Khoj the search Page):

After login, users can access this page.

In this page there is a form that:

- Takes the “Input Values”
- Takes the “Search Value”
- Sort the “Input values” in descending order.
- Store the sorted “Input Values” in the database.
- Check if the “Search Value” is in the “Input Values”
- Print the output

```json
http://127.0.0.1:8000/
```

## Section Three (API Endpoint):

### Endpoint 1: Get All Input Values

This endpoint takes Three Parameters: start_datetime, end_datetime, user_id

sample endpoint with parameters:

```json
http://127.0.0.1:8000/api/input-values?format=api&user_id=1&start_datetime=2020-09-24T19:58:23.332624Z&end_datetime=2022-09-24T21:29:28.865268Z
```

Here,

- user_id = 1
- start_datetime = 2020-09-24T19:58:23.332624Z
- end_datetime = 2022-09-24T21:29:28.865268Z

sample response:

```json
{
    “status”: “succes”,
    “user_id” : 1,
    “payload” : [
        {
            “timestamp” : ”2020-12-24T19:58:23.332624Z”,
            “input_values” : “11, 10, 9, 7, 5, 1, 0”
        },
        {
            “timestamp” : ”2022-01-24T21:29:28.865268Z”,
            “input_values” : “13, 11, 10, 7, 5, 2, 1”
    ]
}
```

## License

This project is released under [MITlicense](https://www.mit.edu/~amini/LICENSE.md)
