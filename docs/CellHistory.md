# CellHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_status** | **str** |  | [optional] 
**source_status** | **str** |  | [optional] 
**column_id** | **str** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from gridly.models.cell_history import CellHistory

# TODO update the JSON string below
json = "{}"
# create an instance of CellHistory from a JSON string
cell_history_instance = CellHistory.from_json(json)
# print the JSON string representation of the object
print(CellHistory.to_json())

# convert the object into a dict
cell_history_dict = cell_history_instance.to_dict()
# create an instance of CellHistory from a dict
cell_history_from_dict = CellHistory.from_dict(cell_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


