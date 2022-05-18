# Client Enpoints

## Client Model

```cs
"id": int,
"sales_contact": int
"first_name": string,
"last_name": string,
"email": string,
"is_validated": bool,
"phone": string,
"mobile": string,
"company_name": string,
"date_created": date,
"date_updated": date,
```

## ![](https://img.shields.io/badge/-GET%20-green) /clients/

Get all clients.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns an array of [client](#Client-Model)


## ![](https://img.shields.io/badge/-GET%20-green) /clients/1/

Get one client.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns a [client](#Client-Model)

## ![](https://img.shields.io/badge/-POST%20-orange) /clients/1/

Get one client.

**Request Body**

```cs
"company_name": string
"mobile": string
"user": int
```

> note: you need to have a valid **User ID** in order to create a client

### Success

**Response 200**

Returns a [client](#Client-Model)

## ![](https://img.shields.io/badge/-PATCH%20-blueviolet) /clients/1/

Update one client.

**Request Body**

```cs
"sales_contact": int
"is_validated": bool,
"phone": string,
"mobile": string,
"company_name": string,
```

> note: at least **one field** must be provided

### Success

**Response 200**

Returns a [client](#Client-Model)

## ![](https://img.shields.io/badge/-DELETE%20-critical) /clients/1

Update one client.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns a [client](#Client-Model)