# GridSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_source_language_status** | **str** |  | [optional] 
**translator_can_view_automations** | **bool** |  | [optional] 
**categories** | [**List[FileCategory]**](FileCategory.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**last_modified_time** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 

## Example

```python
from gridly.models.grid_setting import GridSetting

# TODO update the JSON string below
json = "{}"
# create an instance of GridSetting from a JSON string
grid_setting_instance = GridSetting.from_json(json)
# print the JSON string representation of the object
print(GridSetting.to_json())

# convert the object into a dict
grid_setting_dict = grid_setting_instance.to_dict()
# create an instance of GridSetting from a dict
grid_setting_from_dict = GridSetting.from_dict(grid_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


