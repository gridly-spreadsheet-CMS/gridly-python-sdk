# coding: utf-8

"""
    Gridly API

    Gridly API documentation  # noqa: E501

    The version of the OpenAPI document: 5.9.0
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


class Reference(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "columnId",
            "gridId",
        }
        
        class properties:
            gridId = schemas.StrSchema
            columnId = schemas.StrSchema
            branchId = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ROW(cls):
                    return cls("row")
                
                @schemas.classproperty
                def CELL(cls):
                    return cls("cell")
            
            
            class selectionType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SINGLE(cls):
                    return cls("single")
                
                @schemas.classproperty
                def MULTIPLE(cls):
                    return cls("multiple")
            __annotations__ = {
                "gridId": gridId,
                "columnId": columnId,
                "branchId": branchId,
                "type": type,
                "selectionType": selectionType,
            }
    
    columnId: MetaOapg.properties.columnId
    gridId: MetaOapg.properties.gridId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gridId"]) -> MetaOapg.properties.gridId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columnId"]) -> MetaOapg.properties.columnId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branchId"]) -> MetaOapg.properties.branchId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selectionType"]) -> MetaOapg.properties.selectionType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gridId", "columnId", "branchId", "type", "selectionType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gridId"]) -> MetaOapg.properties.gridId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columnId"]) -> MetaOapg.properties.columnId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branchId"]) -> typing.Union[MetaOapg.properties.branchId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selectionType"]) -> typing.Union[MetaOapg.properties.selectionType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gridId", "columnId", "branchId", "type", "selectionType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        columnId: typing.Union[MetaOapg.properties.columnId, str, ],
        gridId: typing.Union[MetaOapg.properties.gridId, str, ],
        branchId: typing.Union[MetaOapg.properties.branchId, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        selectionType: typing.Union[MetaOapg.properties.selectionType, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Reference':
        return super().__new__(
            cls,
            *args,
            columnId=columnId,
            gridId=gridId,
            branchId=branchId,
            type=type,
            selectionType=selectionType,
            _configuration=_configuration,
            **kwargs,
        )
