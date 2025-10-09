# CreateColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | 
**editable** | **bool** |  | [optional] 
**language_code** | **str** |  | [optional] 
**localization_type** | **str** |  | [optional] 
**number_format** | [**NumberFormat**](NumberFormat.md) |  | [optional] 
**selection_options** | **List[str]** | Please use selection | [optional] 
**selection** | [**Selection**](Selection.md) |  | [optional] 
**reference** | [**Reference**](Reference.md) |  | [optional] 
**formula** | [**Formula**](Formula.md) |  | [optional] 
**date_time_format** | [**DateTimeFormat**](DateTimeFormat.md) |  | [optional] 
**length_limit_setting** | [**LengthLimitSetting**](LengthLimitSetting.md) |  | [optional] 

## Example

```python
from gridly.models.create_column import CreateColumn

# TODO update the JSON string below
json = "{}"
# create an instance of CreateColumn from a JSON string
create_column_instance = CreateColumn.from_json(json)
# print the JSON string representation of the object
print(CreateColumn.to_json())

# convert the object into a dict
create_column_dict = create_column_instance.to_dict()
# create an instance of CreateColumn from a dict
create_column_from_dict = CreateColumn.from_dict(create_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


