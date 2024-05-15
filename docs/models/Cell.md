# gridly.model.cell.Cell

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**columnId** | str,  | str,  |  | [optional] 
**dependencyStatus** | str,  | str,  |  | [optional] must be one of ["upToDate", "outOfDate", "unset", ] 
**lengthLimit** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[referencedIds](#referencedIds)** | list, tuple,  | tuple,  |  | [optional] 
**sourceStatus** | str,  | str,  |  | [optional] must be one of ["unset", "doNotTranslate", "notReadyForTranslation", "readyForTranslation", "locked", "lockAllLanguages", ] 
**tm** | bool,  | BoolClass,  |  | [optional] 
**value** |  |  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# referencedIds

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

