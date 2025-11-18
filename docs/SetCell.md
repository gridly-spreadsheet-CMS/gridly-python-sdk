# SetCell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**column_id** | **str** |  | [optional] 
**dependency_status** | **str** |  | [optional] 
**length_limit** | **int** |  | [optional] 
**referenced_ids** | **List[str]** |  | [optional] 
**source_status** | **str** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from gridly.models.set_cell import SetCell

# TODO update the JSON string below
json = "{}"
# create an instance of SetCell from a JSON string
set_cell_instance = SetCell.from_json(json)
# print the JSON string representation of the object
print(SetCell.to_json())

# convert the object into a dict
set_cell_dict = set_cell_instance.to_dict()
# create an instance of SetCell from a dict
set_cell_from_dict = SetCell.from_dict(set_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


