# Formula


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formula_text** | **str** |  | 
**always_format_result_value_as_list** | **bool** |  | [optional] 
**detect_result_value_type** | **str** |  | [optional] 

## Example

```python
from gridly.models.formula import Formula

# TODO update the JSON string below
json = "{}"
# create an instance of Formula from a JSON string
formula_instance = Formula.from_json(json)
# print the JSON string representation of the object
print(Formula.to_json())

# convert the object into a dict
formula_dict = formula_instance.to_dict()
# create an instance of Formula from a dict
formula_from_dict = Formula.from_dict(formula_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


