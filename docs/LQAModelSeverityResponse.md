# LQAModelSeverityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from gridly.models.lqa_model_severity_response import LQAModelSeverityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LQAModelSeverityResponse from a JSON string
lqa_model_severity_response_instance = LQAModelSeverityResponse.from_json(json)
# print the JSON string representation of the object
print(LQAModelSeverityResponse.to_json())

# convert the object into a dict
lqa_model_severity_response_dict = lqa_model_severity_response_instance.to_dict()
# create an instance of LQAModelSeverityResponse from a dict
lqa_model_severity_response_from_dict = LQAModelSeverityResponse.from_dict(lqa_model_severity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


