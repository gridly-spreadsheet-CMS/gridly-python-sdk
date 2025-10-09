# PathNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**parent_path** | **str** |  | [optional] 

## Example

```python
from gridly.models.path_node import PathNode

# TODO update the JSON string below
json = "{}"
# create an instance of PathNode from a JSON string
path_node_instance = PathNode.from_json(json)
# print the JSON string representation of the object
print(PathNode.to_json())

# convert the object into a dict
path_node_dict = path_node_instance.to_dict()
# create an instance of PathNode from a dict
path_node_from_dict = PathNode.from_dict(path_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


