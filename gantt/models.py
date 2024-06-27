from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Task(models.Model):
    parentId = models.ForeignKey(
        'Task',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subtasks',
        db_column='parentId',
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    startDate = models.DateTimeField(null=True, blank=True, db_column='startDate')
    endDate = models.DateTimeField(null=True, blank=True, db_column='endDate')
    effort = models.FloatField(null=True, blank=True)
    effortUnit = models.CharField(
        max_length=255, default='hour', null=True, blank=True, db_column='effortUnit'
    )
    duration = models.FloatField(null=True, blank=True)
    durationUnit = models.CharField(
        max_length=255, default='day', null=True, blank=True, db_column='durationUnit'
    )
    percentDone = models.FloatField(
        default=0,
        null=True,
        blank=True,
        db_column='percentDone',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    schedulingMode = models.CharField(
        max_length=255, null=True, blank=True, db_column='schedulingMode'
    )
    note = models.TextField(null=True, blank=True)
    constraintType = models.CharField(
        max_length=255, null=True, blank=True, db_column='constraintType'
    )
    constraintDate = models.DateTimeField(
        null=True, blank=True, db_column='constraintDate'
    )
    manuallyScheduled = models.BooleanField(
        default=False, null=True, blank=True, db_column='manuallyScheduled'
    )
    effortDriven = models.BooleanField(
        default=False, null=True, blank=True, db_column='effortDriven'
    )
    inactive = models.BooleanField(default=False, null=True, blank=True)
    cls = models.CharField(max_length=255, null=True, blank=True)
    iconCls = models.CharField(
        max_length=255, null=True, blank=True, db_column='iconCls'
    )
    color = models.CharField(max_length=255, null=True, blank=True)
    parentIndex = models.IntegerField(
        default=0, null=True, blank=True, db_column='parentIndex'
    )
    expanded = models.BooleanField(default=False, null=True, blank=True)
    calendar = models.IntegerField(default=0, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    direction = models.CharField(max_length=255, null=True, blank=True)
    unscheduled = models.BooleanField(default=False, null=True, blank=True)
    ignoreResourceCalendar = models.BooleanField(default=False, null=True, blank=True)
    delayFromParent = models.IntegerField(
        default=0, null=True, blank=True, db_column='delayFromParent'
    )
    projectConstraintResolution = models.CharField(
        default='',
        max_length=255,
        null=True,
        blank=True,
        db_column='projectConstraintResolution',
    )
    baselines = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return self.name if self.name else 'Unnamed Task'


class Dependency(models.Model):
    fromEvent = models.ForeignKey(
        'Task',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='dependencies_from',
        db_column='fromEvent',
    )
    toEvent = models.ForeignKey(
        'Task',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='dependencies_to',
        db_column='toEvent',
    )
    type = models.IntegerField(default=2, null=True, blank=True)
    cls = models.CharField(max_length=255, null=True, blank=True)
    lag = models.FloatField(default=0, null=True, blank=True)
    lagUnit = models.CharField(
        max_length=255, default='day', null=True, blank=True, db_column='lagUnit'
    )
    active = models.BooleanField(null=True, blank=True)
    fromSide = models.CharField(
        max_length=255, null=True, blank=True, db_column='fromSide'
    )
    toSide = models.CharField(max_length=255, null=True, blank=True, db_column='toSide')

    class Meta:
        db_table = 'dependencies'
