# MergeRecordConflict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cells** | [**List[MergeCellConflict]**](MergeCellConflict.md) |  | [optional] 
**path_tag** | **str** |  | [optional] 
**record_id** | **str** |  | [optional] 

## Example

```python
from gridly.models.merge_record_conflict import MergeRecordConflict

# TODO update the JSON string below
json = "{}"
# create an instance of MergeRecordConflict from a JSON string
merge_record_conflict_instance = MergeRecordConflict.from_json(json)
# print the JSON string representation of the object
print(MergeRecordConflict.to_json())

# convert the object into a dict
merge_record_conflict_dict = merge_record_conflict_instance.to_dict()
# create an instance of MergeRecordConflict from a dict
merge_record_conflict_from_dict = MergeRecordConflict.from_dict(merge_record_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


