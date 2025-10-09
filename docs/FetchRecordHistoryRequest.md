# FetchRecordHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_ids** | **List[str]** |  | [optional] 
**query** | **str** |  | [optional] 
**sort** | **str** |  | [optional] 
**group_by** | **List[str]** |  | [optional] 
**page** | **str** |  | [optional] 
**fetch_options** | **str** |  | [optional] 
**include_system_user** | **bool** |  | [optional] 

## Example

```python
from gridly.models.fetch_record_history_request import FetchRecordHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchRecordHistoryRequest from a JSON string
fetch_record_history_request_instance = FetchRecordHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(FetchRecordHistoryRequest.to_json())

# convert the object into a dict
fetch_record_history_request_dict = fetch_record_history_request_instance.to_dict()
# create an instance of FetchRecordHistoryRequest from a dict
fetch_record_history_request_from_dict = FetchRecordHistoryRequest.from_dict(fetch_record_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


