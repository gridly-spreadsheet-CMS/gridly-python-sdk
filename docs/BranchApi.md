# gridly.BranchApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](BranchApi.md#create) | **POST** /v1/branches | create
[**create_diff_check**](BranchApi.md#create_diff_check) | **POST** /v1/branches/diffcheck | createDiffCheck
[**delete**](BranchApi.md#delete) | **DELETE** /v1/branches/{branchId} | delete
[**get**](BranchApi.md#get) | **GET** /v1/branches/{branchId} | get
[**get_diff_check**](BranchApi.md#get_diff_check) | **GET** /v1/branches/diffcheck/{taskId} | getDiffCheck
[**list**](BranchApi.md#list) | **GET** /v1/branches | list
[**merge**](BranchApi.md#merge) | **POST** /v1/branches/{branchId}/merge | merge


# **create**
> Branch create(create_branch, grid_id=grid_id, branch_id=branch_id)

create

create

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.branch import Branch
from gridly.models.create_branch import CreateBranch
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
    api_instance = gridly.BranchApi(api_client)
    create_branch = gridly.CreateBranch() # CreateBranch | 
    grid_id = 'grid_id_example' # str | gridId (optional)
    branch_id = 'branch_id_example' # str | branchId (optional)

    try:
        # create
        api_response = api_instance.create(create_branch, grid_id=grid_id, branch_id=branch_id)
        print("The response of BranchApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_branch** | [**CreateBranch**](CreateBranch.md)|  | 
 **grid_id** | **str**| gridId | [optional] 
 **branch_id** | **str**| branchId | [optional] 

### Return type

[**Branch**](Branch.md)

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

# **create_diff_check**
> Task create_diff_check(source_view_id, destination_view_id)

createDiffCheck

createDiffCheck

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.task import Task
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
    api_instance = gridly.BranchApi(api_client)
    source_view_id = 'source_view_id_example' # str | sourceViewId
    destination_view_id = 'destination_view_id_example' # str | destinationViewId

    try:
        # createDiffCheck
        api_response = api_instance.create_diff_check(source_view_id, destination_view_id)
        print("The response of BranchApi->create_diff_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->create_diff_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_view_id** | **str**| sourceViewId | 
 **destination_view_id** | **str**| destinationViewId | 

### Return type

[**Task**](Task.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(branch_id)

delete

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
    api_instance = gridly.BranchApi(api_client)
    branch_id = 'branch_id_example' # str | branchId

    try:
        # delete
        api_instance.delete(branch_id)
    except Exception as e:
        print("Exception when calling BranchApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**| branchId | 

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
> Branch get(branch_id)

get

get

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.branch import Branch
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
    api_instance = gridly.BranchApi(api_client)
    branch_id = 'branch_id_example' # str | branchId

    try:
        # get
        api_response = api_instance.get(branch_id)
        print("The response of BranchApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**| branchId | 

### Return type

[**Branch**](Branch.md)

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

# **get_diff_check**
> List[BranchDiffRecord] get_diff_check(task_id, merge_record_options=merge_record_options, query=query, page=page)

getDiffCheck

getDiffCheck

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.branch_diff_record import BranchDiffRecord
from gridly.models.merge_record_option import MergeRecordOption
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
    api_instance = gridly.BranchApi(api_client)
    task_id = 'task_id_example' # str | taskId
    merge_record_options = ["add","update","delete"] # List[MergeRecordOption] | mergeRecordOptions (optional) (default to ["add","update","delete"])
    query = '{}' # str | query (optional) (default to '{}')
    page = '{}' # str | page (optional) (default to '{}')

    try:
        # getDiffCheck
        api_response = api_instance.get_diff_check(task_id, merge_record_options=merge_record_options, query=query, page=page)
        print("The response of BranchApi->get_diff_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->get_diff_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| taskId | 
 **merge_record_options** | [**List[MergeRecordOption]**](MergeRecordOption.md)| mergeRecordOptions | [optional] [default to [&quot;add&quot;,&quot;update&quot;,&quot;delete&quot;]]
 **query** | **str**| query | [optional] [default to &#39;{}&#39;]
 **page** | **str**| page | [optional] [default to &#39;{}&#39;]

### Return type

[**List[BranchDiffRecord]**](BranchDiffRecord.md)

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
> List[Branch] list(grid_id)

list

list

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.branch import Branch
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
    api_instance = gridly.BranchApi(api_client)
    grid_id = 'grid_id_example' # str | gridId

    try:
        # list
        api_response = api_instance.list(grid_id)
        print("The response of BranchApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId | 

### Return type

[**List[Branch]**](Branch.md)

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

# **merge**
> Task merge(branch_id, destination_branch_id, merge_branch_request, merge_record_options=merge_record_options)

merge

merge

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.merge_branch_request import MergeBranchRequest
from gridly.models.merge_record_option import MergeRecordOption
from gridly.models.task import Task
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
    api_instance = gridly.BranchApi(api_client)
    branch_id = 'branch_id_example' # str | branchId
    destination_branch_id = 'destination_branch_id_example' # str | destinationBranchId
    merge_branch_request = gridly.MergeBranchRequest() # MergeBranchRequest | 
    merge_record_options = [] # List[MergeRecordOption] | mergeRecordOptions (optional) (default to [])

    try:
        # merge
        api_response = api_instance.merge(branch_id, destination_branch_id, merge_branch_request, merge_record_options=merge_record_options)
        print("The response of BranchApi->merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchApi->merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**| branchId | 
 **destination_branch_id** | **str**| destinationBranchId | 
 **merge_branch_request** | [**MergeBranchRequest**](MergeBranchRequest.md)|  | 
 **merge_record_options** | [**List[MergeRecordOption]**](MergeRecordOption.md)| mergeRecordOptions | [optional] [default to []]

### Return type

[**Task**](Task.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

