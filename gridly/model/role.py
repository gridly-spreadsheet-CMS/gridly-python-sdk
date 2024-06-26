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


class Role(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            name = schemas.StrSchema
            title = schemas.StrSchema
            type = schemas.StrSchema
            level = schemas.StrSchema
            
            
            class privileges(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    
                    @staticmethod
                    def items() -> typing.Type['Privilege']:
                        return Privilege
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Privilege'], typing.List['Privilege']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'privileges':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Privilege':
                    return super().__getitem__(i)
            
            
            class privilegeIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'privilegeIds':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            isSystemRole = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "title": title,
                "type": type,
                "level": level,
                "privileges": privileges,
                "privilegeIds": privilegeIds,
                "isSystemRole": isSystemRole,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privileges"]) -> MetaOapg.properties.privileges: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privilegeIds"]) -> MetaOapg.properties.privilegeIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSystemRole"]) -> MetaOapg.properties.isSystemRole: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "title", "type", "level", "privileges", "privilegeIds", "isSystemRole", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> typing.Union[MetaOapg.properties.level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privileges"]) -> typing.Union[MetaOapg.properties.privileges, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privilegeIds"]) -> typing.Union[MetaOapg.properties.privilegeIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSystemRole"]) -> typing.Union[MetaOapg.properties.isSystemRole, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "title", "type", "level", "privileges", "privilegeIds", "isSystemRole", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        level: typing.Union[MetaOapg.properties.level, str, schemas.Unset] = schemas.unset,
        privileges: typing.Union[MetaOapg.properties.privileges, list, tuple, schemas.Unset] = schemas.unset,
        privilegeIds: typing.Union[MetaOapg.properties.privilegeIds, list, tuple, schemas.Unset] = schemas.unset,
        isSystemRole: typing.Union[MetaOapg.properties.isSystemRole, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Role':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            title=title,
            type=type,
            level=level,
            privileges=privileges,
            privilegeIds=privilegeIds,
            isSystemRole=isSystemRole,
            _configuration=_configuration,
            **kwargs,
        )

from gridly.model.privilege import Privilege
