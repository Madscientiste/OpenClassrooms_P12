# Users Enpoint

## User Model

```cs
"id": int
"username": string
"first_name": string
"last_name": string
"email": string
*"password": string
*"password2": string
```

> ***Marked fields are write-only**

## ![](https://img.shields.io/badge/-GET%20-green) /users/

Get all users.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns an array of [user](#Users-Model)


## ![](https://img.shields.io/badge/-GET%20-green) /users/1/

Get one user.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns a [user](#Users-Model)

## ![](https://img.shields.io/badge/-POST%20-orange) /users/1/

Get one user.

**Request Body**

```cs
"username": string
"first_name": string
"last_name": string
"email": string
"password": string
"password2": string
```

> Note: All fields are **required**

### Success

**Response 200**

Returns a [user](#Users-Model)

## ![](https://img.shields.io/badge/-PATCH%20-blueviolet) /users/1/

Update one user.

**Request Body**

```cs
"username": string
"first_name": string
"last_name": string
"email": string
"password": string
```

> Note: at least **one field** must be provided

### Success

**Response 200**

Returns a [user](#Users-Model)

## ![](https://img.shields.io/badge/-DELETE%20-critical) /users/1

Update one user.

**Request Body**

```cs
Empty
```

### Success

**Response 201**

```cs
Empty
```
