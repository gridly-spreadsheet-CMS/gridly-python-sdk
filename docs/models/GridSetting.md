# gridly.model.grid_setting.GridSetting

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**defaultSourceLanguageStatus** | str,  | str,  |  | [optional] must be one of ["unset", "doNotTranslate", "notReadyForTranslation", "readyForTranslation", "locked", "lockAllLanguages", ] 
**translatorCanViewAutomations** | bool,  | BoolClass,  |  | [optional] 
**[categories](#categories)** | list, tuple,  | tuple,  |  | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**createdTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**lastModifiedTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**createdBy** | str,  | str,  |  | [optional] 
**lastModifiedBy** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# categories

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FileCategory**](FileCategory.md) | [**FileCategory**](FileCategory.md) | [**FileCategory**](FileCategory.md) |  | 

# metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

