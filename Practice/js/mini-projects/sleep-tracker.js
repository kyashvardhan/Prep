// AI-Powered Sleep Cycle Tracker
class SleepTracker {
    constructor() {
        this.sleepData = JSON.parse(localStorage.getItem("sleep")) || [];
    }

    startSleep() {
        const startTime = new Date().toISOString();
        console.log("🛏️ Sleep started at", startTime);
        localStorage.setItem("sleepStart", startTime);
    }

    wakeUp() {
        const wakeTime = new Date().toISOString();
        const startTime = localStorage.getItem("sleepStart");

        if (!startTime) {
            console.log("❌ No sleep session found.");
            return;
        }

        const duration = (new Date(wakeTime) - new Date(startTime)) / 3600000;
        this.sleepData.push({ start: startTime, end: wakeTime, duration: duration.toFixed(2) });
        localStorage.setItem("sleep", JSON.stringify(this.sleepData));
        localStorage.removeItem("sleepStart");

        console.log(`⏰ You slept for ${duration.toFixed(2)} hours.`);
    }

    showSleepData() {
        console.log("📊 Sleep History:", this.sleepData);
    }
}

// Usage Example
const sleepTracker = new SleepTracker();
sleepTracker.startSleep(); // Call before sleeping
setTimeout(() => sleepTracker.wakeUp(), 8000); // Simulating 8 seconds of sleep
