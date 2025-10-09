# SelectionOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**value** | **str** |  | 

## Example

```python
from gridly.models.selection_option import SelectionOption

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionOption from a JSON string
selection_option_instance = SelectionOption.from_json(json)
# print the JSON string representation of the object
print(SelectionOption.to_json())

# convert the object into a dict
selection_option_dict = selection_option_instance.to_dict()
# create an instance of SelectionOption from a dict
selection_option_from_dict = SelectionOption.from_dict(selection_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


