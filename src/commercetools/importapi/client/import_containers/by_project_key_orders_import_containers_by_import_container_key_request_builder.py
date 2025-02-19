# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.errors import ErrorResponse
from ...models.importrequests import ImportResponse, OrderImportRequest

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyOrdersImportContainersByImportContainerKeyRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _import_container_key: str

    def __init__(
        self,
        project_key: str,
        import_container_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._import_container_key = import_container_key
        self._client = client

    def post(
        self,
        body: "OrderImportRequest",
        *,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> "ImportResponse":
        """Creates a request for creating new Orders or updating existing ones."""
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/orders/import-containers/{self._import_container_key}",
            params={},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return ImportResponse.deserialize(response.json())
        elif response.status_code == 400:
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        warnings.warn("Unhandled status code %d" % response.status_code)
