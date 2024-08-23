const { Client } = require('unb-api');
const client = new Client('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIxMjcyMzMyMzM5NjkwNzMzNTk2IiwiaWF0IjoxNzIzNDE4MDY4fQ.h5gGc4ZRWOcH1DkYlB-brvUAR91Sij1zckoQdvxG5eU');    // Get your API token from https://unbelievaboat.com/api/docs

const guildI = '938728183203758080';
const userId = '432437043956809738';

client.editUserBalance(guildId, userId, { cash: 8000000, bank: 0, reason: "https://cdn.discordapp.com/attachments/938728183203758082/1276472585898426500/meme.png?ex=66c9a73c&is=66c855bc&hm=8a97c24a597e8fab83ca6b0151381268d1c6cef6cc731eca4e2e278aceb64d31&" });