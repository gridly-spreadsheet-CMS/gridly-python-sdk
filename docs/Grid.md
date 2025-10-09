# Grid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**columns** | [**List[ViewColumn]**](ViewColumn.md) |  | [optional] 
**default_access_view_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**record_identifier_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from gridly.models.grid import Grid

# TODO update the JSON string below
json = "{}"
# create an instance of Grid from a JSON string
grid_instance = Grid.from_json(json)
# print the JSON string representation of the object
print(Grid.to_json())

# convert the object into a dict
grid_dict = grid_instance.to_dict()
# create an instance of Grid from a dict
grid_from_dict = Grid.from_dict(grid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


