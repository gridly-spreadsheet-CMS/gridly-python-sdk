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
**subField** | str,  | str,  |  | [optional] must be one of ["DEPENDENCY_STATUS", "SOURCE_STATUS", "TARGET_STATUS", "FLOW_STATUS", "TM", "MT", "TICKET", "COLOR", "METADATA", "CELL_METADATA", "WORD_COUNT", "PREVIEW_SOURCE_DATA", "PREVIEW_SOURCE_DEPENDENCY_STATUS", "PREVIEW_STATUS", "PREVIEW_MERGE_OPTION", "RELATIVE_TIME", "LENGTH_VIOLATED", "LENGTH_SETTING", "WORKFLOW_STATUS", "REPETITION", "QA_CHECK_STATUS", ] 
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

