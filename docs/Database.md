# Database


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**grids** | [**List[Grid]**](Grid.md) |  | [optional] 
**views** | [**List[View]**](View.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**groups** | [**List[Group]**](Group.md) |  | [optional] 

## Example

```python
from gridly.models.database import Database

# TODO update the JSON string below
json = "{}"
# create an instance of Database from a JSON string
database_instance = Database.from_json(json)
# print the JSON string representation of the object
print(Database.to_json())

# convert the object into a dict
database_dict = database_instance.to_dict()
# create an instance of Database from a dict
database_from_dict = Database.from_dict(database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


