# Sales Enpoints

## Sales Model

```cs
"id": int
"user": int
```

## ![](https://img.shields.io/badge/-GET%20-green) /sales/

Get all sales.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns an array of [sales](#Sales-Model)


## ![](https://img.shields.io/badge/-GET%20-green) /sales/1/

Get one sales.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns a [sales](#Sales-Model)

## ![](https://img.shields.io/badge/-POST%20-orange) /sales/1/

Get one sales.

**Request Body**

```cs
"user": int
```

> note: you need to have a valid **User ID** in order to create a sales

### Success

**Response 200**

Returns a [sales](#Sales-Model)

## ![](https://img.shields.io/badge/-PATCH%20-blueviolet) /sales/1/

Update one sales.

**Request Body**

```cs
"user": int
```

> note: at least **one field** must be provided

### Success

**Response 200**

Returns a [sales](#Sales-Model)

## ![](https://img.shields.io/badge/-DELETE%20-critical) /sales/1

Update one sales.

**Request Body**

```cs
Empty
```

### Success

**Response 201**

```cs
Empty
```