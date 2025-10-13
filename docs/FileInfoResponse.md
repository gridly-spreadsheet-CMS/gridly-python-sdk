# FileInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**thumbnail_id** | **str** |  | [optional] 

## Example

```python
from gridly.models.file_info_response import FileInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileInfoResponse from a JSON string
file_info_response_instance = FileInfoResponse.from_json(json)
# print the JSON string representation of the object
print(FileInfoResponse.to_json())

# convert the object into a dict
file_info_response_dict = file_info_response_instance.to_dict()
# create an instance of FileInfoResponse from a dict
file_info_response_from_dict = FileInfoResponse.from_dict(file_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


