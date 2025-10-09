# CreateShareView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_grid_history** | **bool** |  | [optional] 
**regenerate** | **bool** |  | [optional] 

## Example

```python
from gridly.models.create_share_view import CreateShareView

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShareView from a JSON string
create_share_view_instance = CreateShareView.from_json(json)
# print the JSON string representation of the object
print(CreateShareView.to_json())

# convert the object into a dict
create_share_view_dict = create_share_view_instance.to_dict()
# create an instance of CreateShareView from a dict
create_share_view_from_dict = CreateShareView.from_dict(create_share_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


