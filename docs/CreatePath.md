# CreatePath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_path** | **str** |  | [optional] 
**paths** | **List[str]** |  | [optional] 

## Example

```python
from gridly.models.create_path import CreatePath

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePath from a JSON string
create_path_instance = CreatePath.from_json(json)
# print the JSON string representation of the object
print(CreatePath.to_json())

# convert the object into a dict
create_path_dict = create_path_instance.to_dict()
# create an instance of CreatePath from a dict
create_path_from_dict = CreatePath.from_dict(create_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


