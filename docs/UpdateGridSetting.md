# UpdateGridSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_date_time_format** | [**DateTimeFormat**](DateTimeFormat.md) |  | [optional] 
**default_source_language_status** | **str** |  | [optional] 
**translator_can_view_automations** | **bool** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from gridly.models.update_grid_setting import UpdateGridSetting

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGridSetting from a JSON string
update_grid_setting_instance = UpdateGridSetting.from_json(json)
# print the JSON string representation of the object
print(UpdateGridSetting.to_json())

# convert the object into a dict
update_grid_setting_dict = update_grid_setting_instance.to_dict()
# create an instance of UpdateGridSetting from a dict
update_grid_setting_from_dict = UpdateGridSetting.from_dict(update_grid_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


