# BranchDiffCell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_dependency_status** | **str** |  | [optional] 
**destination_dependency_status** | **str** |  | [optional] 
**source_source_status** | **str** |  | [optional] 
**destination_source_status** | **str** |  | [optional] 
**source_length_setting** | **int** |  | [optional] 
**destination_length_setting** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**column_id** | **str** |  | [optional] 
**source_value** | **object** |  | [optional] 
**destination_value** | **object** |  | [optional] 

## Example

```python
from gridly.models.branch_diff_cell import BranchDiffCell

# TODO update the JSON string below
json = "{}"
# create an instance of BranchDiffCell from a JSON string
branch_diff_cell_instance = BranchDiffCell.from_json(json)
# print the JSON string representation of the object
print(BranchDiffCell.to_json())

# convert the object into a dict
branch_diff_cell_dict = branch_diff_cell_instance.to_dict()
# create an instance of BranchDiffCell from a dict
branch_diff_cell_from_dict = BranchDiffCell.from_dict(branch_diff_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


