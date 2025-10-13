# ExportRecordHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_ids** | **List[str]** |  | [optional] 
**from_time** | **datetime** |  | 
**to_time** | **datetime** |  | 
**format** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**last_modified_by_users** | **List[str]** |  | [optional] 

## Example

```python
from gridly.models.export_record_history import ExportRecordHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ExportRecordHistory from a JSON string
export_record_history_instance = ExportRecordHistory.from_json(json)
# print the JSON string representation of the object
print(ExportRecordHistory.to_json())

# convert the object into a dict
export_record_history_dict = export_record_history_instance.to_dict()
# create an instance of ExportRecordHistory from a dict
export_record_history_from_dict = ExportRecordHistory.from_dict(export_record_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


