# Clean Architecture using FastApi

This is a simple approach to implement Clean Architecture using FastApi.
This guide is based on the following articles:

- [Designing APIs with Clean Architecture](https://theprodev.medium.com/desgining-apis-with-clean-architecture-2fedff1b79cb)
- [FastAPI Clean Architecture](https://medium.com/@YDyachenko/fastapi-clean-architecture-4c961b512213)
- [Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [fastapi-clean-example](https://github.com/0xTheProDev/fastapi-clean-example)

This example showcases Repository Pattern in Hexagonal Architecture (also known as Clean Architecture).

## Project Structure

```
project/
├── configs/
├── metadata/
├── models/
├── repositories/
├── routers/
├── schemas/
├── services/
└── main.py
```

**Explanation :star:**

- `configs`: Contains all the configuration files.
    - `Database.py`: Contains the database configuration.
    - `Environment.py`: Contains the environment variables.
    - `GraphQL.py`: Contains the GraphQL configuration.
- `metadata`: Contains the metadata files.
    - `Tags.py`: Contains the tags for the API. The description of each one module is in the file.
- `models`: Contains the models of the application. These models are used to interact with the database, contains the
  ORM. Each class define a table in the database.
    - `BaseModel.py`: Contains the base model of the application.
    - `UserModel.py`: Contains the user model of the application.
- `repositories`: Contains the repositories of the application. These repositories are used to interact with the
  database, contains the queries. Each class define a table in the database.
    - `UserRepository.py`: Contains the user repository of the application.
- `routers`: Contains the routers of the application. These routers are used to define the endpoints of the API. Each
  endpoint y organized in modules that contains the version of the API.
    - `v1`: Contains the version 1 of the API.
        - `UserRouter.py`: Contains the user router of the application.
- `schemas`: Contains the schemas of the application. These schemas are used to define the request and response of the
  API.
    - `pydantic`: Here is located all the schemas used in the app using the pydantic library.
        - `UserSchema.py`: Contains the user schema of the application.
    - `graphql`: Here is located all the schemas used in the app using the graphql library.
        - `User.py` Contains the author graphql schema of the application.
        - `Query.py` Contains the query graphql schema of the application.
        - `Mutation.py` Contains the mutation graphql schema of the application.
- `services`: Contains the services of the application. These services are used to define the business logic of the API.
  Each service require the repository of the model.
    - `UserService.py`: Contains the user service of the application.
- `main.py`: Contains the main file of the application. This file is used to run the API.