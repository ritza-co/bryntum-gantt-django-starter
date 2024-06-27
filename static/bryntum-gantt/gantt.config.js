import { Gantt } from './gantt.module.js';

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const gantt = new Gantt({
    appendTo : document.body,
    project  : {
        taskStore : {
            autoTree          : true,
            transformFlatData : true
        },
        transport : {
            load : {
                url : '/load'
            },
            sync : {
                url     : '/sync',
                headers : { 'X-CSRFToken' : csrftoken }
            }
        },
        autoLoad         : true,
        autoSync         : true,
        validateResponse : true
    },

    columns : [{ type : 'name', width : 250, text : 'Tasks' }]
});