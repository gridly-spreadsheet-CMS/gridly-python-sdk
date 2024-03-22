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
> Branch create(create_branch)

create

create

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import branch_api
from gridly.model.branch import Branch
from gridly.model.create_branch import CreateBranch
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
    api_instance = branch_api.BranchApi(api_client)
    create_branch = CreateBranch(
        name="name_example",
        description="description_example",
        custom_properties={
            "key": {},
        },
        inherit_group_access=True,
        inherit_automation=True,
        view_id="view_id_example",
    ) # CreateBranch | 
    grid_id = "gridId_example" # str | gridId (optional)
    branch_id = "branchId_example" # str | branchId (optional)

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(create_branch)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling BranchApi->create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # create
        api_response = api_instance.create(create_branch, grid_id=grid_id, branch_id=branch_id)
        pprint(api_response)
    except gridly.ApiException as e:
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
import time
import gridly
from gridly.api import branch_api
from gridly.model.task import Task
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
    api_instance = branch_api.BranchApi(api_client)
    source_view_id = "sourceViewId_example" # str | sourceViewId
    destination_view_id = "destinationViewId_example" # str | destinationViewId

    # example passing only required values which don't have defaults set
    try:
        # createDiffCheck
        api_response = api_instance.create_diff_check(source_view_id, destination_view_id)
        pprint(api_response)
    except gridly.ApiException as e:
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
import time
import gridly
from gridly.api import branch_api
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
    api_instance = branch_api.BranchApi(api_client)
    branch_id = "branchId_example" # str | branchId

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_instance.delete(branch_id)
    except gridly.ApiException as e:
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
import time
import gridly
from gridly.api import branch_api
from gridly.model.branch import Branch
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
    api_instance = branch_api.BranchApi(api_client)
    branch_id = "branchId_example" # str | branchId

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(branch_id)
        pprint(api_response)
    except gridly.ApiException as e:
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
> [BranchDiffRecord] get_diff_check(task_id)

getDiffCheck

getDiffCheck

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import branch_api
from gridly.model.branch_diff_record import BranchDiffRecord
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
    api_instance = branch_api.BranchApi(api_client)
    task_id = "taskId_example" # str | taskId
    merge_record_options = [
        "add",
    ] # [str], none_type | mergeRecordOptions (optional)
    query = "{}" # str, none_type | query (optional) if omitted the server will use the default value of "{}"
    page = "{}" # str, none_type | page (optional) if omitted the server will use the default value of "{}"

    # example passing only required values which don't have defaults set
    try:
        # getDiffCheck
        api_response = api_instance.get_diff_check(task_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling BranchApi->get_diff_check: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # getDiffCheck
        api_response = api_instance.get_diff_check(task_id, merge_record_options=merge_record_options, query=query, page=page)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling BranchApi->get_diff_check: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| taskId |
 **merge_record_options** | **[str], none_type**| mergeRecordOptions | [optional]
 **query** | **str, none_type**| query | [optional] if omitted the server will use the default value of "{}"
 **page** | **str, none_type**| page | [optional] if omitted the server will use the default value of "{}"

### Return type

[**[BranchDiffRecord]**](BranchDiffRecord.md)

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
> [Branch] list(grid_id)

list

list

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import branch_api
from gridly.model.branch import Branch
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
    api_instance = branch_api.BranchApi(api_client)
    grid_id = "gridId_example" # str | gridId

    # example passing only required values which don't have defaults set
    try:
        # list
        api_response = api_instance.list(grid_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling BranchApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId |

### Return type

[**[Branch]**](Branch.md)

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
> Task merge(branch_id, destination_branch_id, merge_branch_request)

merge

merge

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import branch_api
from gridly.model.merge_branch_request import MergeBranchRequest
from gridly.model.task import Task
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
    api_instance = branch_api.BranchApi(api_client)
    branch_id = "branchId_example" # str | branchId
    destination_branch_id = "destinationBranchId_example" # str | destinationBranchId
    merge_branch_request = MergeBranchRequest(
        merge_record_options=[
            "add",
        ],
        merge_record_conflicts=[
            MergeRecordConflict(
                cells=[
                    MergeCellConflict(
                        column_id="column_id_example",
                        option="child",
                    ),
                ],
                path_tag="path_tag_example",
                record_id="record_id_example",
            ),
        ],
        use_last_merge_resolve=True,
        query=[
            FilterField(
                case_sensitive=True,
                column_id="column_id_example",
                operator="isNull",
                query_path_tag_via_id=True,
                sub_field="DEPENDENCY_STATUS",
                values=[
                    {},
                ],
            ),
        ],
    ) # MergeBranchRequest | 
    merge_record_options = [] # [str], none_type | mergeRecordOptions (optional) if omitted the server will use the default value of []

    # example passing only required values which don't have defaults set
    try:
        # merge
        api_response = api_instance.merge(branch_id, destination_branch_id, merge_branch_request)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling BranchApi->merge: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # merge
        api_response = api_instance.merge(branch_id, destination_branch_id, merge_branch_request, merge_record_options=merge_record_options)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling BranchApi->merge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**| branchId |
 **destination_branch_id** | **str**| destinationBranchId |
 **merge_branch_request** | [**MergeBranchRequest**](MergeBranchRequest.md)|  |
 **merge_record_options** | **[str], none_type**| mergeRecordOptions | [optional] if omitted the server will use the default value of []

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

