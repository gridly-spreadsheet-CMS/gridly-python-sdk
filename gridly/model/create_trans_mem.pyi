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


class CreateTransMem(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            description = schemas.StrSchema
            
            
            class projectIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'projectIds':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            fuzzyMatch = schemas.BoolSchema
            isDisabled = schemas.BoolSchema
            isPausedConsuming = schemas.BoolSchema
            contextLookup = schemas.BoolSchema
        
            @staticmethod
            def populateTranslationStatus() -> typing.Type['TranslationStatus']:
                return TranslationStatus
            allowAlternative = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "description": description,
                "projectIds": projectIds,
                "fuzzyMatch": fuzzyMatch,
                "isDisabled": isDisabled,
                "isPausedConsuming": isPausedConsuming,
                "contextLookup": contextLookup,
                "populateTranslationStatus": populateTranslationStatus,
                "allowAlternative": allowAlternative,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectIds"]) -> MetaOapg.properties.projectIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fuzzyMatch"]) -> MetaOapg.properties.fuzzyMatch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDisabled"]) -> MetaOapg.properties.isDisabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPausedConsuming"]) -> MetaOapg.properties.isPausedConsuming: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextLookup"]) -> MetaOapg.properties.contextLookup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["populateTranslationStatus"]) -> 'TranslationStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowAlternative"]) -> MetaOapg.properties.allowAlternative: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "projectIds", "fuzzyMatch", "isDisabled", "isPausedConsuming", "contextLookup", "populateTranslationStatus", "allowAlternative", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectIds"]) -> typing.Union[MetaOapg.properties.projectIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fuzzyMatch"]) -> typing.Union[MetaOapg.properties.fuzzyMatch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDisabled"]) -> typing.Union[MetaOapg.properties.isDisabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPausedConsuming"]) -> typing.Union[MetaOapg.properties.isPausedConsuming, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextLookup"]) -> typing.Union[MetaOapg.properties.contextLookup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["populateTranslationStatus"]) -> typing.Union['TranslationStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowAlternative"]) -> typing.Union[MetaOapg.properties.allowAlternative, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "projectIds", "fuzzyMatch", "isDisabled", "isPausedConsuming", "contextLookup", "populateTranslationStatus", "allowAlternative", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        projectIds: typing.Union[MetaOapg.properties.projectIds, list, tuple, schemas.Unset] = schemas.unset,
        fuzzyMatch: typing.Union[MetaOapg.properties.fuzzyMatch, bool, schemas.Unset] = schemas.unset,
        isDisabled: typing.Union[MetaOapg.properties.isDisabled, bool, schemas.Unset] = schemas.unset,
        isPausedConsuming: typing.Union[MetaOapg.properties.isPausedConsuming, bool, schemas.Unset] = schemas.unset,
        contextLookup: typing.Union[MetaOapg.properties.contextLookup, bool, schemas.Unset] = schemas.unset,
        populateTranslationStatus: typing.Union['TranslationStatus', schemas.Unset] = schemas.unset,
        allowAlternative: typing.Union[MetaOapg.properties.allowAlternative, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateTransMem':
        return super().__new__(
            cls,
            *args,
            name=name,
            description=description,
            projectIds=projectIds,
            fuzzyMatch=fuzzyMatch,
            isDisabled=isDisabled,
            isPausedConsuming=isPausedConsuming,
            contextLookup=contextLookup,
            populateTranslationStatus=populateTranslationStatus,
            allowAlternative=allowAlternative,
            _configuration=_configuration,
            **kwargs,
        )

from gridly.model.translation_status import TranslationStatus
