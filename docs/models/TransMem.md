# gridly.model.trans_mem.TransMem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**id** | str,  | str,  |  | [optional] 
**[projectIds](#projectIds)** | list, tuple,  | tuple,  |  | [optional] 
**isDisabled** | bool,  | BoolClass,  |  | [optional] 
**isPausedConsuming** | bool,  | BoolClass,  |  | [optional] 
**populateTranslationStatus** | [**TranslationStatus**](TranslationStatus.md) | [**TranslationStatus**](TranslationStatus.md) |  | [optional] 
**contextLookup** | bool,  | BoolClass,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**fuzzyMatch** | bool,  | BoolClass,  |  | [optional] 
**allowAlternative** | bool,  | BoolClass,  |  | [optional] 
**allowAlternativeHasSameRecordId** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# projectIds

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

