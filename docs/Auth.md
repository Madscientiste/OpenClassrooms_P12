# Auth Enpoints

## /auth/token

Login a user with given credentials.

- **Method** : POST

**Request Body**

```cs
"username": string,
"password": string
```

### Success

**Response**

```cs
"refresh": string
"access": string
```

## /auth/refresh

Refresh a user's token.

- **Method** : POST

**Request Body**

```cs
"refresh": string
```

### Success

**Response 200** 

```cs
"access": string
```
