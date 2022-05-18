# Support Enpoints

## Support Model

```cs
"id": int
"user": int
```

## ![](https://img.shields.io/badge/-GET%20-green) /supports/

Get all supports.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns an array of [support](#Support-Model)


## ![](https://img.shields.io/badge/-GET%20-green) /supports/1/

Get one support.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns a [support](#Support-Model)

## ![](https://img.shields.io/badge/-POST%20-orange) /supports/1/

Get one support.

**Request Body**

```cs
"user": int
```

> note: you need to have a valid **User ID** in order to create a support

### Success

**Response 200**

Returns a [support](#Support-Model)

## ![](https://img.shields.io/badge/-PATCH%20-blueviolet) /supports/1/

Update one support.

**Request Body**

```cs
"user": int
```

> note: at least **one field** must be provided

### Success

**Response 200**

Returns a [support](#Support-Model)

## ![](https://img.shields.io/badge/-DELETE%20-critical) /supports/1

Update one support.

**Request Body**

```cs
Empty
```

### Success

**Response 201**

```cs
Empty
```