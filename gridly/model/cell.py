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


class Cell(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            columnId = schemas.StrSchema
            
            
            class dependencyStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "upToDate": "UP_TO_DATE",
                        "outOfDate": "OUT_OF_DATE",
                        "unset": "UNSET",
                    }
                
                @schemas.classproperty
                def UP_TO_DATE(cls):
                    return cls("upToDate")
                
                @schemas.classproperty
                def OUT_OF_DATE(cls):
                    return cls("outOfDate")
                
                @schemas.classproperty
                def UNSET(cls):
                    return cls("unset")
            lengthLimit = schemas.Int32Schema
            
            
            class referencedIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'referencedIds':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class sourceStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "unset": "UNSET",
                        "doNotTranslate": "DO_NOT_TRANSLATE",
                        "notReadyForTranslation": "NOT_READY_FOR_TRANSLATION",
                        "readyForTranslation": "READY_FOR_TRANSLATION",
                        "locked": "LOCKED",
                        "lockAllLanguages": "LOCK_ALL_LANGUAGES",
                    }
                
                @schemas.classproperty
                def UNSET(cls):
                    return cls("unset")
                
                @schemas.classproperty
                def DO_NOT_TRANSLATE(cls):
                    return cls("doNotTranslate")
                
                @schemas.classproperty
                def NOT_READY_FOR_TRANSLATION(cls):
                    return cls("notReadyForTranslation")
                
                @schemas.classproperty
                def READY_FOR_TRANSLATION(cls):
                    return cls("readyForTranslation")
                
                @schemas.classproperty
                def LOCKED(cls):
                    return cls("locked")
                
                @schemas.classproperty
                def LOCK_ALL_LANGUAGES(cls):
                    return cls("lockAllLanguages")
            tm = schemas.BoolSchema
            value = schemas.Schema
            __annotations__ = {
                "columnId": columnId,
                "dependencyStatus": dependencyStatus,
                "lengthLimit": lengthLimit,
                "referencedIds": referencedIds,
                "sourceStatus": sourceStatus,
                "tm": tm,
                "value": value,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columnId"]) -> MetaOapg.properties.columnId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dependencyStatus"]) -> MetaOapg.properties.dependencyStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lengthLimit"]) -> MetaOapg.properties.lengthLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referencedIds"]) -> MetaOapg.properties.referencedIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceStatus"]) -> MetaOapg.properties.sourceStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tm"]) -> MetaOapg.properties.tm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["columnId", "dependencyStatus", "lengthLimit", "referencedIds", "sourceStatus", "tm", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columnId"]) -> typing.Union[MetaOapg.properties.columnId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dependencyStatus"]) -> typing.Union[MetaOapg.properties.dependencyStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lengthLimit"]) -> typing.Union[MetaOapg.properties.lengthLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referencedIds"]) -> typing.Union[MetaOapg.properties.referencedIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceStatus"]) -> typing.Union[MetaOapg.properties.sourceStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tm"]) -> typing.Union[MetaOapg.properties.tm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["columnId", "dependencyStatus", "lengthLimit", "referencedIds", "sourceStatus", "tm", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        columnId: typing.Union[MetaOapg.properties.columnId, str, schemas.Unset] = schemas.unset,
        dependencyStatus: typing.Union[MetaOapg.properties.dependencyStatus, str, schemas.Unset] = schemas.unset,
        lengthLimit: typing.Union[MetaOapg.properties.lengthLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        referencedIds: typing.Union[MetaOapg.properties.referencedIds, list, tuple, schemas.Unset] = schemas.unset,
        sourceStatus: typing.Union[MetaOapg.properties.sourceStatus, str, schemas.Unset] = schemas.unset,
        tm: typing.Union[MetaOapg.properties.tm, bool, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Cell':
        return super().__new__(
            cls,
            *args,
            columnId=columnId,
            dependencyStatus=dependencyStatus,
            lengthLimit=lengthLimit,
            referencedIds=referencedIds,
            sourceStatus=sourceStatus,
            tm=tm,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )
