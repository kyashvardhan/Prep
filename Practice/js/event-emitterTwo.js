class EventEmitter {
  constructor() {
    this.events = {};
  }
  
  on(event, listener) {
    if (!this.events[event]) this.events[event] = [];
    this.events[event].push(listener);
  }
  
  emit(event, ...args) {
    if (this.events[event]) {
      this.events[event].forEach(listener => listener.apply(this, args));
    }
  }
  
  off(event, listenerToRemove) {
    if (!this.events[event]) return;
    this.events[event] = this.events[event].filter(listener => listener !== listenerToRemove);
  }
}

// Example usage:
const emitter = new EventEmitter();
function greeting(name) { console.log(`Hello, ${name}!`); }
emitter.on("greet", greeting);
emitter.emit("greet", "Yash");
emitter.off("greet", greeting);
emitter.emit("greet", "Yash"); // No output after removal
