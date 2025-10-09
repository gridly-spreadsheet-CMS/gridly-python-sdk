# ExecutionTriggerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_await** | **bool** |  | [optional] 

## Example

```python
from gridly.models.execution_trigger_request import ExecutionTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionTriggerRequest from a JSON string
execution_trigger_request_instance = ExecutionTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(ExecutionTriggerRequest.to_json())

# convert the object into a dict
execution_trigger_request_dict = execution_trigger_request_instance.to_dict()
# create an instance of ExecutionTriggerRequest from a dict
execution_trigger_request_from_dict = ExecutionTriggerRequest.from_dict(execution_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


