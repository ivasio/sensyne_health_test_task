# Sensyne Health Test App 

Application is built using FastAPI. Models and server stubs (routers) were generated
from the specification using https://github.com/koxudaxi/fastapi-code-generator

## Requirements
- docker-compose

The application can be run locally using ```docker-compose up```

## Tests

All tests passed except for Get/Update/Delete non-existent reading - by default FastAPI 
returns ```422 Unprocessable Entity``` for malformed requests (in these test cases 
```unknown-reading-uuid``` is actually not a valid UUID)

Tested using ```newman``` CLI tool
