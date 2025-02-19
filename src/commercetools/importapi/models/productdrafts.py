# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import (
        Asset,
        CategoryKeyReference,
        ChannelKeyReference,
        CustomerGroupKeyReference,
        DiscountedPrice,
        Image,
        LocalizedString,
        PriceTier,
        ProductTypeKeyReference,
        StateKeyReference,
        TaxCategoryKeyReference,
        TypedMoney,
    )
    from .customfields import Custom
    from .products import SearchKeywords
    from .productvariants import Attribute

__all__ = ["PriceDraftImport", "ProductDraftImport", "ProductVariantDraftImport"]


class ProductDraftImport(ImportResource):
    """The representation of a Product Draft for the import purpose."""

    #: The `productType` of a [Product](/../api/projects/products#product).
    #: Maps to `Product.productType`.
    #: The Reference to the [ProductType](/../api/projects/productTypes#producttype) with which the ProductDraft is associated.
    #: If referenced ProductType does not exist, the `state` of the [ImportOperation](/import-operation#importoperation) will be set to `unresolved` until the necessary ProductType is created.
    product_type: "ProductTypeKeyReference"
    name: "LocalizedString"
    #: Human-readable identifiers usually used as deep-link URL to the related product. Each slug must be unique across a project,
    #: but a product can have the same slug for different languages. Allowed are alphabetic, numeric, underscore (_) and hyphen (-) characters.
    slug: "LocalizedString"
    #: Maps to `Product.description`.
    description: typing.Optional["LocalizedString"]
    #: The Reference to the [Categories](/../api/projects/categories#category) with which the ProductDraft is associated.
    #: If referenced Categories do not exist, the `state` of the [ImportOperation](/import-operation#importoperation) will be set to `unresolved` until the necessary Categories are created.
    categories: typing.Optional[typing.List["CategoryKeyReference"]]
    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    meta_title: typing.Optional["LocalizedString"]
    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    meta_description: typing.Optional["LocalizedString"]
    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    meta_keywords: typing.Optional["LocalizedString"]
    #: The master Product variant.
    #: Required if the `variants` array contains a Product Variant.
    master_variant: typing.Optional["ProductVariantDraftImport"]
    #: An array of related Product Variants.
    variants: typing.Optional[typing.List["ProductVariantDraftImport"]]
    #: The Reference to the [TaxCategory](/../api/projects/taxCategories#taxcategory) with which the ProductDraft is associated.
    #: If referenced TaxCategory does not exist, the `state` of the [ImportOperation](/import-operation#importoperation) will be set to `unresolved` until the necessary TaxCategory is created.
    tax_category: typing.Optional["TaxCategoryKeyReference"]
    #: Search keywords are primarily used by the suggester but are also considered for the full-text search. SearchKeywords is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag). The value to a language tag key is an array of SearchKeyword for the specific language.
    #: ```json
    #: {
    #:   "en": [
    #:     { "text": "Multi tool" },
    #:     { "text": "Swiss Army Knife", "suggestTokenizer": { "type": "whitespace" } }
    #:   ],
    #:   "de": [
    #:     {
    #:       "text": "Schweizer Messer",
    #:       "suggestTokenizer": {
    #:         "type": "custom",
    #:         "inputs": ["schweizer messer", "offiziersmesser", "sackmesser"]
    #:       }
    #:     }
    #:   ]
    #: }
    #: ```
    search_keywords: typing.Optional["SearchKeywords"]
    #: The Reference to the [State](/../api/projects/states#state) with which the ProductDraft is associated.
    #: If referenced State does not exist, the `state` of the [ImportOperation](/import-operation#importoperation) will be set to `unresolved` until the necessary State is created.
    state: typing.Optional["StateKeyReference"]
    #: If `publish` is set to either `true` or `false`, both staged and current projections are set to the same value provided by the import data.
    #: If `publish` is not set, the staged projection is set to the provided import data, but the current projection stays unchanged.
    #: However, if the import data contains no update, that is, if it matches the staged projection of the existing Product in the platform, the import induces no change in the existing Product whether `publish` is set or not.
    publish: typing.Optional[bool]

    def __init__(
        self,
        *,
        key: str,
        product_type: "ProductTypeKeyReference",
        name: "LocalizedString",
        slug: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        categories: typing.Optional[typing.List["CategoryKeyReference"]] = None,
        meta_title: typing.Optional["LocalizedString"] = None,
        meta_description: typing.Optional["LocalizedString"] = None,
        meta_keywords: typing.Optional["LocalizedString"] = None,
        master_variant: typing.Optional["ProductVariantDraftImport"] = None,
        variants: typing.Optional[typing.List["ProductVariantDraftImport"]] = None,
        tax_category: typing.Optional["TaxCategoryKeyReference"] = None,
        search_keywords: typing.Optional["SearchKeywords"] = None,
        state: typing.Optional["StateKeyReference"] = None,
        publish: typing.Optional[bool] = None
    ):
        self.product_type = product_type
        self.name = name
        self.slug = slug
        self.description = description
        self.categories = categories
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.master_variant = master_variant
        self.variants = variants
        self.tax_category = tax_category
        self.search_keywords = search_keywords
        self.state = state
        self.publish = publish

        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductDraftImport":
        from ._schemas.productdrafts import ProductDraftImportSchema

        return ProductDraftImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productdrafts import ProductDraftImportSchema

        return ProductDraftImportSchema().dump(self)


class ProductVariantDraftImport(_BaseType):
    """The representation of a Product Variant Draft for the import purpose."""

    sku: typing.Optional[str]
    key: str
    prices: typing.Optional[typing.List["PriceDraftImport"]]
    attributes: typing.Optional[typing.List["Attribute"]]
    images: typing.Optional[typing.List["Image"]]
    assets: typing.Optional[typing.List["Asset"]]

    def __init__(
        self,
        *,
        sku: typing.Optional[str] = None,
        key: str,
        prices: typing.Optional[typing.List["PriceDraftImport"]] = None,
        attributes: typing.Optional[typing.List["Attribute"]] = None,
        images: typing.Optional[typing.List["Image"]] = None,
        assets: typing.Optional[typing.List["Asset"]] = None
    ):
        self.sku = sku
        self.key = key
        self.prices = prices
        self.attributes = attributes
        self.images = images
        self.assets = assets

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantDraftImport":
        from ._schemas.productdrafts import ProductVariantDraftImportSchema

        return ProductVariantDraftImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productdrafts import ProductVariantDraftImportSchema

        return ProductVariantDraftImportSchema().dump(self)


class PriceDraftImport(_BaseType):
    """The representation of a Price Draft for the import purpose."""

    value: "TypedMoney"
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: typing.Optional[str]
    #: References a customer group by key.
    customer_group: typing.Optional["CustomerGroupKeyReference"]
    #: References a channel by key.
    channel: typing.Optional["ChannelKeyReference"]
    valid_from: typing.Optional[datetime.datetime]
    valid_until: typing.Optional[datetime.datetime]
    #: The custom fields for this category.
    custom: typing.Optional["Custom"]
    #: Sets a discounted price from an external service.
    discounted: typing.Optional["DiscountedPrice"]
    #: The tiered prices for this price.
    tiers: typing.Optional[typing.List["PriceTier"]]
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        value: "TypedMoney",
        country: typing.Optional[str] = None,
        customer_group: typing.Optional["CustomerGroupKeyReference"] = None,
        channel: typing.Optional["ChannelKeyReference"] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["Custom"] = None,
        discounted: typing.Optional["DiscountedPrice"] = None,
        tiers: typing.Optional[typing.List["PriceTier"]] = None,
        key: typing.Optional[str] = None
    ):
        self.value = value
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.custom = custom
        self.discounted = discounted
        self.tiers = tiers
        self.key = key

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceDraftImport":
        from ._schemas.productdrafts import PriceDraftImportSchema

        return PriceDraftImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.productdrafts import PriceDraftImportSchema

        return PriceDraftImportSchema().dump(self)
