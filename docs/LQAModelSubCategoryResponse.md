# LQAModelSubCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**severities** | [**List[SubCategorySeverityResponse]**](SubCategorySeverityResponse.md) |  | [optional] 

## Example

```python
from gridly.models.lqa_model_sub_category_response import LQAModelSubCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LQAModelSubCategoryResponse from a JSON string
lqa_model_sub_category_response_instance = LQAModelSubCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(LQAModelSubCategoryResponse.to_json())

# convert the object into a dict
lqa_model_sub_category_response_dict = lqa_model_sub_category_response_instance.to_dict()
# create an instance of LQAModelSubCategoryResponse from a dict
lqa_model_sub_category_response_from_dict = LQAModelSubCategoryResponse.from_dict(lqa_model_sub_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


