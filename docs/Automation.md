# Automation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**completed** | **bool** |  | [optional] 
**triggers** | [**List[AutomationTrigger]**](AutomationTrigger.md) |  | [optional] 
**actions** | [**List[AutomationNode]**](AutomationNode.md) |  | [optional] 

## Example

```python
from gridly.models.automation import Automation

# TODO update the JSON string below
json = "{}"
# create an instance of Automation from a JSON string
automation_instance = Automation.from_json(json)
# print the JSON string representation of the object
print(Automation.to_json())

# convert the object into a dict
automation_dict = automation_instance.to_dict()
# create an instance of Automation from a dict
automation_from_dict = Automation.from_dict(automation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


