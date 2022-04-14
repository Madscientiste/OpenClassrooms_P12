# API Endpoints

## Open Endpoints

Open endpoints require no Authentication.

* [Login](/doc/login.md) : `POST /api/login/`

## Endpoints that require Authentication

Authentication is performed with the `Authorization` HTTP header in the format `Authorization: TOKEN_TYPE TOKEN`.

Example Bearer Token Authorization Header

``` json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

### Users related

**Current authenticated user must have permissions to access this endpoint.**

Viewing & Manipulating the User

* [Show All Users](/doc/users/get.md) : `GET /api/users/`
* [Create A User](/doc/users/post.md) : `POST /api/users/`
<!--  -->
* [Get a User](/doc/users/#id/get.md) : `GET /api/users/:pk/`
* [Update A User](/doc/users/#id/put.md) : `PUT /api/users/:pk/`
* [Delete A User](/doc/users/#id/delete.md) : `DELETE /api/users/:pk/`
