# CreateTransMem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 
**fuzzy_match** | **bool** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**is_paused_consuming** | **bool** |  | [optional] 
**context_lookup** | **bool** |  | [optional] 
**populate_translation_status** | [**TranslationStatus**](TranslationStatus.md) |  | [optional] 
**allow_alternative** | **bool** |  | [optional] 

## Example

```python
from gridly.models.create_trans_mem import CreateTransMem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransMem from a JSON string
create_trans_mem_instance = CreateTransMem.from_json(json)
# print the JSON string representation of the object
print(CreateTransMem.to_json())

# convert the object into a dict
create_trans_mem_dict = create_trans_mem_instance.to_dict()
# create an instance of CreateTransMem from a dict
create_trans_mem_from_dict = CreateTransMem.from_dict(create_trans_mem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


