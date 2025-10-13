# CreateProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from gridly.models.create_project import CreateProject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProject from a JSON string
create_project_instance = CreateProject.from_json(json)
# print the JSON string representation of the object
print(CreateProject.to_json())

# convert the object into a dict
create_project_dict = create_project_instance.to_dict()
# create an instance of CreateProject from a dict
create_project_from_dict = CreateProject.from_dict(create_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


