# ViewColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**date_time_format** | [**DateTimeFormat**](DateTimeFormat.md) |  | [optional] 
**depends_on** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**editable** | **bool** |  | [optional] 
**formula** | [**Formula**](Formula.md) |  | [optional] 
**is_source** | **bool** |  | [optional] 
**is_target** | **bool** |  | [optional] 
**language_code** | **str** |  | [optional] 
**language_name** | **str** |  | [optional] 
**length_limit_setting** | [**LengthLimitSetting**](LengthLimitSetting.md) |  | [optional] 
**localization_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**number_format** | [**NumberFormat**](NumberFormat.md) |  | [optional] 
**reference** | [**ColumnReference**](ColumnReference.md) |  | [optional] 
**selection** | [**Selection**](Selection.md) |  | [optional] 
**selection_options** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from gridly.models.view_column import ViewColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ViewColumn from a JSON string
view_column_instance = ViewColumn.from_json(json)
# print the JSON string representation of the object
print(ViewColumn.to_json())

# convert the object into a dict
view_column_dict = view_column_instance.to_dict()
# create an instance of ViewColumn from a dict
view_column_from_dict = ViewColumn.from_dict(view_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


