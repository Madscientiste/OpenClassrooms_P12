# Login

* [Main Page](/doc/README.md)

Used to collect a (``Access`` & ``Refresh``) Token for a registered User.

**URL** : `/api/login/`

**Method** : `POST`

**Data constraints**

```json
{
    "username": "[valid email address]",
    "password": "[password in plain text]"
}
```

**Data example**

```json
{
    "username": "iloveauth@example.com",
    "password": "abcd1234"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwI...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MT.."

}
```

## Error Response Types

**Code** : `400 BAD REQUEST`

**ARRAY**

```json
[
  {
    "username": [
        "A user with that username already exists."
        // ... //
    ],
    "password": [
        "This password is too common.",
        "This password is entirely numeric."
        // ... //
    ]
  }
]
```

**Object**

```json
{
  "detail": "No active account found with the given credentials"
}
```
