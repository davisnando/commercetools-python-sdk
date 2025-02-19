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

# Fields


# Marshmallow Schemas
class ImportSummarySchema(helpers.BaseSchema):
    states = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".OperationStatesSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    total = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ImportSummary(**data)


class OperationStatesSchema(helpers.BaseSchema):
    processing = marshmallow.fields.Integer(allow_none=True, missing=None)
    validation_failed = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="validationFailed"
    )
    unresolved = marshmallow.fields.Integer(allow_none=True, missing=None)
    wait_for_master_variant = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="waitForMasterVariant"
    )
    imported = marshmallow.fields.Integer(allow_none=True, missing=None)
    rejected = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.OperationStates(**data)
