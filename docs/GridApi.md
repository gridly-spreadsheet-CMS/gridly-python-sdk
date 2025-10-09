# gridly.GridApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](GridApi.md#create) | **POST** /v1/grids | create
[**create_category**](GridApi.md#create_category) | **POST** /v1/grids/{gridId}/settings/categories | createCategory
[**delete**](GridApi.md#delete) | **DELETE** /v1/grids/{gridId} | delete
[**delete_category**](GridApi.md#delete_category) | **DELETE** /v1/grids/{gridId}/settings/categories/{categoryId} | deleteCategory
[**delete_file**](GridApi.md#delete_file) | **DELETE** /v1/grids/{gridId}/settings/categories/{categoryId}/files/{fileId} | deleteFile
[**get**](GridApi.md#get) | **GET** /v1/grids/{gridId} | get
[**get_setting**](GridApi.md#get_setting) | **GET** /v1/grids/{gridId}/settings | getSetting
[**list**](GridApi.md#list) | **GET** /v1/grids | list
[**list_files**](GridApi.md#list_files) | **GET** /v1/grids/{gridId}/settings/files | listFiles
[**list_template_grids**](GridApi.md#list_template_grids) | **GET** /v1/template-grids | listTemplateGrids
[**update**](GridApi.md#update) | **PATCH** /v1/grids/{gridId} | update
[**update_category**](GridApi.md#update_category) | **PUT** /v1/grids/{gridId}/settings/categories/{categoryId} | updateCategory
[**update_setting**](GridApi.md#update_setting) | **PATCH** /v1/grids/{gridId}/settings | updateSetting
[**upload_setting_file**](GridApi.md#upload_setting_file) | **POST** /v1/grids/{gridId}/settings/categories/{categoryId}/files | uploadSettingFile


# **create**
> Grid create(db_id, create_grid)

create

Create a Grid

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.create_grid import CreateGrid
from gridly.models.grid import Grid
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    db_id = 'db_id_example' # str | dbId
    create_grid = gridly.CreateGrid() # CreateGrid | 

    try:
        # create
        api_response = api_instance.create(db_id, create_grid)
        print("The response of GridApi->create:\n")
        pprint(api_response)
    except Exception as e:
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

# **create_category**
> FileCategory create_category(grid_id, create_file_category)

createCategory

createCategory

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.create_file_category import CreateFileCategory
from gridly.models.file_category import FileCategory
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId
    create_file_category = gridly.CreateFileCategory() # CreateFileCategory | 

    try:
        # createCategory
        api_response = api_instance.create_category(grid_id, create_file_category)
        print("The response of GridApi->create_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridApi->create_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId | 
 **create_file_category** | [**CreateFileCategory**](CreateFileCategory.md)|  | 

### Return type

[**FileCategory**](FileCategory.md)

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

# **delete**
> delete(grid_id)

delete

Delete a Grid

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId

    try:
        # delete
        api_instance.delete(grid_id)
    except Exception as e:
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

# **delete_category**
> delete_category(grid_id, category_id)

deleteCategory

deleteCategory

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId
    category_id = 'category_id_example' # str | categoryId

    try:
        # deleteCategory
        api_instance.delete_category(grid_id, category_id)
    except Exception as e:
        print("Exception when calling GridApi->delete_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId | 
 **category_id** | **str**| categoryId | 

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

# **delete_file**
> delete_file(grid_id, category_id, file_id)

deleteFile

deleteFile

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId
    category_id = 'category_id_example' # str | categoryId
    file_id = 'file_id_example' # str | fileId

    try:
        # deleteFile
        api_instance.delete_file(grid_id, category_id, file_id)
    except Exception as e:
        print("Exception when calling GridApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId | 
 **category_id** | **str**| categoryId | 
 **file_id** | **str**| fileId | 

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
import gridly
from gridly.models.grid import Grid
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId

    try:
        # get
        api_response = api_instance.get(grid_id)
        print("The response of GridApi->get:\n")
        pprint(api_response)
    except Exception as e:
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

# **get_setting**
> GridSetting get_setting(grid_id)

getSetting

getSetting

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.grid_setting import GridSetting
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId

    try:
        # getSetting
        api_response = api_instance.get_setting(grid_id)
        print("The response of GridApi->get_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridApi->get_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId | 

### Return type

[**GridSetting**](GridSetting.md)

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
> List[Grid] list(db_id, query=query)

list

Get a Grid

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.grid import Grid
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    db_id = 'db_id_example' # str | dbId
    query = '{}' # str | query (optional) (default to '{}')

    try:
        # list
        api_response = api_instance.list(db_id, query=query)
        print("The response of GridApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | **str**| dbId | 
 **query** | **str**| query | [optional] [default to &#39;{}&#39;]

### Return type

[**List[Grid]**](Grid.md)

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

# **list_files**
> List[SettingFile] list_files(grid_id, category_id=category_id)

listFiles

listFiles

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.setting_file import SettingFile
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId
    category_id = ['category_id_example'] # List[str] | categoryId (optional)

    try:
        # listFiles
        api_response = api_instance.list_files(grid_id, category_id=category_id)
        print("The response of GridApi->list_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridApi->list_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId | 
 **category_id** | [**List[str]**](str.md)| categoryId | [optional] 

### Return type

[**List[SettingFile]**](SettingFile.md)

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
> List[Grid] list_template_grids()

listTemplateGrids

listTemplateGrids

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.grid import Grid
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)

    try:
        # listTemplateGrids
        api_response = api_instance.list_template_grids()
        print("The response of GridApi->list_template_grids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridApi->list_template_grids: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Grid]**](Grid.md)

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
import gridly
from gridly.models.grid import Grid
from gridly.models.update_grid import UpdateGrid
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId
    update_grid = gridly.UpdateGrid() # UpdateGrid | 

    try:
        # update
        api_response = api_instance.update(grid_id, update_grid)
        print("The response of GridApi->update:\n")
        pprint(api_response)
    except Exception as e:
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

# **update_category**
> FileCategory update_category(grid_id, category_id, update_category)

updateCategory

updateCategory

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.file_category import FileCategory
from gridly.models.update_category import UpdateCategory
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId
    category_id = 'category_id_example' # str | categoryId
    update_category = gridly.UpdateCategory() # UpdateCategory | 

    try:
        # updateCategory
        api_response = api_instance.update_category(grid_id, category_id, update_category)
        print("The response of GridApi->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridApi->update_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId | 
 **category_id** | **str**| categoryId | 
 **update_category** | [**UpdateCategory**](UpdateCategory.md)|  | 

### Return type

[**FileCategory**](FileCategory.md)

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

# **update_setting**
> GridSetting update_setting(grid_id, update_grid_setting)

updateSetting

updateSetting

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.grid_setting import GridSetting
from gridly.models.update_grid_setting import UpdateGridSetting
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId
    update_grid_setting = gridly.UpdateGridSetting() # UpdateGridSetting | 

    try:
        # updateSetting
        api_response = api_instance.update_setting(grid_id, update_grid_setting)
        print("The response of GridApi->update_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridApi->update_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId | 
 **update_grid_setting** | [**UpdateGridSetting**](UpdateGridSetting.md)|  | 

### Return type

[**GridSetting**](GridSetting.md)

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

# **upload_setting_file**
> UploadedFile upload_setting_file(grid_id, category_id, upload_setting_file_request)

uploadSettingFile

uploadSettingFile

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.upload_setting_file_request import UploadSettingFileRequest
from gridly.models.uploaded_file import UploadedFile
from gridly.rest import ApiException
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
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.GridApi(api_client)
    grid_id = 'grid_id_example' # str | gridId
    category_id = 'category_id_example' # str | categoryId
    upload_setting_file_request = gridly.UploadSettingFileRequest() # UploadSettingFileRequest | 

    try:
        # uploadSettingFile
        api_response = api_instance.upload_setting_file(grid_id, category_id, upload_setting_file_request)
        print("The response of GridApi->upload_setting_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GridApi->upload_setting_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId | 
 **category_id** | **str**| categoryId | 
 **upload_setting_file_request** | [**UploadSettingFileRequest**](UploadSettingFileRequest.md)|  | 

### Return type

[**UploadedFile**](UploadedFile.md)

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

