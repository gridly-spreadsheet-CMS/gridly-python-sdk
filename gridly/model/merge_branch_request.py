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


class MergeBranchRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class mergeRecordOptions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "add": "ADD",
                                "update": "UPDATE",
                                "delete": "DELETE",
                                "override": "OVERRIDE",
                            }
                        
                        @schemas.classproperty
                        def ADD(cls):
                            return cls("add")
                        
                        @schemas.classproperty
                        def UPDATE(cls):
                            return cls("update")
                        
                        @schemas.classproperty
                        def DELETE(cls):
                            return cls("delete")
                        
                        @schemas.classproperty
                        def OVERRIDE(cls):
                            return cls("override")
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mergeRecordOptions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class mergeRecordConflicts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 2000
                    min_items = 0
                    
                    @staticmethod
                    def items() -> typing.Type['MergeRecordConflict']:
                        return MergeRecordConflict
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MergeRecordConflict'], typing.List['MergeRecordConflict']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mergeRecordConflicts':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MergeRecordConflict':
                    return super().__getitem__(i)
            useLastMergeResolve = schemas.BoolSchema
            
            
            class query(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FilterField']:
                        return FilterField
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FilterField'], typing.List['FilterField']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'query':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FilterField':
                    return super().__getitem__(i)
            __annotations__ = {
                "mergeRecordOptions": mergeRecordOptions,
                "mergeRecordConflicts": mergeRecordConflicts,
                "useLastMergeResolve": useLastMergeResolve,
                "query": query,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mergeRecordOptions"]) -> MetaOapg.properties.mergeRecordOptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mergeRecordConflicts"]) -> MetaOapg.properties.mergeRecordConflicts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useLastMergeResolve"]) -> MetaOapg.properties.useLastMergeResolve: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["mergeRecordOptions", "mergeRecordConflicts", "useLastMergeResolve", "query", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mergeRecordOptions"]) -> typing.Union[MetaOapg.properties.mergeRecordOptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mergeRecordConflicts"]) -> typing.Union[MetaOapg.properties.mergeRecordConflicts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useLastMergeResolve"]) -> typing.Union[MetaOapg.properties.useLastMergeResolve, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mergeRecordOptions", "mergeRecordConflicts", "useLastMergeResolve", "query", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        mergeRecordOptions: typing.Union[MetaOapg.properties.mergeRecordOptions, list, tuple, schemas.Unset] = schemas.unset,
        mergeRecordConflicts: typing.Union[MetaOapg.properties.mergeRecordConflicts, list, tuple, schemas.Unset] = schemas.unset,
        useLastMergeResolve: typing.Union[MetaOapg.properties.useLastMergeResolve, bool, schemas.Unset] = schemas.unset,
        query: typing.Union[MetaOapg.properties.query, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MergeBranchRequest':
        return super().__new__(
            cls,
            *args,
            mergeRecordOptions=mergeRecordOptions,
            mergeRecordConflicts=mergeRecordConflicts,
            useLastMergeResolve=useLastMergeResolve,
            query=query,
            _configuration=_configuration,
            **kwargs,
        )

from gridly.model.filter_field import FilterField
from gridly.model.merge_record_conflict import MergeRecordConflict