# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.cart import Cart, CartDraft, CartPagedQueryResponse
from ...models.error import ErrorResponse
from ..replicate.by_project_key_in_store_key_by_store_key_carts_replicate_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartsReplicateRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_carts_by_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_carts_customer_id_by_customer_id_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder,
)
from .by_project_key_in_store_key_by_store_key_carts_key_by_key_request_builder import (
    ByProjectKeyInStoreKeyByStoreKeyCartsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeyInStoreKeyByStoreKeyCartsRequestBuilder:

    _client: "BaseClient"
    _project_key: str
    _store_key: str

    def __init__(
        self,
        project_key: str,
        store_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._store_key = store_key
        self._client = client

    def with_customer_id(
        self, customer_id: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder:
        return (
            ByProjectKeyInStoreKeyByStoreKeyCartsCustomerIdByCustomerIdRequestBuilder(
                customer_id=customer_id,
                project_key=self._project_key,
                store_key=self._store_key,
                client=self._client,
            )
        )

    def with_key(
        self, key: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCartsKeyByKeyRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCartsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def replicate(self) -> ByProjectKeyInStoreKeyByStoreKeyCartsReplicateRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCartsReplicateRequestBuilder(
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def with_id(
        self, id: str
    ) -> ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder:
        return ByProjectKeyInStoreKeyByStoreKeyCartsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
            store_key=self._store_key,
            client=self._client,
        )

    def get(
        self,
        *,
        expand: typing.List["str"] = None,
        sort: typing.List["str"] = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: typing.List["str"] = None,
        predicate_var: typing.Dict[str, typing.List["str"]] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["CartPagedQueryResponse"]:
        """Queries carts in a specific Store."""
        params = {
            "expand": expand,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "withTotal": with_total,
            "where": where,
        }
        predicate_var and params.update(
            {f"var.{k}": v for k, v in predicate_var.items()}
        )
        headers = {} if headers is None else headers
        response = self._client._get(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return CartPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "CartDraft",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Cart"]:
        """Creates a cart in the store specified by {storeKey}.
        When using this endpoint the cart's store field is always set to the store specified in the path parameter.
        Creating a cart can fail with an InvalidOperation if the referenced shipping method
        in the CartDraft has a predicate which does not match the cart.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/in-store/key={self._store_key}/carts",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return Cart.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)
