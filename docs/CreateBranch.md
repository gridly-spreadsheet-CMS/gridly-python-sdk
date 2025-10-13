# CreateBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**custom_properties** | **Dict[str, object]** |  | [optional] 
**inherit_group_access** | **bool** |  | [optional] 
**inherit_automation** | **bool** |  | [optional] 
**view_id** | **str** |  | [optional] 

## Example

```python
from gridly.models.create_branch import CreateBranch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBranch from a JSON string
create_branch_instance = CreateBranch.from_json(json)
# print the JSON string representation of the object
print(CreateBranch.to_json())

# convert the object into a dict
create_branch_dict = create_branch_instance.to_dict()
# create an instance of CreateBranch from a dict
create_branch_from_dict = CreateBranch.from_dict(create_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


