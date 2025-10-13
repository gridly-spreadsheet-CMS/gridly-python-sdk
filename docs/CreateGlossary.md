# CreateGlossary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**langs** | **List[str]** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 

## Example

```python
from gridly.models.create_glossary import CreateGlossary

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGlossary from a JSON string
create_glossary_instance = CreateGlossary.from_json(json)
# print the JSON string representation of the object
print(CreateGlossary.to_json())

# convert the object into a dict
create_glossary_dict = create_glossary_instance.to_dict()
# create an instance of CreateGlossary from a dict
create_glossary_from_dict = CreateGlossary.from_dict(create_glossary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


