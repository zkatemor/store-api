# Microservice for an electronic store

## Technology
- Python3
- Flask
- MongoDB

## How to

1. Running MongoDB as a Docker container.

        sudo docker run -d -p 27017:27017 mongo
2. Starting a project from IDE. Create .env file by example.
    
        virtualenv venv
        
        source venv/bin/activate
        
        pip install -r requirements.txt
        
        python manage.py runserver

## API Documentation

### Create product

`POST` /product

**Body (json)**

- *name* (string) is required
- *description* (string) is required
- *params* (list of dict) is required

**Example:**
```json
{
    "name": "Microwave",
    "description": "The best of the best",
    "params": [
        {"Size": "S"}
    ]
}
```

**Response**

- `422 Unprocessable Entity` 

```json
{
    "error": {
        "message": "The browser (or proxy) sent a request that this server could not understand."
    }
}
```

- `201 OK` 

```json
{
    "successful": {
        "id": "5fb6d5fe66e8d01c77a6e0a2"
    }
}
```

### Get a list of product names, with the ability to filter

`GET` /product

**Body (json)**

- *name* (string) is not required
- *params* (list of dict) is not required

**Example:**
```json
{
    "name": "Microwave",
    "params": [
        {"Size": "S"}
    ]
}
```

or

```json
{
    "name": "Microwave"
}
```

or with empty body (return all products)

**Response**

- `422 Unprocessable Entity` 

```json
{
    "error": {
        "message": "The browser (or proxy) sent a request that this server could not understand."
    }
}
```

- `200 OK` 

```json
{
    "result": [
        {
            "id": "5fb6d5fe66e8d01c77a6e0a2",
            "name": "Microwave"
        },
        {
            "id": "5fb6d73766e8d01c77a6e0a3",
            "name": "TV set"
        }
    ]
}
```

### Get product details by ID

`GET` /product/:id

**Body (in path)**

- *id* (string) is required

**Response**

- `404 Not Found` 

```json
{
    "error": {
        "message": "not found"
    }
}
```

- `200 OK` 

```json
{
    "result": {
        "name": "Microwave",
        "description": "The best of the best",
        "params": [
            {
                "Size": "M"
            }
        ]
    }
}
```