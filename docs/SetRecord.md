# SetRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**cells** | [**List[SetCell]**](SetCell.md) |  | [optional] 
**mark_updated_cells_with_mt_flag** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from gridly.models.set_record import SetRecord

# TODO update the JSON string below
json = "{}"
# create an instance of SetRecord from a JSON string
set_record_instance = SetRecord.from_json(json)
# print the JSON string representation of the object
print(SetRecord.to_json())

# convert the object into a dict
set_record_dict = set_record_instance.to_dict()
# create an instance of SetRecord from a dict
set_record_from_dict = SetRecord.from_dict(set_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


