const apiURL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin&vs_currencies=usd";

async function fetchCryptoPrices() {
    try {
        const response = await fetch(apiURL);
        const data = await response.json();
        
        console.log("💰 Live Cryptocurrency Prices:");
        console.log(`🔹 Bitcoin: $${data.bitcoin.usd}`);
        console.log(`🔹 Ethereum: $${data.ethereum.usd}`);
        console.log(`🔹 Dogecoin: $${data.dogecoin.usd}`);
    } catch (error) {
        console.error("Error fetching crypto prices:", error);
    }
}

// Fetch and update prices every 10 seconds
setInterval(fetchCryptoPrices, 10000);
fetchCryptoPrices();
