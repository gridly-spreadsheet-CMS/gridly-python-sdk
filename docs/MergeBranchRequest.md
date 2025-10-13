# MergeBranchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_record_options** | **List[str]** |  | [optional] 
**merge_record_conflicts** | [**List[MergeRecordConflict]**](MergeRecordConflict.md) |  | [optional] 
**use_last_merge_resolve** | **bool** |  | [optional] 
**check_mismatched_column_type** | **bool** |  | [optional] 
**query** | [**List[FilterField]**](FilterField.md) |  | [optional] 

## Example

```python
from gridly.models.merge_branch_request import MergeBranchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergeBranchRequest from a JSON string
merge_branch_request_instance = MergeBranchRequest.from_json(json)
# print the JSON string representation of the object
print(MergeBranchRequest.to_json())

# convert the object into a dict
merge_branch_request_dict = merge_branch_request_instance.to_dict()
# create an instance of MergeBranchRequest from a dict
merge_branch_request_from_dict = MergeBranchRequest.from_dict(merge_branch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


