# BranchDiffRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**cells** | [**List[BranchDiffCell]**](BranchDiffCell.md) |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**last_modified_time** | **datetime** |  | [optional] 

## Example

```python
from gridly.models.branch_diff_record import BranchDiffRecord

# TODO update the JSON string below
json = "{}"
# create an instance of BranchDiffRecord from a JSON string
branch_diff_record_instance = BranchDiffRecord.from_json(json)
# print the JSON string representation of the object
print(BranchDiffRecord.to_json())

# convert the object into a dict
branch_diff_record_dict = branch_diff_record_instance.to_dict()
# create an instance of BranchDiffRecord from a dict
branch_diff_record_from_dict = BranchDiffRecord.from_dict(branch_diff_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


