# ShareView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**view_id** | **str** |  | [optional] 
**include_grid_history** | **bool** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 

## Example

```python
from gridly.models.share_view import ShareView

# TODO update the JSON string below
json = "{}"
# create an instance of ShareView from a JSON string
share_view_instance = ShareView.from_json(json)
# print the JSON string representation of the object
print(ShareView.to_json())

# convert the object into a dict
share_view_dict = share_view_instance.to_dict()
# create an instance of ShareView from a dict
share_view_from_dict = ShareView.from_dict(share_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


