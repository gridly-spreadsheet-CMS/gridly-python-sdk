# SubCategorySeverityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**score** | **float** |  | [optional] 

## Example

```python
from gridly.models.sub_category_severity_response import SubCategorySeverityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubCategorySeverityResponse from a JSON string
sub_category_severity_response_instance = SubCategorySeverityResponse.from_json(json)
# print the JSON string representation of the object
print(SubCategorySeverityResponse.to_json())

# convert the object into a dict
sub_category_severity_response_dict = sub_category_severity_response_instance.to_dict()
# create an instance of SubCategorySeverityResponse from a dict
sub_category_severity_response_from_dict = SubCategorySeverityResponse.from_dict(sub_category_severity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


