class Habit {
    constructor(name) {
        this.name = name;
        this.log = [];
    }

    mark(status) {
        const today = new Date().toDateString();
        this.log.push({ date: today, status });
        console.log(`✅ Marked ${this.name} as ${status ? 'done' : 'missed'} on ${today}`);
    }

    weeklyReport() {
        const completed = this.log.filter(entry => entry.status).length;
        const missed = this.log.length - completed;
        console.log(`📅 Weekly Report for "${this.name}":`);
        console.log(`✅ Completed: ${completed} days`);
        console.log(`❌ Missed: ${missed} days`);
    }
}

// Example usage
const drinkWater = new Habit("Drink 2L Water");
drinkWater.mark(true);
drinkWater.mark(false);
drinkWater.mark(true);
drinkWater.weeklyReport();
