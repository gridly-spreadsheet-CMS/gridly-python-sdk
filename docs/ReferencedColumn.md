# ReferencedColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**selection_options** | **List[str]** |  | [optional] 

## Example

```python
from gridly.models.referenced_column import ReferencedColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedColumn from a JSON string
referenced_column_instance = ReferencedColumn.from_json(json)
# print the JSON string representation of the object
print(ReferencedColumn.to_json())

# convert the object into a dict
referenced_column_dict = referenced_column_instance.to_dict()
# create an instance of ReferencedColumn from a dict
referenced_column_from_dict = ReferencedColumn.from_dict(referenced_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


