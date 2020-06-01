import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from project_management_portal.interactors.login_interactor import \
    LoginInteractor
from project_management_portal.storages.user_storage_implementation import \
    LoginStorageImplementation
from project_management_portal.presenters.user_login_presenter_implementation import \
    UserLoginPresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    user = kwargs['user']

    storage = LoginStorageImplementation()
    oauth_storage = OAuth2SQLStorage()
    presenter = UserLoginPresenterImplementation()
    interactor = LoginInteractor(
        storage=storage,
        oauth_storage=oauth_storage,
        presenter=presenter
    )

    response = interactor.user_login(
        username=user.username,
        password=user.password
    )
    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)
