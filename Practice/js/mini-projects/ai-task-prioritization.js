class Task {
    constructor(title, description, urgency, importance) {
        this.title = title;
        this.description = description;
        this.urgency = urgency; // Scale: 1-10
        this.importance = importance; // Scale: 1-10
        this.score = this.calculatePriority();
    }

    calculatePriority() {
        return (this.urgency * 0.6) + (this.importance * 0.4);
    }
}

class TaskManager {
    constructor() {
        this.tasks = [];
    }

    addTask(title, description, urgency, importance) {
        const task = new Task(title, description, urgency, importance);
        this.tasks.push(task);
        this.sortTasks();
    }

    sortTasks() {
        this.tasks.sort((a, b) => b.score - a.score);
    }

    displayTasks() {
        console.log("📌 **Prioritized Task List**:");
        this.tasks.forEach(task => {
            console.log(`🔹 ${task.title} - Score: ${task.score.toFixed(2)}`);
        });
    }
}

// Example usage
const taskManager = new TaskManager();
taskManager.addTask("Complete JavaScript project", "Finish all pending assignments", 8, 10);
taskManager.addTask("Grocery Shopping", "Buy fruits and vegetables", 4, 5);
taskManager.addTask("Workout", "Cardio and strength training", 6, 7);

taskManager.displayTasks();
