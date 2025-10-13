# UploadSettingFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** |  | [optional] 

## Example

```python
from gridly.models.upload_setting_file_request import UploadSettingFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSettingFileRequest from a JSON string
upload_setting_file_request_instance = UploadSettingFileRequest.from_json(json)
# print the JSON string representation of the object
print(UploadSettingFileRequest.to_json())

# convert the object into a dict
upload_setting_file_request_dict = upload_setting_file_request_instance.to_dict()
# create an instance of UploadSettingFileRequest from a dict
upload_setting_file_request_from_dict = UploadSettingFileRequest.from_dict(upload_setting_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


