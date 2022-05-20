# Contract Enpoints

## Contract Model

```cs
"id": int
"client": int
"salesmans": int[]
"status": bool
"amount": float
"date_created": date
"date_updated": date
"payment_due": date
```

## Filters

This enpoint can be filtered using "search" and "ordering"

> **eg**: GET /example/?search=value&ordering=field

## ![](https://img.shields.io/badge/-GET%20-green) /contracts/

Get all contracts.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns an array of [contract](#Contract-Model)


## ![](https://img.shields.io/badge/-GET%20-green) /contracts/1/

Get one contract.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns a [contract](#Contract-Model)

## ![](https://img.shields.io/badge/-POST%20-orange) /contracts/1/

Get one contract.

**Request Body**

```cs
"client": int
"salesmans": int[]
"status": bool
"amount": float
"payment_due": date
```

> note: In order to create a contract, you will need a valid:
> - **User ID** 
> - **Client ID**
> - **Salesman ID** 



### Success

**Response 200**

Returns a [contract](#Contract-Model)

## ![](https://img.shields.io/badge/-PATCH%20-blueviolet) /contracts/1/

Update one contract.

**Request Body**

```cs
"status": bool
"amount": float
"payment_due": date
```

> note: at least **one field** must be provided

### Success

**Response 200**

Returns a [contract](#Contract-Model)

## ![](https://img.shields.io/badge/-DELETE%20-critical) /contracts/1

Update one contract.

**Request Body**

```cs
Empty
```

### Success

**Response 201**

```cs
Empty
```
