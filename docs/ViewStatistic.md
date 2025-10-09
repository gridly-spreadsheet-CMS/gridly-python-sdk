# ViewStatistic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_count** | **int** |  | [optional] 
**translations** | [**Dict[str, ColumnStatistic]**](ColumnStatistic.md) |  | [optional] 

## Example

```python
from gridly.models.view_statistic import ViewStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of ViewStatistic from a JSON string
view_statistic_instance = ViewStatistic.from_json(json)
# print the JSON string representation of the object
print(ViewStatistic.to_json())

# convert the object into a dict
view_statistic_dict = view_statistic_instance.to_dict()
# create an instance of ViewStatistic from a dict
view_statistic_from_dict = ViewStatistic.from_dict(view_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


