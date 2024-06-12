# Bryntum Gantt with Django

How to use the Bryntum Gantt with Django 

## Getting Started

Clone the repo and checkout the complete app branch 

Create and activate a virtual environment 

```sh
python -m venv venv
source venv/bin/activate
```

Install Django

```sh
pip install django
```

Run migrations 

```shell
python manage.py makemigrations gantt
python manage.py migrate 
```

Load sample data into SQLite database 

```shell
sqlite3 db.sqlite3
```

```
INSERT INTO tasks (id, name, startDate, endDate, effort, effortUnit, duration, durationUnit, percentDone, schedulingMode, note, constraintType, constraintDate, manuallyScheduled, effortDriven, inactive, cls, iconCls, color, expanded, calendar, deadline, direction, baselines, delayFromParent, ignoreResourceCalendar, projectConstraintResolution, unscheduled, parentIndex, parentId)
values  (1, 'Launch SaaS Product', '2024-06-14 00:00:00', '2024-06-20 22:00:00', 6, 'hour', 6.916666666666667, 'day', 50, null, null, null, null, 0, 0, 0, null, '', null, 1, 0, null, null, null, 0, 0, '', 0, 0, null),
        (2, 'Setup web server', '2024-06-14 00:00:00', '2024-06-20 22:00:00', 6, 'hour', 6.916666666666667, 'day', 50, null, null, null, null, 0, 0, 0, null, '', null, 1, 0, null, null, null, 0, 0, '', 0, 0, 1),
        (3, 'Install Apache', '2024-06-14 00:00:00', '2024-06-17 00:00:00', 3, 'hour', 3, 'day', 50, null, null, null, null, 0, 0, 0, null, '', null, 0, 0, null, null, null, 0, 0, '', 0, 0, 2),
        (4, 'Configure firewall', '2024-06-17 22:00:00', '2024-06-20 22:00:00', 3, 'hour', 3, 'day', 50, null, null, 'startnoearlierthan', '2024-06-17 22:00:00', 0, 0, 0, null, '', null, 0, 0, null, null, null, 0, 0, '', 0, 1, 2);
```

```
INSERT INTO dependencies (id, cls, lag, lagUnit, active, fromSide, toSide, fromEvent, toEvent, type)
values  (1, null, 2, 'day', null, null, null, 3, 4, 2);
```

Download the Bryntum Gantt distribution folder [here](https://customerzone.bryntum.com/)

Copy the following files and folders from the `/build` folder in the Bryntum Gantt distribution folder and paste them into the `static/bryntum-gantt` folder:

```
fonts
locales
gantt.module.js
gantt.module.js.map
gantt.stockholm.css
gantt.stockholm.css.map
```

## Running the app

```
python manage.py runserver localhost:8000
```

The app will be accessible at `http://localhost:8000` and you can perform Gantt CRUD operations