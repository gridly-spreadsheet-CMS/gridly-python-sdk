# gridly.ProjectApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ProjectApi.md#create) | **POST** /v1/projects | create
[**delete**](ProjectApi.md#delete) | **DELETE** /v1/projects/{projectId} | delete
[**find_one**](ProjectApi.md#find_one) | **GET** /v1/projects/{projectId} | findOne
[**list**](ProjectApi.md#list) | **GET** /v1/projects | list
[**update**](ProjectApi.md#update) | **PUT** /v1/projects/{projectId} | update


# **create**
> Project create(create_project)

create

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import project_api
from gridly.model.create_project import CreateProject
from gridly.model.project import Project
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
    api_instance = project_api.ProjectApi(api_client)
    create_project = CreateProject(
        name="name_example",
        description="description_example",
    ) # CreateProject | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(create_project)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ProjectApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project** | [**CreateProject**](CreateProject.md)|  |

### Return type

[**Project**](Project.md)

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
> delete(project_id)

delete

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import project_api
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
    api_instance = project_api.ProjectApi(api_client)
    project_id = 1 # int | projectId

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_instance.delete(project_id)
    except gridly.ApiException as e:
        print("Exception when calling ProjectApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| projectId |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_one**
> ProjectDetail find_one(project_id)

findOne

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import project_api
from gridly.model.project_detail import ProjectDetail
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
    api_instance = project_api.ProjectApi(api_client)
    project_id = 1 # int | projectId

    # example passing only required values which don't have defaults set
    try:
        # findOne
        api_response = api_instance.find_one(project_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ProjectApi->find_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| projectId |

### Return type

[**ProjectDetail**](ProjectDetail.md)

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
> [Project] list()

list

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import project_api
from gridly.model.project import Project
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
    api_instance = project_api.ProjectApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # list
        api_response = api_instance.list()
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ProjectApi->list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Project]**](Project.md)

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
> Project update(project_id, update_project)

update

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import project_api
from gridly.model.project import Project
from gridly.model.update_project import UpdateProject
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
    api_instance = project_api.ProjectApi(api_client)
    project_id = 1 # int | projectId
    update_project = UpdateProject(
        name="name_example",
        description="description_example",
    ) # UpdateProject | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(project_id, update_project)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ProjectApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| projectId |
 **update_project** | [**UpdateProject**](UpdateProject.md)|  |

### Return type

[**Project**](Project.md)

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

