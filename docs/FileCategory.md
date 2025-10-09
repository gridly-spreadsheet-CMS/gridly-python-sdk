# FileCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from gridly.models.file_category import FileCategory

# TODO update the JSON string below
json = "{}"
# create an instance of FileCategory from a JSON string
file_category_instance = FileCategory.from_json(json)
# print the JSON string representation of the object
print(FileCategory.to_json())

# convert the object into a dict
file_category_dict = file_category_instance.to_dict()
# create an instance of FileCategory from a dict
file_category_from_dict = FileCategory.from_dict(file_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


