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


class UpdateDependency(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "targetColumnId",
            "sourceColumnId",
        }
        
        class properties:
            targetColumnId = schemas.StrSchema
            sourceColumnId = schemas.StrSchema
            
            
            class newId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^(?!_)\w+$',  # noqa: E501
                    }]
            __annotations__ = {
                "targetColumnId": targetColumnId,
                "sourceColumnId": sourceColumnId,
                "newId": newId,
            }
    
    targetColumnId: MetaOapg.properties.targetColumnId
    sourceColumnId: MetaOapg.properties.sourceColumnId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetColumnId"]) -> MetaOapg.properties.targetColumnId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceColumnId"]) -> MetaOapg.properties.sourceColumnId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["newId"]) -> MetaOapg.properties.newId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["targetColumnId", "sourceColumnId", "newId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetColumnId"]) -> MetaOapg.properties.targetColumnId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceColumnId"]) -> MetaOapg.properties.sourceColumnId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["newId"]) -> typing.Union[MetaOapg.properties.newId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["targetColumnId", "sourceColumnId", "newId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        targetColumnId: typing.Union[MetaOapg.properties.targetColumnId, str, ],
        sourceColumnId: typing.Union[MetaOapg.properties.sourceColumnId, str, ],
        newId: typing.Union[MetaOapg.properties.newId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateDependency':
        return super().__new__(
            cls,
            *args,
            targetColumnId=targetColumnId,
            sourceColumnId=sourceColumnId,
            newId=newId,
            _configuration=_configuration,
            **kwargs,
        )
