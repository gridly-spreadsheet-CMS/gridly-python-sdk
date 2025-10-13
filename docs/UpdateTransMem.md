# UpdateTransMem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 
**fuzzy_match** | **bool** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**is_paused_consuming** | **bool** |  | [optional] 
**populate_translation_status** | [**TranslationStatus**](TranslationStatus.md) |  | [optional] 
**context_lookup** | **bool** |  | [optional] 
**allow_alternative** | **bool** |  | [optional] 
**allow_alternative_has_same_record_id** | **bool** |  | [optional] 

## Example

```python
from gridly.models.update_trans_mem import UpdateTransMem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransMem from a JSON string
update_trans_mem_instance = UpdateTransMem.from_json(json)
# print the JSON string representation of the object
print(UpdateTransMem.to_json())

# convert the object into a dict
update_trans_mem_dict = update_trans_mem_instance.to_dict()
# create an instance of UpdateTransMem from a dict
update_trans_mem_from_dict = UpdateTransMem.from_dict(update_trans_mem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


