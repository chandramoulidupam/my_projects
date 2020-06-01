import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from project_management_portal.interactors.logout_interactor import \
    LogoutInteractor
from project_management_portal.storages.user_storage_implementation import \
    LogoutStorageImplementation
from project_management_portal.presenters.user_logout_presenter_implementation import \
    UserLogoutPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    user = kwargs['user']
    request_data = kwargs['request_data']
    storage = LogoutStorageImplementation()
    presenter = UserLogoutPresenterImplementation()
    interactor = LogoutInteractor(
        storage=storage,
        presenter=presenter
    )

    response = interactor.user_logout(
        access_token=request_data['access_token']
    )
    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)
