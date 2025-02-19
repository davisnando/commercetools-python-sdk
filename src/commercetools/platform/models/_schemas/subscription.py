# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..subscription import SubscriptionHealthStatus
from .common import BaseResourceSchema

# Fields


# Marshmallow Schemas
class ChangeSubscriptionSchema(helpers.BaseSchema):
    resource_type_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="resourceTypeId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ChangeSubscription(**data)


class DeliveryFormatSchema(helpers.BaseSchema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.DeliveryFormat(**data)


class CloudEventsFormatSchema(DeliveryFormatSchema):
    cloud_events_version = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="cloudEventsVersion"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CloudEventsFormat(**data)


class DeliveryPayloadSchema(helpers.BaseSchema):
    project_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="projectKey"
    )
    notification_type = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="notificationType"
    )
    resource = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("typeId", "type_id"),
        discriminator_schemas={
            "cart-discount": helpers.absmod(
                __name__, ".cart_discount.CartDiscountReferenceSchema"
            ),
            "cart": helpers.absmod(__name__, ".cart.CartReferenceSchema"),
            "category": helpers.absmod(__name__, ".category.CategoryReferenceSchema"),
            "channel": helpers.absmod(__name__, ".channel.ChannelReferenceSchema"),
            "key-value-document": helpers.absmod(
                __name__, ".custom_object.CustomObjectReferenceSchema"
            ),
            "customer-group": helpers.absmod(
                __name__, ".customer_group.CustomerGroupReferenceSchema"
            ),
            "customer": helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
            "discount-code": helpers.absmod(
                __name__, ".discount_code.DiscountCodeReferenceSchema"
            ),
            "inventory-entry": helpers.absmod(
                __name__, ".inventory.InventoryEntryReferenceSchema"
            ),
            "order-edit": helpers.absmod(
                __name__, ".order_edit.OrderEditReferenceSchema"
            ),
            "order": helpers.absmod(__name__, ".order.OrderReferenceSchema"),
            "payment": helpers.absmod(__name__, ".payment.PaymentReferenceSchema"),
            "product-discount": helpers.absmod(
                __name__, ".product_discount.ProductDiscountReferenceSchema"
            ),
            "product-selection": helpers.absmod(
                __name__, ".product_selection.ProductSelectionReferenceSchema"
            ),
            "product-type": helpers.absmod(
                __name__, ".product_type.ProductTypeReferenceSchema"
            ),
            "product": helpers.absmod(__name__, ".product.ProductReferenceSchema"),
            "review": helpers.absmod(__name__, ".review.ReviewReferenceSchema"),
            "shipping-method": helpers.absmod(
                __name__, ".shipping_method.ShippingMethodReferenceSchema"
            ),
            "shopping-list": helpers.absmod(
                __name__, ".shopping_list.ShoppingListReferenceSchema"
            ),
            "state": helpers.absmod(__name__, ".state.StateReferenceSchema"),
            "store": helpers.absmod(__name__, ".store.StoreReferenceSchema"),
            "tax-category": helpers.absmod(
                __name__, ".tax_category.TaxCategoryReferenceSchema"
            ),
            "type": helpers.absmod(__name__, ".type.TypeReferenceSchema"),
            "zone": helpers.absmod(__name__, ".zone.ZoneReferenceSchema"),
        },
        missing=None,
    )
    resource_user_provided_identifiers = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".message.UserProvidedIdentifiersSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="resourceUserProvidedIdentifiers",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["notification_type"]
        return models.DeliveryPayload(**data)


class DestinationSchema(helpers.BaseSchema):
    type = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.Destination(**data)


class AzureEventGridDestinationSchema(DestinationSchema):
    uri = marshmallow.fields.String(allow_none=True, missing=None)
    access_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="accessKey"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.AzureEventGridDestination(**data)


class AzureServiceBusDestinationSchema(DestinationSchema):
    connection_string = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="connectionString"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.AzureServiceBusDestination(**data)


class EventBridgeDestinationSchema(DestinationSchema):
    region = marshmallow.fields.String(allow_none=True, missing=None)
    account_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="accountId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.EventBridgeDestination(**data)


class GoogleCloudPubSubDestinationSchema(DestinationSchema):
    project_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="projectId"
    )
    topic = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.GoogleCloudPubSubDestination(**data)


class IronMqDestinationSchema(DestinationSchema):
    uri = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.IronMqDestination(**data)


class MessageDeliveryPayloadSchema(DeliveryPayloadSchema):
    id = marshmallow.fields.String(allow_none=True, missing=None)
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    created_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="createdAt"
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="lastModifiedAt"
    )
    sequence_number = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="sequenceNumber"
    )
    resource_version = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="resourceVersion"
    )
    payload_not_included = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".PayloadNotIncludedSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="payloadNotIncluded",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["notification_type"]
        return models.MessageDeliveryPayload(**data)


class MessageSubscriptionSchema(helpers.BaseSchema):
    resource_type_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="resourceTypeId"
    )
    types = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.MessageSubscription(**data)


class PayloadNotIncludedSchema(helpers.BaseSchema):
    reason = marshmallow.fields.String(allow_none=True, missing=None)
    payload_type = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="payloadType"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.PayloadNotIncluded(**data)


class PlatformFormatSchema(DeliveryFormatSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.PlatformFormat(**data)


class ResourceCreatedDeliveryPayloadSchema(DeliveryPayloadSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="modifiedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["notification_type"]
        return models.ResourceCreatedDeliveryPayload(**data)


class ResourceDeletedDeliveryPayloadSchema(DeliveryPayloadSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="modifiedAt"
    )
    data_erasure = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="dataErasure",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["notification_type"]
        return models.ResourceDeletedDeliveryPayload(**data)


class ResourceUpdatedDeliveryPayloadSchema(DeliveryPayloadSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    old_version = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="oldVersion"
    )
    modified_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="modifiedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["notification_type"]
        return models.ResourceUpdatedDeliveryPayload(**data)


class SnsDestinationSchema(DestinationSchema):
    access_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="accessKey"
    )
    access_secret = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="accessSecret"
    )
    topic_arn = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="topicArn"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.SnsDestination(**data)


class SqsDestinationSchema(DestinationSchema):
    access_key = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="accessKey"
    )
    access_secret = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="accessSecret"
    )
    queue_url = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="queueUrl"
    )
    region = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.SqsDestination(**data)


class SubscriptionSchema(BaseResourceSchema):
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="createdBy",
    )
    changes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ChangeSubscriptionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    destination = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "EventGrid": helpers.absmod(__name__, ".AzureEventGridDestinationSchema"),
            "AzureServiceBus": helpers.absmod(
                __name__, ".AzureServiceBusDestinationSchema"
            ),
            "EventBridge": helpers.absmod(__name__, ".EventBridgeDestinationSchema"),
            "GoogleCloudPubSub": helpers.absmod(
                __name__, ".GoogleCloudPubSubDestinationSchema"
            ),
            "IronMQ": helpers.absmod(__name__, ".IronMqDestinationSchema"),
            "SNS": helpers.absmod(__name__, ".SnsDestinationSchema"),
            "SQS": helpers.absmod(__name__, ".SqsDestinationSchema"),
        },
        missing=None,
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    messages = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MessageSubscriptionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    format = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "CloudEvents": helpers.absmod(__name__, ".CloudEventsFormatSchema"),
            "Platform": helpers.absmod(__name__, ".PlatformFormatSchema"),
        },
        missing=None,
    )
    status = marshmallow_enum.EnumField(
        SubscriptionHealthStatus, by_value=True, allow_none=True, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Subscription(**data)


class SubscriptionDraftSchema(helpers.BaseSchema):
    changes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ChangeSubscriptionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    destination = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "EventGrid": helpers.absmod(__name__, ".AzureEventGridDestinationSchema"),
            "AzureServiceBus": helpers.absmod(
                __name__, ".AzureServiceBusDestinationSchema"
            ),
            "EventBridge": helpers.absmod(__name__, ".EventBridgeDestinationSchema"),
            "GoogleCloudPubSub": helpers.absmod(
                __name__, ".GoogleCloudPubSubDestinationSchema"
            ),
            "IronMQ": helpers.absmod(__name__, ".IronMqDestinationSchema"),
            "SNS": helpers.absmod(__name__, ".SnsDestinationSchema"),
            "SQS": helpers.absmod(__name__, ".SqsDestinationSchema"),
        },
        missing=None,
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    messages = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MessageSubscriptionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    format = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "CloudEvents": helpers.absmod(__name__, ".CloudEventsFormatSchema"),
            "Platform": helpers.absmod(__name__, ".PlatformFormatSchema"),
        },
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SubscriptionDraft(**data)


class SubscriptionPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SubscriptionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SubscriptionPagedQueryResponse(**data)


class SubscriptionUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeDestination": helpers.absmod(
                    __name__, ".SubscriptionChangeDestinationActionSchema"
                ),
                "setChanges": helpers.absmod(
                    __name__, ".SubscriptionSetChangesActionSchema"
                ),
                "setKey": helpers.absmod(__name__, ".SubscriptionSetKeyActionSchema"),
                "setMessages": helpers.absmod(
                    __name__, ".SubscriptionSetMessagesActionSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SubscriptionUpdate(**data)


class SubscriptionUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.SubscriptionUpdateAction(**data)


class SubscriptionChangeDestinationActionSchema(SubscriptionUpdateActionSchema):
    destination = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "EventGrid": helpers.absmod(__name__, ".AzureEventGridDestinationSchema"),
            "AzureServiceBus": helpers.absmod(
                __name__, ".AzureServiceBusDestinationSchema"
            ),
            "EventBridge": helpers.absmod(__name__, ".EventBridgeDestinationSchema"),
            "GoogleCloudPubSub": helpers.absmod(
                __name__, ".GoogleCloudPubSubDestinationSchema"
            ),
            "IronMQ": helpers.absmod(__name__, ".IronMqDestinationSchema"),
            "SNS": helpers.absmod(__name__, ".SnsDestinationSchema"),
            "SQS": helpers.absmod(__name__, ".SqsDestinationSchema"),
        },
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.SubscriptionChangeDestinationAction(**data)


class SubscriptionSetChangesActionSchema(SubscriptionUpdateActionSchema):
    changes = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ChangeSubscriptionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.SubscriptionSetChangesAction(**data)


class SubscriptionSetKeyActionSchema(SubscriptionUpdateActionSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.SubscriptionSetKeyAction(**data)


class SubscriptionSetMessagesActionSchema(SubscriptionUpdateActionSchema):
    messages = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".MessageSubscriptionSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.SubscriptionSetMessagesAction(**data)
