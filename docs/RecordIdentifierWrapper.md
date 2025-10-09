# RecordIdentifierWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**path** | **str** |  | 

## Example

```python
from gridly.models.record_identifier_wrapper import RecordIdentifierWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of RecordIdentifierWrapper from a JSON string
record_identifier_wrapper_instance = RecordIdentifierWrapper.from_json(json)
# print the JSON string representation of the object
print(RecordIdentifierWrapper.to_json())

# convert the object into a dict
record_identifier_wrapper_dict = record_identifier_wrapper_instance.to_dict()
# create an instance of RecordIdentifierWrapper from a dict
record_identifier_wrapper_from_dict = RecordIdentifierWrapper.from_dict(record_identifier_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


