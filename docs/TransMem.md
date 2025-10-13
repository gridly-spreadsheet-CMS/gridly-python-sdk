# TransMem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**is_paused_consuming** | **bool** |  | [optional] 
**populate_translation_status** | [**TranslationStatus**](TranslationStatus.md) |  | [optional] 
**context_lookup** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fuzzy_match** | **bool** |  | [optional] 
**allow_alternative** | **bool** |  | [optional] 
**allow_alternative_has_same_record_id** | **bool** |  | [optional] 

## Example

```python
from gridly.models.trans_mem import TransMem

# TODO update the JSON string below
json = "{}"
# create an instance of TransMem from a JSON string
trans_mem_instance = TransMem.from_json(json)
# print the JSON string representation of the object
print(TransMem.to_json())

# convert the object into a dict
trans_mem_dict = trans_mem_instance.to_dict()
# create an instance of TransMem from a dict
trans_mem_from_dict = TransMem.from_dict(trans_mem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


