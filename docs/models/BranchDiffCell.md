# gridly.model.branch_diff_cell.BranchDiffCell

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceDependencyStatus** | str,  | str,  |  | [optional] must be one of ["upToDate", "outOfDate", "unset", ] 
**destinationDependencyStatus** | str,  | str,  |  | [optional] must be one of ["upToDate", "outOfDate", "unset", ] 
**sourceSourceStatus** | str,  | str,  |  | [optional] must be one of ["unset", "doNotTranslate", "notReadyForTranslation", "readyForTranslation", "locked", "lockAllLanguages", ] 
**destinationSourceStatus** | str,  | str,  |  | [optional] must be one of ["unset", "doNotTranslate", "notReadyForTranslation", "readyForTranslation", "locked", "lockAllLanguages", ] 
**sourceLengthSetting** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**destinationLengthSetting** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**status** | str,  | str,  |  | [optional] must be one of ["behind", "ahead", "conflicted", "unchanged", "invalidData", "na", "empty", "targetTranslationEmpty", "translationNotReady", "translationNotFound", "sourceTargetMismatched", "targetChangedTMNotApproved", "targetNotChanged", "sourcedChanged", "targetChanged", "textOverLength", "translationNotChanged", "notChanged", "warningOff", ] 
**columnId** | str,  | str,  |  | [optional] 
**[sourceValue](#sourceValue)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[destinationValue](#destinationValue)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sourceValue

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# destinationValue

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

