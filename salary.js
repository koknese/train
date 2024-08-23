const { Client } = require('unb-api');
const client = new Client('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIxMjcyMzMyMzM5NjkwNzMzNTk2IiwiaWF0IjoxNzIzNDE4MDY4fQ.h5gGc4ZRWOcH1DkYlB-brvUAR91Sij1zckoQdvxG5eU');    // Get your API token from https://unbelievaboat.com/api/docs

const guildId = '938728183203758080';
const userId = '432437043956809738';

client.editUserBalance(guildId, userId, { cash: 8000000, bank: 0, reason: "Salary" });