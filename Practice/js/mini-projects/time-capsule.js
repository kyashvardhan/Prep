// Time Capsule Messenger - Schedule messages to be displayed in the future
class TimeCapsule {
    constructor() {
        this.messages = JSON.parse(localStorage.getItem("capsule")) || [];
        this.checkMessages();
    }

    scheduleMessage(text, delayInSeconds) {
        const futureTime = Date.now() + delayInSeconds * 1000;
        this.messages.push({ text, time: futureTime });
        this.updateStorage();
        console.log(`Message saved! It will appear in ${delayInSeconds} seconds.`);
    }

    checkMessages() {
        setInterval(() => {
            const now = Date.now();
            this.messages = this.messages.filter((msg) => {
                if (msg.time <= now) {
                    console.log(`🔔 Time Capsule Message: "${msg.text}"`);
                    return false; // Remove message after displaying
                }
                return true;
            });
            this.updateStorage();
        }, 1000);
    }

    updateStorage() {
        localStorage.setItem("capsule", JSON.stringify(this.messages));
    }
}

// Usage Example
const capsule = new TimeCapsule();
capsule.scheduleMessage("Hello from the past!", 10);
