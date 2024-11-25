# gridly.model.branch.Branch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**[columns](#columns)** | list, tuple,  | tuple,  |  | [optional] 
**defaultAccessViewId** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**isMaster** | bool,  | BoolClass,  |  | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**recordIdentifierType** | str,  | str,  |  | [optional] must be one of ["recordId", "pathTagRecordId", ] 
**status** | str,  | str,  |  | [optional] must be one of ["deleted", "active", "inactive", "restoring", "backingUp", "uploading", "importing", "branching", "merging", "duplicating", "clearingRecords", "copying", "updatingWorkflow", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# columns

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ViewColumn**](ViewColumn.md) | [**ViewColumn**](ViewColumn.md) | [**ViewColumn**](ViewColumn.md) |  | 

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

