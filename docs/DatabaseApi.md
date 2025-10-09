# gridly.DatabaseApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](DatabaseApi.md#create) | **POST** /v1/databases | create
[**delete**](DatabaseApi.md#delete) | **DELETE** /v1/databases/{dbId} | delete
[**duplicate**](DatabaseApi.md#duplicate) | **POST** /v1/databases/{dbId}/duplicate | duplicate
[**get**](DatabaseApi.md#get) | **GET** /v1/databases/{dbId} | get
[**list**](DatabaseApi.md#list) | **GET** /v1/databases | list
[**update**](DatabaseApi.md#update) | **PUT** /v1/databases/{dbId} | update


# **create**
> Database create(project_id, body)

create

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.create_database import CreateDatabase
from gridly.models.database import Database
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
    api_instance = gridly.DatabaseApi(api_client)
    project_id = 56 # int | projectId
    body = gridly.CreateDatabase() # CreateDatabase | body

    try:
        # create
        api_response = api_instance.create(project_id, body)
        print("The response of DatabaseApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| projectId | 
 **body** | [**CreateDatabase**](CreateDatabase.md)| body | 

### Return type

[**Database**](Database.md)

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
> delete(db_id)

delete

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
    api_instance = gridly.DatabaseApi(api_client)
    db_id = 'db_id_example' # str | dbId

    try:
        # delete
        api_instance.delete(db_id)
    except Exception as e:
        print("Exception when calling DatabaseApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | **str**| dbId | 

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

# **duplicate**
> Database duplicate(db_id, project_id, body)

duplicate

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.create_database import CreateDatabase
from gridly.models.database import Database
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
    api_instance = gridly.DatabaseApi(api_client)
    db_id = 'db_id_example' # str | dbId
    project_id = 56 # int | projectId
    body = gridly.CreateDatabase() # CreateDatabase | body

    try:
        # duplicate
        api_response = api_instance.duplicate(db_id, project_id, body)
        print("The response of DatabaseApi->duplicate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->duplicate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | **str**| dbId | 
 **project_id** | **int**| projectId | 
 **body** | [**CreateDatabase**](CreateDatabase.md)| body | 

### Return type

[**Database**](Database.md)

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

# **get**
> Database get(db_id)

get

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.database import Database
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
    api_instance = gridly.DatabaseApi(api_client)
    db_id = 'db_id_example' # str | dbId

    try:
        # get
        api_response = api_instance.get(db_id)
        print("The response of DatabaseApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | **str**| dbId | 

### Return type

[**Database**](Database.md)

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
> List[Database] list(expand=expand, page=page, project_id=project_id, search=search, sort=sort)

list

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.database import Database
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
    api_instance = gridly.DatabaseApi(api_client)
    expand = ['expand_example'] # List[str] | expand (optional)
    page = '' # str | page (optional) (default to '')
    project_id = 56 # int | projectId (optional)
    search = 'search_example' # str | search (optional)
    sort = '' # str | sort (optional) (default to '')

    try:
        # list
        api_response = api_instance.list(expand=expand, page=page, project_id=project_id, search=search, sort=sort)
        print("The response of DatabaseApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | [**List[str]**](str.md)| expand | [optional] 
 **page** | **str**| page | [optional] [default to &#39;&#39;]
 **project_id** | **int**| projectId | [optional] 
 **search** | **str**| search | [optional] 
 **sort** | **str**| sort | [optional] [default to &#39;&#39;]

### Return type

[**List[Database]**](Database.md)

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
> Database update(db_id, body)

update

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.database import Database
from gridly.models.update_database import UpdateDatabase
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
    api_instance = gridly.DatabaseApi(api_client)
    db_id = 'db_id_example' # str | dbId
    body = gridly.UpdateDatabase() # UpdateDatabase | body

    try:
        # update
        api_response = api_instance.update(db_id, body)
        print("The response of DatabaseApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | **str**| dbId | 
 **body** | [**UpdateDatabase**](UpdateDatabase.md)| body | 

### Return type

[**Database**](Database.md)

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

