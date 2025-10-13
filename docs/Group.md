# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**group_id** | **int** |  | [optional] 
**company_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**share_type** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**system_group** | **bool** |  | [optional] 
**is_system_group** | **bool** |  | [optional] 

## Example

```python
from gridly.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


