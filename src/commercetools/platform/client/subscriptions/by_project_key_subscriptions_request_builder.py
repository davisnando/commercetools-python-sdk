# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import typing
import warnings

from ...models.error import ErrorResponse
from ...models.subscription import (
    Subscription,
    SubscriptionDraft,
    SubscriptionPagedQueryResponse,
)
from .by_project_key_subscriptions_by_id_request_builder import (
    ByProjectKeySubscriptionsByIDRequestBuilder,
)
from .by_project_key_subscriptions_key_by_key_request_builder import (
    ByProjectKeySubscriptionsKeyByKeyRequestBuilder,
)

if typing.TYPE_CHECKING:
    from ...base_client import BaseClient


class ByProjectKeySubscriptionsRequestBuilder:

    _client: "BaseClient"
    _project_key: str

    def __init__(
        self,
        project_key: str,
        client: "BaseClient",
    ):
        self._project_key = project_key
        self._client = client

    def with_key(self, key: str) -> ByProjectKeySubscriptionsKeyByKeyRequestBuilder:
        return ByProjectKeySubscriptionsKeyByKeyRequestBuilder(
            key=key,
            project_key=self._project_key,
            client=self._client,
        )

    def with_id(self, id: str) -> ByProjectKeySubscriptionsByIDRequestBuilder:
        return ByProjectKeySubscriptionsByIDRequestBuilder(
            id=id,
            project_key=self._project_key,
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
    ) -> typing.Optional["SubscriptionPagedQueryResponse"]:
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
            endpoint=f"/{self._project_key}/subscriptions",
            params=params,
            headers=headers,
            options=options,
        )
        if response.status_code == 200:
            return SubscriptionPagedQueryResponse.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)

    def post(
        self,
        body: "SubscriptionDraft",
        *,
        expand: typing.List["str"] = None,
        headers: typing.Dict[str, str] = None,
        options: typing.Dict[str, typing.Any] = None,
    ) -> typing.Optional["Subscription"]:
        """The creation of a Subscription is eventually consistent, it may take up to a minute before it becomes fully active.
        In order to test that the destination is correctly configured, a test message will be put into the queue.
        If the message could not be delivered, the subscription will not be created.
        The payload of the test message is a notification of type ResourceCreated for the resourceTypeId subscription.
        Currently, a maximum of 25 subscriptions can be created per project.

        """
        headers = {} if headers is None else headers
        response = self._client._post(
            endpoint=f"/{self._project_key}/subscriptions",
            params={"expand": expand},
            json=body.serialize(),
            headers={"Content-Type": "application/json", **headers},
            options=options,
        )
        if response.status_code in (201, 200):
            return Subscription.deserialize(response.json())
        elif response.status_code in (400, 401, 403, 500, 502, 503):
            obj = ErrorResponse.deserialize(response.json())
            raise self._client._create_exception(obj, response)
        elif response.status_code == 404:
            return None
        warnings.warn("Unhandled status code %d" % response.status_code)
