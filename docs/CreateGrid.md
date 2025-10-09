# CreateGrid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**template_grid_id** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**record_identifier_type** | **str** |  | [default to 'recordId']
**columns** | [**List[CreateColumn]**](CreateColumn.md) |  | [optional] 

## Example

```python
from gridly.models.create_grid import CreateGrid

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGrid from a JSON string
create_grid_instance = CreateGrid.from_json(json)
# print the JSON string representation of the object
print(CreateGrid.to_json())

# convert the object into a dict
create_grid_dict = create_grid_instance.to_dict()
# create an instance of CreateGrid from a dict
create_grid_from_dict = CreateGrid.from_dict(create_grid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


