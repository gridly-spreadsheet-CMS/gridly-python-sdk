# NumberFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**decimal_places** | **int** |  | [optional] 
**currency_symbol** | **str** |  | [optional] 
**use1000_separator** | **bool** |  | [optional] 

## Example

```python
from gridly.models.number_format import NumberFormat

# TODO update the JSON string below
json = "{}"
# create an instance of NumberFormat from a JSON string
number_format_instance = NumberFormat.from_json(json)
# print the JSON string representation of the object
print(NumberFormat.to_json())

# convert the object into a dict
number_format_dict = number_format_instance.to_dict()
# create an instance of NumberFormat from a dict
number_format_from_dict = NumberFormat.from_dict(number_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


