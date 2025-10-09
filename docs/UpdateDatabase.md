# UpdateDatabase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from gridly.models.update_database import UpdateDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDatabase from a JSON string
update_database_instance = UpdateDatabase.from_json(json)
# print the JSON string representation of the object
print(UpdateDatabase.to_json())

# convert the object into a dict
update_database_dict = update_database_instance.to_dict()
# create an instance of UpdateDatabase from a dict
update_database_from_dict = UpdateDatabase.from_dict(update_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


