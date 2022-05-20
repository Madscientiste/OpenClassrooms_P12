# Event Enpoints

## Event Model

```cs
"id": int,
"client": int,
"support": int
"contract": int,
"date_created": date,
"date_updated": date,
"attendees": int,
"event_date": date,
"notes": string,
```

## Filters

This enpoint can be filtered using "search" and "ordering"

> **eg**: GET /example/?search=value&ordering=field

## ![](https://img.shields.io/badge/-GET%20-green) /events/

Get all events.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns an array of [event](#Event-Model)


## ![](https://img.shields.io/badge/-GET%20-green) /events/1/

Get one event.

**Request Body**

```cs
Empty
```

### Success

**Response 200**

Returns a [event](#Event-Model)

## ![](https://img.shields.io/badge/-POST%20-orange) /events/1/

Get one event.

**Request Body**

```cs
"client": int,
"support": int
"contract": int,
"attendees": int,
"event_date": date,
"notes": string,
```

> note: In order to create a event, you will need a valid:
> - **Client ID**
> - **Support ID** 


### Success

**Response 200**

Returns a [event](#Event-Model)

## ![](https://img.shields.io/badge/-PATCH%20-blueviolet) /events/1/

Update one event.

**Request Body**

```cs
"client": int,
"support": int
"contract": int,
"attendees": int,
"event_date": date,
"notes": string,
```

> note: at least **one field** must be provided

### Success

**Response 200**

Returns a [event](#Event-Model)

## ![](https://img.shields.io/badge/-DELETE%20-critical) /events/1

Update one event.

**Request Body**

```cs
Empty
```

### Success

**Response 201**

```cs
Empty
```
