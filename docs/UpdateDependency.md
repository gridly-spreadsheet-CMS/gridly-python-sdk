# UpdateDependency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_id** | **str** |  | [optional] 
**target_column_id** | **str** |  | 
**source_column_id** | **str** |  | 

## Example

```python
from gridly.models.update_dependency import UpdateDependency

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDependency from a JSON string
update_dependency_instance = UpdateDependency.from_json(json)
# print the JSON string representation of the object
print(UpdateDependency.to_json())

# convert the object into a dict
update_dependency_dict = update_dependency_instance.to_dict()
# create an instance of UpdateDependency from a dict
update_dependency_from_dict = UpdateDependency.from_dict(update_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


