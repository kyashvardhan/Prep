async function convertCurrency(amount, fromCurrency, toCurrency) {
  const response = await fetch(`https://api.exchangerate-api.com/v4/latest/${fromCurrency}`);
  const data = await response.json();
  const rate = data.rates[toCurrency];
  const converted = (amount * rate).toFixed(2);
  console.log(`💱 ${amount} ${fromCurrency} = ${converted} ${toCurrency}`);
}

// Example usage
convertCurrency(100, 'USD', 'INR');
