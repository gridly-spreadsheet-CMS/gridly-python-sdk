# AutomationTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**trigger_type** | **str** |  | [optional] 
**watching_columns** | **List[str]** |  | [optional] 
**watching_all** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from gridly.models.automation_trigger import AutomationTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationTrigger from a JSON string
automation_trigger_instance = AutomationTrigger.from_json(json)
# print the JSON string representation of the object
print(AutomationTrigger.to_json())

# convert the object into a dict
automation_trigger_dict = automation_trigger_instance.to_dict()
# create an instance of AutomationTrigger from a dict
automation_trigger_from_dict = AutomationTrigger.from_dict(automation_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


