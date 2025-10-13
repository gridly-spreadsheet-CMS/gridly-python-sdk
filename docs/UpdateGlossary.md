# UpdateGlossary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**langs** | **List[str]** |  | [optional] 
**projects** | [**List[GlossaryProject]**](GlossaryProject.md) |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 

## Example

```python
from gridly.models.update_glossary import UpdateGlossary

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGlossary from a JSON string
update_glossary_instance = UpdateGlossary.from_json(json)
# print the JSON string representation of the object
print(UpdateGlossary.to_json())

# convert the object into a dict
update_glossary_dict = update_glossary_instance.to_dict()
# create an instance of UpdateGlossary from a dict
update_glossary_from_dict = UpdateGlossary.from_dict(update_glossary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


