# gridly.model.filter_field.FilterField

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operator** | str,  | str,  |  | must be one of ["isNull", "isNotNull", "isEmpty", "isNotEmpty", "contains", "notContains", "startsWith", "notStartsWith", "endsWith", "notEndsWith", "regexp", "notRegexp", "=", "!=", "<", "<=", ">", ">=", "in", "notIn", "modifiedBy", "notModifiedBy", "between", "notBetween", "hasQaError", "isLengthViolated", "hasTag", "spellCheck", "qaCheck", "isMt", ] 
**caseSensitive** | bool,  | BoolClass,  |  | [optional] 
**columnId** | str,  | str,  |  | [optional] 
**dynamicColumn** | str,  | str,  |  | [optional] 
**queryPathTagViaId** | bool,  | BoolClass,  |  | [optional] 
**subField** | str,  | str,  |  | [optional] must be one of ["_dependencyStatus", "_sourceStatus", "_targetStatus", "_flowStatus", "_tm", "_mt", "_ticket", "_color", "_metadata", "_cell_metadata", "_word_count", "_previewSourceData", "_previewSourceDependencyStatus", "_previewStatus", "_previewMergeOption", "_relativeTime", "_length_violated", "_lengthSetting", "_workflow", "_workflowStepTransitioned", "_repetition", "_qaCheckStatus", "_spellCheckStatus", "_hasTag", ] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

