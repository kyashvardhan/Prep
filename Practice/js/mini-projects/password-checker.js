// Password Strength & Breach Checker (Uses HaveIBeenPwned API)
const fetch = require("node-fetch");
const crypto = require("crypto");

async function checkPassword(pw) {
    const hash = crypto.createHash("sha1").update(pw).digest("hex").toUpperCase();
    const prefix = hash.slice(0, 5);
    const suffix = hash.slice(5);

    const response = await fetch(`https://api.pwnedpasswords.com/range/${prefix}`);
    const data = await response.text();

    if (data.includes(suffix)) {
        console.log("⚠️ This password has been leaked in data breaches! Change it immediately.");
    } else {
        console.log("✅ This password is safe.");
    }
}

// Usage Example
checkPassword("mypassword123");
