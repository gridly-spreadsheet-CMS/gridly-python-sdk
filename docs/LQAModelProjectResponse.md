# LQAModelProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from gridly.models.lqa_model_project_response import LQAModelProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LQAModelProjectResponse from a JSON string
lqa_model_project_response_instance = LQAModelProjectResponse.from_json(json)
# print the JSON string representation of the object
print(LQAModelProjectResponse.to_json())

# convert the object into a dict
lqa_model_project_response_dict = lqa_model_project_response_instance.to_dict()
# create an instance of LQAModelProjectResponse from a dict
lqa_model_project_response_from_dict = LQAModelProjectResponse.from_dict(lqa_model_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


