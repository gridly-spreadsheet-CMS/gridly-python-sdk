# gridly.model.group.Group

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**groupId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**companyId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**name** | str,  | str,  |  | [optional] 
**logoUrl** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["NORMAL", "ADMIN", ] 
**shareType** | str,  | str,  |  | [optional] must be one of ["none", "full", "project", "database", "grid", "view", ] 
**createdDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**lastModifiedDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**systemGroup** | bool,  | BoolClass,  |  | [optional] 
**isSystemGroup** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

