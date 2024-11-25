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


class FetchRecordHistoryRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class columnIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'columnIds':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            query = schemas.StrSchema
            sort = schemas.StrSchema
            
            
            class groupBy(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'groupBy':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            page = schemas.StrSchema
            fetchOptions = schemas.StrSchema
            includeSystemUser = schemas.BoolSchema
            __annotations__ = {
                "columnIds": columnIds,
                "query": query,
                "sort": sort,
                "groupBy": groupBy,
                "page": page,
                "fetchOptions": fetchOptions,
                "includeSystemUser": includeSystemUser,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columnIds"]) -> MetaOapg.properties.columnIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> MetaOapg.properties.sort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupBy"]) -> MetaOapg.properties.groupBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fetchOptions"]) -> MetaOapg.properties.fetchOptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeSystemUser"]) -> MetaOapg.properties.includeSystemUser: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["columnIds", "query", "sort", "groupBy", "page", "fetchOptions", "includeSystemUser", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columnIds"]) -> typing.Union[MetaOapg.properties.columnIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> typing.Union[MetaOapg.properties.sort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupBy"]) -> typing.Union[MetaOapg.properties.groupBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fetchOptions"]) -> typing.Union[MetaOapg.properties.fetchOptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeSystemUser"]) -> typing.Union[MetaOapg.properties.includeSystemUser, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["columnIds", "query", "sort", "groupBy", "page", "fetchOptions", "includeSystemUser", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        columnIds: typing.Union[MetaOapg.properties.columnIds, list, tuple, schemas.Unset] = schemas.unset,
        query: typing.Union[MetaOapg.properties.query, str, schemas.Unset] = schemas.unset,
        sort: typing.Union[MetaOapg.properties.sort, str, schemas.Unset] = schemas.unset,
        groupBy: typing.Union[MetaOapg.properties.groupBy, list, tuple, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, str, schemas.Unset] = schemas.unset,
        fetchOptions: typing.Union[MetaOapg.properties.fetchOptions, str, schemas.Unset] = schemas.unset,
        includeSystemUser: typing.Union[MetaOapg.properties.includeSystemUser, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FetchRecordHistoryRequest':
        return super().__new__(
            cls,
            *args,
            columnIds=columnIds,
            query=query,
            sort=sort,
            groupBy=groupBy,
            page=page,
            fetchOptions=fetchOptions,
            includeSystemUser=includeSystemUser,
            _configuration=_configuration,
            **kwargs,
        )
