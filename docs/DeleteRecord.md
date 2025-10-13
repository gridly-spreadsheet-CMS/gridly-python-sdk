# DeleteRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 
**identifiers** | [**List[RecordIdentifierWrapper]**](RecordIdentifierWrapper.md) |  | [optional] 

## Example

```python
from gridly.models.delete_record import DeleteRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRecord from a JSON string
delete_record_instance = DeleteRecord.from_json(json)
# print the JSON string representation of the object
print(DeleteRecord.to_json())

# convert the object into a dict
delete_record_dict = delete_record_instance.to_dict()
# create an instance of DeleteRecord from a dict
delete_record_from_dict = DeleteRecord.from_dict(delete_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


