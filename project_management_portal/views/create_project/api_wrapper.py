import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from .validator_class import ValidatorClass
from project_management_portal.interactors.create_project_interactor import \
    CreateProjectInteractor
from project_management_portal.storages.create_project_storage_implementation import \
    CreateProjectImplementation
from project_management_portal.presenters.create_project_presenter_implementation import \
    CreateProjectPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    user = kwargs['user']
    request_data = kwargs['request_data']

    storage = CreateProjectImplementation()
    presenter = CreateProjectPresenterImplementation()
    interactor = CreateProjectInteractor(
        storage=storage,
        presenter=presenter
    )

    response = interactor.create_project(
        user_id=user.id,
        name=request_data['name'],
        description=request_data['description'],
        workflow_type=request_data['workflow_type'],
        project_type=request_data['project_type']
    )
    # print("\n" * 10,response)
    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)
