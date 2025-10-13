# BulkExecutionTriggerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automation_ids** | **List[str]** |  | [optional] 
**var_await** | **bool** |  | [optional] 

## Example

```python
from gridly.models.bulk_execution_trigger_request import BulkExecutionTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkExecutionTriggerRequest from a JSON string
bulk_execution_trigger_request_instance = BulkExecutionTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(BulkExecutionTriggerRequest.to_json())

# convert the object into a dict
bulk_execution_trigger_request_dict = bulk_execution_trigger_request_instance.to_dict()
# create an instance of BulkExecutionTriggerRequest from a dict
bulk_execution_trigger_request_from_dict = BulkExecutionTriggerRequest.from_dict(bulk_execution_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


