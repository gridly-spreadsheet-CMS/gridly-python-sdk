# MovePath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** |  | [optional] 
**from_parent_path** | **str** |  | [optional] 
**to_parent_path** | **str** |  | [optional] 
**move_before** | **str** |  | [optional] 
**move_after** | **str** |  | [optional] 

## Example

```python
from gridly.models.move_path import MovePath

# TODO update the JSON string below
json = "{}"
# create an instance of MovePath from a JSON string
move_path_instance = MovePath.from_json(json)
# print the JSON string representation of the object
print(MovePath.to_json())

# convert the object into a dict
move_path_dict = move_path_instance.to_dict()
# create an instance of MovePath from a dict
move_path_from_dict = MovePath.from_dict(move_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


