# TranslationCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **int** |  | [optional] 
**out_of_date** | **int** |  | [optional] 
**unset** | **int** |  | [optional] 
**up_to_date** | **int** |  | [optional] 

## Example

```python
from gridly.models.translation_count import TranslationCount

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationCount from a JSON string
translation_count_instance = TranslationCount.from_json(json)
# print the JSON string representation of the object
print(TranslationCount.to_json())

# convert the object into a dict
translation_count_dict = translation_count_instance.to_dict()
# create an instance of TranslationCount from a dict
translation_count_from_dict = TranslationCount.from_dict(translation_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


