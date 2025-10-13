# AutomationNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**completed** | **bool** |  | [optional] 

## Example

```python
from gridly.models.automation_node import AutomationNode

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationNode from a JSON string
automation_node_instance = AutomationNode.from_json(json)
# print the JSON string representation of the object
print(AutomationNode.to_json())

# convert the object into a dict
automation_node_dict = automation_node_instance.to_dict()
# create an instance of AutomationNode from a dict
automation_node_from_dict = AutomationNode.from_dict(automation_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


