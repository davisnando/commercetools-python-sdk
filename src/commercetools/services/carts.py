# DO NOT EDIT! This file is automatically generated
import typing

from marshmallow import fields

from commercetools._schemas._cart import (
    CartDraftSchema,
    CartPagedQueryResponseSchema,
    CartSchema,
    CartUpdateSchema,
    ReplicaCartDraftSchema,
)
from commercetools.helpers import OptionalList, RemoveEmptyValuesMixin
from commercetools.types._cart import (
    Cart,
    CartDraft,
    CartPagedQueryResponse,
    CartUpdate,
    CartUpdateAction,
    ReplicaCartDraft,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _CartQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    customer_id = OptionalList(fields.String(), data_key="customerId", required=False)


class _CartUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _CartDeleteSchema(
    traits.VersionedSchema, traits.ExpandableSchema, traits.DataErasureSchema
):
    pass


class CartService(abstract.AbstractService):
    """A shopping cart holds product variants and can be ordered."""

    def get_by_customer_id(
        self, customer_id: str, *, expand: OptionalListStr = None
    ) -> Cart:
        """Retrieves the active cart of the customer that has been modified most
        recently.

        It does not consider carts with CartOrigin Merchant. If no active cart
        exists, a 404 Not Found error is returned.  The cart may not contain up-
        to-date prices, discounts etc. If you want to ensure they're up-to-date,
        send an Update request with the Recalculate update action instead.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"carts/customer-id={customer_id}",
            params=params,
            schema_cls=CartSchema,
        )

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> Cart:
        """The cart may not contain up-to-date prices, discounts etc.

        If you want to ensure they're up-to-date, send an Update request with the
        Recalculate update action instead.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"carts/{id}", params=params, schema_cls=CartSchema
        )

    def query(
        self,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
        customer_id: str = None,
    ) -> CartPagedQueryResponse:
        """A shopping cart holds product variants and can be ordered.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "with_total": with_total,
                "where": where,
                "predicate_var": predicate_var,
                "customer_id": customer_id,
            },
            _CartQuerySchema,
        )
        return self._client._get(
            endpoint="carts", params=params, schema_cls=CartPagedQueryResponseSchema
        )

    def create(self, draft: CartDraft, *, expand: OptionalListStr = None) -> Cart:
        """Creating a cart can fail with an InvalidOperation if the referenced
        shipping method in the

        CartDraft has a predicate which does not match the cart.   A shopping
        cart holds product variants and can be ordered.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="carts",
            params=params,
            data_object=draft,
            request_schema_cls=CartDraftSchema,
            response_schema_cls=CartSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[CartUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> Cart:
        params = self._serialize_params({"expand": expand}, _CartUpdateSchema)
        update_action = CartUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"carts/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=CartUpdateSchema,
            response_schema_cls=CartSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> Cart:
        params = self._serialize_params(
            {"version": version, "expand": expand, "data_erasure": data_erasure},
            _CartDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"carts/{id}",
            params=params,
            response_schema_cls=CartSchema,
            force_delete=force_delete,
        )

    def replicate(self, draft: ReplicaCartDraft) -> Cart:
        params: typing.Dict[str, str] = {}
        return self._client._post(
            endpoint="carts/replicate",
            params=params,
            data_object=draft,
            request_schema_cls=ReplicaCartDraftSchema,
            response_schema_cls=CartSchema,
        )
