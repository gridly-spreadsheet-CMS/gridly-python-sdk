# View


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**columns** | [**List[ViewColumn]**](ViewColumn.md) |  | [optional] 
**grid_id** | **str** |  | [optional] 
**grid_status** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**records** | [**List[Record]**](Record.md) |  | [optional] 

## Example

```python
from gridly.models.view import View

# TODO update the JSON string below
json = "{}"
# create an instance of View from a JSON string
view_instance = View.from_json(json)
# print the JSON string representation of the object
print(View.to_json())

# convert the object into a dict
view_dict = view_instance.to_dict()
# create an instance of View from a dict
view_from_dict = View.from_dict(view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


