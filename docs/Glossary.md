# Glossary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**langs** | **List[str]** |  | [optional] 
**projects** | [**List[GlossaryProject]**](GlossaryProject.md) |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 

## Example

```python
from gridly.models.glossary import Glossary

# TODO update the JSON string below
json = "{}"
# create an instance of Glossary from a JSON string
glossary_instance = Glossary.from_json(json)
# print the JSON string representation of the object
print(Glossary.to_json())

# convert the object into a dict
glossary_dict = glossary_instance.to_dict()
# create an instance of Glossary from a dict
glossary_from_dict = Glossary.from_dict(glossary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


