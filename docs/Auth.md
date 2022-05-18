# Auth Enpoints

## ![](https://img.shields.io/badge/-POST%20-orange) /auth/token

Login a user with given credentials.

**Request Body**

```cs
"username": string,
"password": string
```

### Success

**Response 200**

```cs
"refresh": string
"access": string
```

## ![](https://img.shields.io/badge/-POST%20-orange) /auth/refresh

Refresh a user's token.

**Request Body**

```cs
"refresh": string
```

### Success

**Response 200** 

```cs
"access": string
```
