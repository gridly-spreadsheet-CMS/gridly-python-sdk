# DateTimeFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**time_format** | **str** |  | [optional] 
**zone_offset** | **str** |  | [optional] 
**show_time_zone** | **bool** |  | [optional] 

## Example

```python
from gridly.models.date_time_format import DateTimeFormat

# TODO update the JSON string below
json = "{}"
# create an instance of DateTimeFormat from a JSON string
date_time_format_instance = DateTimeFormat.from_json(json)
# print the JSON string representation of the object
print(DateTimeFormat.to_json())

# convert the object into a dict
date_time_format_dict = date_time_format_instance.to_dict()
# create an instance of DateTimeFormat from a dict
date_time_format_from_dict = DateTimeFormat.from_dict(date_time_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


