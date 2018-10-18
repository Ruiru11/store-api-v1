# Store-api-v1
> An application programming interface.
> To be used by Front End pages

[![Build Status](https://travis-ci.org/Ruiru11/store-api-v1.svg?branch=develop)](https://travis-ci.org/Ruiru11/store-api-v1) [![Coverage Status](https://coveralls.io/repos/github/Ruiru11/store-api-v1/badge.svg?branch=develop)](https://coveralls.io/github/Ruiru11/store-api-v1?branch=develop)

## HELPS MANAGE CRUD OPERATIONS

## Installation:
. Navigate to where you want to install the project
. In your terminal:
. git clone `https://github.com/Ruiru11/store-api-v1.git`
. Navigate into into the created folder 
. git init 

#### create a virtualenv environment 

OS X & Linux:

```sh
pip install -r requirements.txt
```

Windows:

```sh
pip install -r requirements.txt
```

## HOW TO USE THE APPLICATION

. 	Available  Endpoints

> ```POST/api/v1/products```
. Used to create a new product for the store (Only accessible to admin)
#### payload
```
{
       "name":"steel",
       "price":"sh.825",
       "category":"construction",
       "description":"Y16-For Columns and Slab"
}
```

> ```POST/api/v1/sales```
. Used to create a new sale order (accessible by store attendants)
#### payload
```
{
        "name": "Jone Doe",
        "description": "['oil-paint','wood','nails','T.cost=3000']"
}
```

> ```POST/api/v1/signup```
. Used to create users
#### payload
```
{
        "username": "Kristine Camil",
        "password": "password",
         "email": "camil@new.com",
         "role": "attendant"
}
```

#### The rest of the enpoints
> ```POST/api/v1/signin```
. Used to signin a user

 > ```GET/api/v1/products```
 . Used to get all products(accessible to admin and attendants)

> ```GET/api/v1/products/<int:id>```
. Used to get a single product created (accessible to both admin and attendants)

> ```GET/api/v1/sales``` 
. Used to get all sale orders (only  accesible to admin)

> ```GET/api/v1/sales/<int:id>```
. Used to get a single sale order (accessible only to admin and attendant who created the orders)

## How should this be manually tested?

#### After cloning the repo locally run python run.py
. Using postman to test the above endpoints using the below headers

##### key Content-Type →application/json
##### Key Authorization → Token

## Running the tests


```
  pytest --cov=app tests
```