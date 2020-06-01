from django.contrib.auth.models import AbstractUser
from django.db import models
from project_management_portal.constants.enums import ProjectType, IssueType


class User(AbstractUser):
    name = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return "%s %s" % (self.name, self.profile_pic)


class State(models.Model):
    name = models.CharField(max_length=50)


class Transition(models.Model):
    name = models.CharField(max_length=50)
    from_state = models.ForeignKey(State, on_delete=models.CASCADE,related_name="present_state")
    to_state = models.ForeignKey(State, on_delete=models.CASCADE)


class WorkflowType(models.Model):
    name = models.CharField(max_length=200)
    states = models.ManyToManyField(State)
    transitions = models.ManyToManyField(Transition)
    created_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    workflow_type = models.ForeignKey(WorkflowType, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=100,
        choices=ProjectType.get_list_of_tuples()
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_of_project")
    created_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ManyToManyField(User)
    def __str__(self):
        return self.project_type

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    issue_type = models.CharField(max_length=100,
        choices=IssueType.get_list_of_tuples()
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default="Backlog")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
