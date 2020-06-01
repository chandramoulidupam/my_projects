import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from project_management_portal.interactors.get_list_of_projects import \
    GetListOfProjectInteractor
from project_management_portal.storages.get_list_of_projects_storage_implementation import \
    GetListOfProjectImplementation
from project_management_portal.presenters.get_list_of_projects_presenter_implementation import \
    GetListOfProjectPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    user = kwargs['user']
    query_parameters = kwargs['request_query_params']
    storage = GetListOfProjectImplementation()
    presenter = GetListOfProjectPresenterImplementation()
    interactor = GetListOfProjectInteractor(
        storage=storage,
        presenter=presenter
    )

    response = interactor.get_list_of_project(
        user_id=user.id,
        offset=query_parameters['offset'],
        limit=query_parameters['limit'],
    )
    print("\n"*15, response)
    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)
