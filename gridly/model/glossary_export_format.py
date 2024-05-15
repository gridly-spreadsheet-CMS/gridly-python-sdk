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


class GlossaryExportFormat(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "csv": "CSV",
            "xls": "XLS",
            "xlsx": "XLSX",
            "tbx": "TBX",
        }
    
    @schemas.classproperty
    def CSV(cls):
        return cls("csv")
    
    @schemas.classproperty
    def XLS(cls):
        return cls("xls")
    
    @schemas.classproperty
    def XLSX(cls):
        return cls("xlsx")
    
    @schemas.classproperty
    def TBX(cls):
        return cls("tbx")
