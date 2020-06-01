import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from .validator_class import ValidatorClass
from project_management_portal.interactors.create_task_interactor import \
    CreateTaskInteractor
from project_management_portal.storages.create_task_storage_implementation import \
    CreateTaskImplementation
from project_management_portal.presenters.create_task_presenter_implementation import \
    CreateTaskPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    project_id = kwargs['project_id']
    request_data = kwargs['request_data']

    storage = CreateTaskImplementation()
    presenter = CreateTaskPresenterImplementation()

    interactor = CreateTaskInteractor(
        storage=storage,
        presenter=presenter
    )
    response = interactor.create_task(
        title=request_data['title'],
        issue_type=request_data['issue_type'],
        project_id=project_id,
        description=request_data['description'],
        assigned_to_id=request_data['assigned_to'],
        state_id=1
    )
    # print("\n" * 10,response)
    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)
