# Branch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**columns** | [**List[ViewColumn]**](ViewColumn.md) |  | [optional] 
**default_access_view_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_master** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**record_identifier_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from gridly.models.branch import Branch

# TODO update the JSON string below
json = "{}"
# create an instance of Branch from a JSON string
branch_instance = Branch.from_json(json)
# print the JSON string representation of the object
print(Branch.to_json())

# convert the object into a dict
branch_dict = branch_instance.to_dict()
# create an instance of Branch from a dict
branch_from_dict = Branch.from_dict(branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


