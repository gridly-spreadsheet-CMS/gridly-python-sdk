# coding: utf-8

"""
    Gridly API

    Gridly API documentation  # noqa: E501

    The version of the OpenAPI document: 4.33.0
    Contact: support@gridly.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gridly import schemas  # noqa: F401


class ImportOption(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ADD": "ADD",
            "UPDATE": "UPDATE",
            "UPDATE_ONLY": "UPDATE_ONLY",
        }
    
    @schemas.classproperty
    def ADD(cls):
        return cls("ADD")
    
    @schemas.classproperty
    def UPDATE(cls):
        return cls("UPDATE")
    
    @schemas.classproperty
    def UPDATE_ONLY(cls):
        return cls("UPDATE_ONLY")
