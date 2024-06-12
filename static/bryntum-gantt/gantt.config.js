import {Gantt} from "./gantt.module.js";


const gantt = new Gantt({
  appendTo: document.body,
  project: {
    taskStore: {
      autoTree: true,
      transformFlatData: true,
    },
    transport: {
      load: {
        url: "/load",
      },
      sync: {
        url: "/sync",
      },
    },
    autoLoad: true,
    autoSync: true,
    validateResponse: true,
  },

  columns: [{type: "name", width: 250, text: "Tasks"}],
});