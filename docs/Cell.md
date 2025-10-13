# Cell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_id** | **str** |  | [optional] 
**dependency_status** | **str** |  | [optional] 
**length_limit** | **int** |  | [optional] 
**line_limit** | **int** |  | [optional] 
**mt** | **bool** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**referenced_ids** | **List[str]** |  | [optional] 
**source_status** | **str** |  | [optional] 
**tm** | **bool** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from gridly.models.cell import Cell

# TODO update the JSON string below
json = "{}"
# create an instance of Cell from a JSON string
cell_instance = Cell.from_json(json)
# print the JSON string representation of the object
print(Cell.to_json())

# convert the object into a dict
cell_dict = cell_instance.to_dict()
# create an instance of Cell from a dict
cell_from_dict = Cell.from_dict(cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


