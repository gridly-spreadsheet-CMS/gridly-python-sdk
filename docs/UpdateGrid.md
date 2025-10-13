# UpdateGrid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from gridly.models.update_grid import UpdateGrid

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGrid from a JSON string
update_grid_instance = UpdateGrid.from_json(json)
# print the JSON string representation of the object
print(UpdateGrid.to_json())

# convert the object into a dict
update_grid_dict = update_grid_instance.to_dict()
# create an instance of UpdateGrid from a dict
update_grid_from_dict = UpdateGrid.from_dict(update_grid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


