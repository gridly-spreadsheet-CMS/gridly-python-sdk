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


class MergeRecordConflict(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class cells(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MergeCellConflict']:
                        return MergeCellConflict
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MergeCellConflict'], typing.List['MergeCellConflict']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cells':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MergeCellConflict':
                    return super().__getitem__(i)
            pathTag = schemas.StrSchema
            recordId = schemas.StrSchema
            __annotations__ = {
                "cells": cells,
                "pathTag": pathTag,
                "recordId": recordId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cells"]) -> MetaOapg.properties.cells: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pathTag"]) -> MetaOapg.properties.pathTag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recordId"]) -> MetaOapg.properties.recordId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cells", "pathTag", "recordId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cells"]) -> typing.Union[MetaOapg.properties.cells, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pathTag"]) -> typing.Union[MetaOapg.properties.pathTag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recordId"]) -> typing.Union[MetaOapg.properties.recordId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cells", "pathTag", "recordId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cells: typing.Union[MetaOapg.properties.cells, list, tuple, schemas.Unset] = schemas.unset,
        pathTag: typing.Union[MetaOapg.properties.pathTag, str, schemas.Unset] = schemas.unset,
        recordId: typing.Union[MetaOapg.properties.recordId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MergeRecordConflict':
        return super().__new__(
            cls,
            *args,
            cells=cells,
            pathTag=pathTag,
            recordId=recordId,
            _configuration=_configuration,
            **kwargs,
        )

from gridly.model.merge_cell_conflict import MergeCellConflict
