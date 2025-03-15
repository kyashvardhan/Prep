// Crypto Price Alert System (Using CoinGecko API)
const fetch = require("node-fetch");

async function getCryptoPrice(crypto = "bitcoin") {
    const response = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${crypto}&vs_currencies=usd`);
    const data = await response.json();
    console.log(`💰 ${crypto.toUpperCase()} price: $${data[crypto].usd}`);
}

// Check price every 10 seconds
setInterval(() => getCryptoPrice("ethereum"), 10000);
