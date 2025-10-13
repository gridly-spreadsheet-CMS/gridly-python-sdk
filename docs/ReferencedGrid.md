# ReferencedGrid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from gridly.models.referenced_grid import ReferencedGrid

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedGrid from a JSON string
referenced_grid_instance = ReferencedGrid.from_json(json)
# print the JSON string representation of the object
print(ReferencedGrid.to_json())

# convert the object into a dict
referenced_grid_dict = referenced_grid_instance.to_dict()
# create an instance of ReferencedGrid from a dict
referenced_grid_from_dict = ReferencedGrid.from_dict(referenced_grid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


