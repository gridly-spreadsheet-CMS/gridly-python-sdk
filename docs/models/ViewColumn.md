# gridly.model.view_column.ViewColumn

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**dateTimeFormat** | [**DateTimeFormat**](DateTimeFormat.md) | [**DateTimeFormat**](DateTimeFormat.md) |  | [optional] 
**dependsOn** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**editable** | bool,  | BoolClass,  |  | [optional] 
**formula** | [**Formula**](Formula.md) | [**Formula**](Formula.md) |  | [optional] 
**isSource** | bool,  | BoolClass,  |  | [optional] 
**isTarget** | bool,  | BoolClass,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**localizationType** | str,  | str,  |  | [optional] must be one of ["sourceLanguage", "targetLanguage", ] 
**name** | str,  | str,  |  | [optional] 
**numberFormat** | [**NumberFormat**](NumberFormat.md) | [**NumberFormat**](NumberFormat.md) |  | [optional] 
**reference** | [**ColumnReference**](ColumnReference.md) | [**ColumnReference**](ColumnReference.md) |  | [optional] 
**[selectionOptions](#selectionOptions)** | list, tuple,  | tuple,  |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["singleLine", "multipleLines", "richText", "markdown", "singleSelection", "multipleSelections", "boolean", "number", "datetime", "files", "reference", "lookup", "language", "json", "yaml", "html", "formula", "user", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# selectionOptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

