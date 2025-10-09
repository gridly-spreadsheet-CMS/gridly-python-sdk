# FilterField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accent_sensitive** | **bool** |  | [optional] 
**case_sensitive** | **bool** |  | [optional] 
**column_id** | **str** |  | [optional] 
**dynamic_column** | **str** |  | [optional] [readonly] 
**operator** | **str** |  | 
**query_path_tag_via_id** | **bool** |  | [optional] 
**sub_field** | **str** |  | [optional] 
**values** | **List[object]** |  | [optional] 

## Example

```python
from gridly.models.filter_field import FilterField

# TODO update the JSON string below
json = "{}"
# create an instance of FilterField from a JSON string
filter_field_instance = FilterField.from_json(json)
# print the JSON string representation of the object
print(FilterField.to_json())

# convert the object into a dict
filter_field_dict = filter_field_instance.to_dict()
# create an instance of FilterField from a dict
filter_field_from_dict = FilterField.from_dict(filter_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


