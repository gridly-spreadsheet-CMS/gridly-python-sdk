# gridly.model.cdn.CDN

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**gridId** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["readyToPublish", "processing", "published", ] 
**lastGeneratedTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**lastPublishedTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**permission** | str,  | str,  |  | [optional] must be one of ["public", "private", ] 
**type** | str,  | str,  |  | [optional] 
**createdTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**lastModifiedTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**createdBy** | str,  | str,  |  | [optional] 
**lastModifiedBy** | str,  | str,  |  | [optional] 
**startTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**endTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**whiteListIP** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

