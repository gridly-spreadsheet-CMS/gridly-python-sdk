# RecordHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**cells** | [**List[CellHistory]**](CellHistory.md) |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**last_modified_time** | **datetime** |  | [optional] 

## Example

```python
from gridly.models.record_history import RecordHistory

# TODO update the JSON string below
json = "{}"
# create an instance of RecordHistory from a JSON string
record_history_instance = RecordHistory.from_json(json)
# print the JSON string representation of the object
print(RecordHistory.to_json())

# convert the object into a dict
record_history_dict = record_history_instance.to_dict()
# create an instance of RecordHistory from a dict
record_history_from_dict = RecordHistory.from_dict(record_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


