# LQAModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**is_system** | **bool** |  | [optional] 
**status** | [**LQAModelStatus**](LQAModelStatus.md) |  | [optional] 
**categories** | [**List[LQAModelCategoryResponse]**](LQAModelCategoryResponse.md) |  | [optional] 
**severities** | [**List[LQAModelSeverityResponse]**](LQAModelSeverityResponse.md) |  | [optional] 
**projects** | [**List[LQAModelProjectResponse]**](LQAModelProjectResponse.md) |  | [optional] 

## Example

```python
from gridly.models.lqa_model_response import LQAModelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LQAModelResponse from a JSON string
lqa_model_response_instance = LQAModelResponse.from_json(json)
# print the JSON string representation of the object
print(LQAModelResponse.to_json())

# convert the object into a dict
lqa_model_response_dict = lqa_model_response_instance.to_dict()
# create an instance of LQAModelResponse from a dict
lqa_model_response_from_dict = LQAModelResponse.from_dict(lqa_model_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


