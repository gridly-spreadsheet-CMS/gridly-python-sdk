# LengthLimitSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | [optional] 
**unit** | **str** |  | 
**use_source_text_length** | **bool** |  | [optional] 

## Example

```python
from gridly.models.length_limit_setting import LengthLimitSetting

# TODO update the JSON string below
json = "{}"
# create an instance of LengthLimitSetting from a JSON string
length_limit_setting_instance = LengthLimitSetting.from_json(json)
# print the JSON string representation of the object
print(LengthLimitSetting.to_json())

# convert the object into a dict
length_limit_setting_dict = length_limit_setting_instance.to_dict()
# create an instance of LengthLimitSetting from a dict
length_limit_setting_from_dict = LengthLimitSetting.from_dict(length_limit_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


