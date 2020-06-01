import pytest
from freezegun import freeze_time
from project_management_portal.models import User, Project,Task, State, Transition, WorkflowType

@pytest.fixture()
def users():
    list_of_users = [
        User(username="user1",password="user1passowrd", is_admin=True),
        User(username="user2",password="user2passowrd", is_admin=False),
        User(username="user3",password="user3passowrd", is_admin=False)
        ]
    User.objects.bulk_create(list_of_users)
    users = User.objects.all()
    return users

@pytest.fixture()
@freeze_time("2020-05-20")
def states():
    list_of_states = [
        State(name="TODO"),
        State(name="To be reviewed"),
        State(name="TODO")
    ]
    State.objects.bulk_create(list_of_states)
    state_objs = State.objects.all()
    return state_objs

@pytest.fixture()
@freeze_time("2020-05-20")
def transitions(states):
    state_obj_1 = State.objects.get(id=1)
    # state_obj_2 = State.objects.get(id=2)
    state_obj_3 = State.objects.get(id=3)
    transition1 = Transition.objects.create(name="transition1", from_state_id=1, to_state_id=3)
    # transition1.present_state.add(state_obj_1)
    # transition1.to_state.add(state_obj_3)
            
    # list_of_transtions = [
    #     Transition(transition="transition2",
    #         description='description2',
    #         from_state=state_obj_2,
    #         to_state=state_obj_3),
    #     Transition(transition="transition3",
    #         description='description3',
    #         from_state=state_obj_1,
    #         to_state=state_obj_2)
    # ]
    # Transition.objects.bulk_create(list_of_transtions)
    transition_objs = Transition.objects.all()

    return transition_objs

@pytest.fixture()
@freeze_time("2020-05-20")
def workflow(transitions):
    state_obj1 = State.objects.get(id=1)
    state_obj2 = State.objects.get(id=2)
    state_obj3 = State.objects.get(id=3)

    transition_obj1 = Transition.objects.get(id=1)
    # transition_obj2 = Transition.objects.get(id=2)
    # transition_obj3 = Transition.objects.get(id=3)

    workflow_obj_1 = WorkflowType.objects.create(name='workflow1')
    workflow_obj_2 = WorkflowType.objects.create(name='workflow2')
    workflow_obj_3 = WorkflowType.objects.create(name='workflow3')

    workflow_obj_1.states.add(state_obj1)
    workflow_obj_2.states.add(state_obj2)
    workflow_obj_3.states.add(state_obj3)

    workflow_obj_1.transitions.add(transition_obj1)
    # workflow_obj_2.transitions.add(transition_obj2)
    # workflow_obj_3.transitions.add(transition_obj3)

    workflow_objs = [workflow_obj_1]

    return workflow_objs

@pytest.fixture()
@freeze_time("2020-05-20")
def create_project(workflow):
    list_of_projects = [
        Project(name='project_1',
                    created_by_id=1,
                    description='description1',
                    workflow_type_id=1,
                    project_type='CRM'
                ),
        Project(name='project_2',
                created_by_id=1,
                description='description2',
                workflow_type_id=2,
                project_type='Financial'
            )
    ]

    project_objs = Project.objects.bulk_create(list_of_projects)

    return project_objs

@pytest.fixture()
@freeze_time("2020-05-20")
def create_task(create_project):
    list_of_tasks = [
        Task(title="PMP",
                description="project_management_portal",
                issue_type="Task",
                assigned_to_id=1,
                state_id=1,
                project_id=1
            ),
        Task(title="GYAAN",
                description="GYAAN",
                issue_type="Task",
                assigned_to_id=1,
                state_id=1,
                project_id=2
            )
    ]

    task_objs = Task.objects.bulk_create(list_of_tasks)

    return task_objs
