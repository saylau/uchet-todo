from django.db.models import QuerySet


class TaskQueryset(QuerySet):
    def own(self):
        return self.filter(user=True)
