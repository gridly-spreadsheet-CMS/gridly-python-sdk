# Record


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**cells** | [**List[Cell]**](Cell.md) |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**last_modified_time** | **datetime** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from gridly.models.record import Record

# TODO update the JSON string below
json = "{}"
# create an instance of Record from a JSON string
record_instance = Record.from_json(json)
# print the JSON string representation of the object
print(Record.to_json())

# convert the object into a dict
record_dict = record_instance.to_dict()
# create an instance of Record from a dict
record_from_dict = Record.from_dict(record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


