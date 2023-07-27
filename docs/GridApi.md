# gridly.GridApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](GridApi.md#create) | **POST** /v1/grids | create
[**delete**](GridApi.md#delete) | **DELETE** /v1/grids/{gridId} | delete
[**get**](GridApi.md#get) | **GET** /v1/grids/{gridId} | get
[**list**](GridApi.md#list) | **GET** /v1/grids | list
[**list_template_grids**](GridApi.md#list_template_grids) | **GET** /v1/template-grids | listTemplateGrids
[**update**](GridApi.md#update) | **PATCH** /v1/grids/{gridId} | update


# **create**
> Grid create(db_id, create_grid)

create

Create a Grid

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import grid_api
from gridly.model.create_grid import CreateGrid
from gridly.model.grid import Grid
from pprint import pprint
# Defining the host is optional and defaults to https://api.gridly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gridly.Configuration(
    host = "https://api.gridly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grid_api.GridApi(api_client)
    db_id = "dbId_example" # str | dbId
    create_grid = CreateGrid(
        name="name_example",
        template_grid_id="template_grid_id_example",
        record_identifier_type="recordId",
        metadata={
            "key": "key_example",
        },
    ) # CreateGrid | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(db_id, create_grid)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling GridApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | **str**| dbId |
 **create_grid** | [**CreateGrid**](CreateGrid.md)|  |

### Return type

[**Grid**](Grid.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(grid_id)

delete

Delete a Grid

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import grid_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.gridly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gridly.Configuration(
    host = "https://api.gridly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grid_api.GridApi(api_client)
    grid_id = "gridId_example" # str | gridId

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_instance.delete(grid_id)
    except gridly.ApiException as e:
        print("Exception when calling GridApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Grid get(grid_id)

get

Get a Grid

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import grid_api
from gridly.model.grid import Grid
from pprint import pprint
# Defining the host is optional and defaults to https://api.gridly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gridly.Configuration(
    host = "https://api.gridly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grid_api.GridApi(api_client)
    grid_id = "gridId_example" # str | gridId

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(grid_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling GridApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId |

### Return type

[**Grid**](Grid.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> [Grid] list(db_id)

list

Get a Grid

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import grid_api
from gridly.model.grid import Grid
from pprint import pprint
# Defining the host is optional and defaults to https://api.gridly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gridly.Configuration(
    host = "https://api.gridly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grid_api.GridApi(api_client)
    db_id = "dbId_example" # str | dbId

    # example passing only required values which don't have defaults set
    try:
        # list
        api_response = api_instance.list(db_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling GridApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | **str**| dbId |

### Return type

[**[Grid]**](Grid.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_template_grids**
> [Grid] list_template_grids()

listTemplateGrids

listTemplateGrids

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import grid_api
from gridly.model.grid import Grid
from pprint import pprint
# Defining the host is optional and defaults to https://api.gridly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gridly.Configuration(
    host = "https://api.gridly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grid_api.GridApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # listTemplateGrids
        api_response = api_instance.list_template_grids()
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling GridApi->list_template_grids: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Grid]**](Grid.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Grid update(grid_id, update_grid)

update

Update a Grid

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import grid_api
from gridly.model.grid import Grid
from gridly.model.update_grid import UpdateGrid
from pprint import pprint
# Defining the host is optional and defaults to https://api.gridly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gridly.Configuration(
    host = "https://api.gridly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grid_api.GridApi(api_client)
    grid_id = "gridId_example" # str | gridId
    update_grid = UpdateGrid(
        name="name_example",
        metadata={
            "key": "key_example",
        },
    ) # UpdateGrid | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(grid_id, update_grid)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling GridApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId |
 **update_grid** | [**UpdateGrid**](UpdateGrid.md)|  |

### Return type

[**Grid**](Grid.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

