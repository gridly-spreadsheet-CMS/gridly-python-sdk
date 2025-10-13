# CDN


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**grid_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**last_generated_time** | **datetime** |  | [optional] 
**last_published_time** | **datetime** |  | [optional] 
**permission** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**last_modified_time** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**white_list_ip** | **str** |  | [optional] 

## Example

```python
from gridly.models.cdn import CDN

# TODO update the JSON string below
json = "{}"
# create an instance of CDN from a JSON string
cdn_instance = CDN.from_json(json)
# print the JSON string representation of the object
print(CDN.to_json())

# convert the object into a dict
cdn_dict = cdn_instance.to_dict()
# create an instance of CDN from a dict
cdn_from_dict = CDN.from_dict(cdn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


