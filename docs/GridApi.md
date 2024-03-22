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
        id="H",
        name="name_example",
        template_grid_id="template_grid_id_example",
        record_identifier_type="recordId",
        columns=[
            CreateColumn(
                id="/qXzyC",
                name="name_example",
                description="description_example",
                type="singleLine",
                editable=True,
                language_code="enUS",
                localization_type="sourceLanguage",
                number_format=NumberFormat(
                    type="DECIMAL",
                    decimal_places=1,
                    currency_symbol="currency_symbol_example",
                    use1000_separator=True,
                ),
                selection_options=[
                    "selection_options_example",
                ],
                reference=Reference(
                    grid_id="grid_id_example",
                    branch_id="branch_id_example",
                    column_id="column_id_example",
                    type="ROW",
                    selection_type="SINGLE",
                ),
                formula=Formula(
                    formula_text="formula_text_example",
                    always_format_result_value_as_list=True,
                    detect_result_value_type="list",
                ),
                date_time_format=DateTimeFormat(
                    date_format="date_format_example",
                    time_format="time_format_example",
                    zone_offset="zone_offset_example",
                    show_time_zone=True,
                ),
            ),
        ],
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

# **create_category**
> FileCategory create_category(grid_id, create_file_category)

createCategory

createCategory

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import grid_api
from gridly.model.create_file_category import CreateFileCategory
from gridly.model.file_category import FileCategory
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
    create_file_category = CreateFileCategory(
        name="name_example",
    ) # CreateFileCategory | 

    # example passing only required values which don't have defaults set
    try:
        # createCategory
        api_response = api_instance.create_category(grid_id, create_file_category)
        pprint(api_response)
    except gridly.ApiException as e:
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

# **delete_category**
> delete_category(grid_id, category_id)

deleteCategory

deleteCategory

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
    category_id = "categoryId_example" # str | categoryId

    # example passing only required values which don't have defaults set
    try:
        # deleteCategory
        api_instance.delete_category(grid_id, category_id)
    except gridly.ApiException as e:
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
    category_id = "categoryId_example" # str | categoryId
    file_id = "fileId_example" # str | fileId

    # example passing only required values which don't have defaults set
    try:
        # deleteFile
        api_instance.delete_file(grid_id, category_id, file_id)
    except gridly.ApiException as e:
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

# **get_setting**
> GridSetting get_setting(grid_id)

getSetting

getSetting

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import grid_api
from gridly.model.grid_setting import GridSetting
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
        # getSetting
        api_response = api_instance.get_setting(grid_id)
        pprint(api_response)
    except gridly.ApiException as e:
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

# **list_files**
> [SettingFile] list_files(grid_id)

listFiles

listFiles

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import grid_api
from gridly.model.setting_file import SettingFile
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
    category_id = [
        "categoryId_example",
    ] # [str] | categoryId (optional)

    # example passing only required values which don't have defaults set
    try:
        # listFiles
        api_response = api_instance.list_files(grid_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling GridApi->list_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # listFiles
        api_response = api_instance.list_files(grid_id, category_id=category_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling GridApi->list_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId |
 **category_id** | **[str]**| categoryId | [optional]

### Return type

[**[SettingFile]**](SettingFile.md)

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

# **update_category**
> FileCategory update_category(grid_id, category_id, update_category)

updateCategory

updateCategory

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import grid_api
from gridly.model.update_category import UpdateCategory
from gridly.model.file_category import FileCategory
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
    category_id = "categoryId_example" # str | categoryId
    update_category = UpdateCategory(
        name="name_example",
    ) # UpdateCategory | 

    # example passing only required values which don't have defaults set
    try:
        # updateCategory
        api_response = api_instance.update_category(grid_id, category_id, update_category)
        pprint(api_response)
    except gridly.ApiException as e:
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
import time
import gridly
from gridly.api import grid_api
from gridly.model.grid_setting import GridSetting
from gridly.model.update_grid_setting import UpdateGridSetting
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
    update_grid_setting = UpdateGridSetting(
        default_date_time_format=DateTimeFormat(
            date_format="date_format_example",
            time_format="time_format_example",
            zone_offset="zone_offset_example",
            show_time_zone=True,
        ),
        default_source_language_status="unset",
        translator_can_view_automations=True,
        metadata={
            "key": "key_example",
        },
    ) # UpdateGridSetting | 

    # example passing only required values which don't have defaults set
    try:
        # updateSetting
        api_response = api_instance.update_setting(grid_id, update_grid_setting)
        pprint(api_response)
    except gridly.ApiException as e:
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
import time
import gridly
from gridly.api import grid_api
from gridly.model.uploaded_file import UploadedFile
from gridly.model.upload_setting_file_request import UploadSettingFileRequest
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
    category_id = "categoryId_example" # str | categoryId
    upload_setting_file_request = UploadSettingFileRequest(
        file=open('/path/to/file', 'rb'),
    ) # UploadSettingFileRequest | 

    # example passing only required values which don't have defaults set
    try:
        # uploadSettingFile
        api_response = api_instance.upload_setting_file(grid_id, category_id, upload_setting_file_request)
        pprint(api_response)
    except gridly.ApiException as e:
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

