# CreateDatabase

body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**enable_guid_record** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from gridly.models.create_database import CreateDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDatabase from a JSON string
create_database_instance = CreateDatabase.from_json(json)
# print the JSON string representation of the object
print(CreateDatabase.to_json())

# convert the object into a dict
create_database_dict = create_database_instance.to_dict()
# create an instance of CreateDatabase from a dict
create_database_from_dict = CreateDatabase.from_dict(create_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


