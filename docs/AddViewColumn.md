# AddViewColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**editable** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**language_code** | **str** |  | [optional] 
**localization_type** | **str** |  | [optional] 
**number_format** | [**NumberFormat**](NumberFormat.md) |  | [optional] 
**selection_options** | **List[str]** | Please use selection | [optional] 
**selection** | [**Selection**](Selection.md) |  | [optional] 
**reference** | [**Reference**](Reference.md) |  | [optional] 
**formula** | [**Formula**](Formula.md) |  | [optional] 
**date_time_format** | [**DateTimeFormat**](DateTimeFormat.md) |  | [optional] 

## Example

```python
from gridly.models.add_view_column import AddViewColumn

# TODO update the JSON string below
json = "{}"
# create an instance of AddViewColumn from a JSON string
add_view_column_instance = AddViewColumn.from_json(json)
# print the JSON string representation of the object
print(AddViewColumn.to_json())

# convert the object into a dict
add_view_column_dict = add_view_column_instance.to_dict()
# create an instance of AddViewColumn from a dict
add_view_column_from_dict = AddViewColumn.from_dict(add_view_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


