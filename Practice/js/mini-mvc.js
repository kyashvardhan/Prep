class Model {
  constructor() {
    this.data = {};
  }
  set(key, value) {
    this.data[key] = value;
    this.onChange && this.onChange(this.data);
  }
  get(key) {
    return this.data[key];
  }
}

class View {
  constructor(model, templateId, containerId) {
    this.model = model;
    this.template = document.getElementById(templateId).innerHTML;
    this.container = document.getElementById(containerId);
    this.model.onChange = () => this.render();
  }
  render() {
    this.container.innerHTML = this.template.replace(/\{\{(.*?)\}\}/g, (match, key) => {
      return this.model.get(key.trim()) || '';
    });
  }
}

class Controller {
  constructor(model, view) {
    this.model = model;
    this.view = view;
  }
  updateData(key, value) {
    this.model.set(key, value);
  }
}

// Example usage:
// HTML required:
// <script type="text/template" id="tpl">Hello, {{name}}!</script>
// <div id="app"></div>
const model = new Model();
const view = new View(model, "tpl", "app");
const controller = new Controller(model, view);
controller.updateData("name", "Yash");
