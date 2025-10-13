# CreateView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**grid_id** | **str** |  | 
**columns** | [**List[AddViewColumn]**](AddViewColumn.md) |  | [optional] 

## Example

```python
from gridly.models.create_view import CreateView

# TODO update the JSON string below
json = "{}"
# create an instance of CreateView from a JSON string
create_view_instance = CreateView.from_json(json)
# print the JSON string representation of the object
print(CreateView.to_json())

# convert the object into a dict
create_view_dict = create_view_instance.to_dict()
# create an instance of CreateView from a dict
create_view_from_dict = CreateView.from_dict(create_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


