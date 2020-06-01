import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from project_management_portal.interactors.get_list_of_tasks import \
    GetListOfTaskInteractor
from project_management_portal.storages.get_list_of_tasks_storage_implementation import \
    GetListOfTaskImplementation
from project_management_portal.presenters.get_list_of_tasks_presenter_implementation import \
    GetListOfTaskstPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    # user = kwargs['user']
    request_data = kwargs['request_data']
    # query_parameters = kwargs['request_query_params']
    storage = GetListOfTaskImplementation()
    presenter = GetListOfTaskstPresenterImplementation()
    interactor = GetListOfTaskInteractor(
        storage=storage,
        presenter=presenter
    )

    response = interactor.get_list_of_tasks_for_user(
        project_id=kwargs['project_id'],
    )
    # print("\n"*15, response)
    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)
