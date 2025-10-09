# CreateDependency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**target_column_id** | **str** |  | 
**source_column_id** | **str** |  | 

## Example

```python
from gridly.models.create_dependency import CreateDependency

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDependency from a JSON string
create_dependency_instance = CreateDependency.from_json(json)
# print the JSON string representation of the object
print(CreateDependency.to_json())

# convert the object into a dict
create_dependency_dict = create_dependency_instance.to_dict()
# create an instance of CreateDependency from a dict
create_dependency_from_dict = CreateDependency.from_dict(create_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


