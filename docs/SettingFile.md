# SettingFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**FileCategory**](FileCategory.md) |  | [optional] 
**files** | [**List[UploadedFile]**](UploadedFile.md) |  | [optional] 

## Example

```python
from gridly.models.setting_file import SettingFile

# TODO update the JSON string below
json = "{}"
# create an instance of SettingFile from a JSON string
setting_file_instance = SettingFile.from_json(json)
# print the JSON string representation of the object
print(SettingFile.to_json())

# convert the object into a dict
setting_file_dict = setting_file_instance.to_dict()
# create an instance of SettingFile from a dict
setting_file_from_dict = SettingFile.from_dict(setting_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


