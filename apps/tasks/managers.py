from typing import TYPE_CHECKING
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

from django.db.models import QuerySet, Manager, Model, Avg
from django.utils import timezone


class TaskQueryset(QuerySet):
    def own(self):
        return self.filter(user=True)
