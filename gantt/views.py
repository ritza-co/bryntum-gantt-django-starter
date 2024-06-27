from django.shortcuts import render
from .models import Task, Dependency
from django.http import JsonResponse
from django.views.decorators.http import require_GET

import json


def index(request):
    return render(request, 'index.html')


@require_GET
def load(request):
    try:
        tasks = list(Task.objects.all().values())
        dependencies = list(Dependency.objects.all().values())

        for task in tasks:
            task['parentId'] = task.pop('parentId_id')

        for dependency in dependencies:
            dependency['fromEvent'] = dependency.pop('fromEvent_id')
            dependency['toEvent'] = dependency.pop('toEvent_id')

        response_data = {
            "success": True,
            "tasks": {
                "rows": tasks,
            },
            "dependencies": {
                "rows": dependencies,
            },
        }
        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse({
            "success": False,
            "error": str(e)
        }, status=500)


def create_operation(added, table):
    record_mapping = []
    for record in added:
        phantom_id = record.pop('$PhantomId', None)
        new_record = None

        if table == 'tasks':
            record['parentId_id'] = record.pop('parentId')
            record.pop('segments')
            new_record = Task.objects.create(**record)

        if table == 'dependencies':
            record['fromEvent_id'] = record.pop('fromEvent')
            record['toEvent_id'] = record.pop('toEvent')
            record.pop('from')
            record.pop('to')
            new_record = Dependency.objects.create(**record)

        if new_record:
            record_mapping.append({'$PhantomId': phantom_id, 'id': new_record.id})
    return record_mapping


def update_operation(updated, table):
    for record in updated:
        if table == 'tasks':
            Task.objects.filter(id=record['id']).update(**record)

        if table == 'dependencies':
            Dependency.objects.filter(id=record['id']).update(**record)


def delete_operation(deleted, table):
    for record in deleted:
        if table == 'tasks':
            Task.objects.filter(id=record['id']).delete()

        if table == 'dependencies':
            Dependency.objects.filter(id=record['id']).delete()


def apply_table_changes(table, changes):
    rows = None
    if 'added' in changes:
        rows = create_operation(changes['added'], table)
    if 'updated' in changes:
        update_operation(changes['updated'], table)
    if 'removed' in changes:
        delete_operation(changes['removed'], table)
    return rows


def sync(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        request_id = data.get('requestId')
        tasks = data.get('tasks')
        dependencies = data.get('dependencies')

        try:
            response = {'requestId': request_id, 'success': True}
            if tasks:
                rows = apply_table_changes("tasks", tasks)
                if rows:
                    response['tasks'] = {'rows': rows}

            if dependencies:
                rows = apply_table_changes("dependencies", dependencies)
                if rows:
                    response['dependencies'] = {'rows': rows}

            return JsonResponse(response)
        except Exception as e:
            print(e)
    return JsonResponse(
        {'success': False, 'message': 'There was an error syncing the data changes.'})
