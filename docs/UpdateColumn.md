# UpdateColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**language_code** | **str** |  | [optional] 
**localization_type** | **str** |  | [optional] 
**selection_options** | **List[str]** | Please use selection | [optional] 
**selection** | [**Selection**](Selection.md) |  | [optional] 
**number_format** | [**NumberFormat**](NumberFormat.md) |  | [optional] 
**reference** | [**Reference**](Reference.md) |  | [optional] 
**formula** | [**Formula**](Formula.md) |  | [optional] 
**date_time_format** | [**DateTimeFormat**](DateTimeFormat.md) |  | [optional] 
**viewable** | **bool** |  | [optional] 
**editable** | **bool** |  | [optional] 
**length_limit_setting** | [**LengthLimitSetting**](LengthLimitSetting.md) |  | [optional] 
**new_id** | **str** |  | [optional] 

## Example

```python
from gridly.models.update_column import UpdateColumn

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateColumn from a JSON string
update_column_instance = UpdateColumn.from_json(json)
# print the JSON string representation of the object
print(UpdateColumn.to_json())

# convert the object into a dict
update_column_dict = update_column_instance.to_dict()
# create an instance of UpdateColumn from a dict
update_column_from_dict = UpdateColumn.from_dict(update_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


