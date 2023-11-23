# gridly.TransmemApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cleanup**](TransmemApi.md#cleanup) | **PUT** /v1/transmems/{tmId}/cleanup | Erases all the translation data of the provided tmId
[**create**](TransmemApi.md#create) | **POST** /v1/transmems | Create a new translation memory
[**create_with_file**](TransmemApi.md#create_with_file) | **POST** /v1/transmems/upload | Create a new translation memory by uploading tmx file
[**delete**](TransmemApi.md#delete) | **DELETE** /v1/transmems/{tmId} | Delete a translation memory by id
[**export**](TransmemApi.md#export) | **GET** /v1/transmems/{tmId}/export | Export translation memory tmx file
[**get**](TransmemApi.md#get) | **GET** /v1/transmems/{tmId} | Get translation memory info by id
[**import_tmx**](TransmemApi.md#import_tmx) | **POST** /v1/transmems/{tmId}/import | Import a translation memory from tmx file
[**list_tm**](TransmemApi.md#list_tm) | **GET** /v1/transmems | List all available translation memories or create default one if there is no translation memory
[**update**](TransmemApi.md#update) | **PUT** /v1/transmems/{tmId} | Update a translation memory


# **cleanup**
> cleanup(tm_id)

Erases all the translation data of the provided tmId

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import transmem_api
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
    api_instance = transmem_api.TransmemApi(api_client)
    tm_id = "tmId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Erases all the translation data of the provided tmId
        api_instance.cleanup(tm_id)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->cleanup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tm_id** | **str**|  |

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

# **create**
> TransMem create()

Create a new translation memory

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import transmem_api
from gridly.model.trans_mem import TransMem
from gridly.model.create_trans_mem import CreateTransMem
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
    api_instance = transmem_api.TransmemApi(api_client)
    create_trans_mem = CreateTransMem(
        name="o",
        description="description_example",
        project_ids=[
            1,
        ],
        fuzzy_match=True,
        is_disabled=True,
        is_paused_consuming=True,
        context_lookup=True,
        populate_translation_status=TranslationStatus("upToDate"),
    ) # CreateTransMem |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new translation memory
        api_response = api_instance.create(create_trans_mem=create_trans_mem)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_trans_mem** | [**CreateTransMem**](CreateTransMem.md)|  | [optional]

### Return type

[**TransMem**](TransMem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a new translation memory successful ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_with_file**
> TransMem create_with_file(file)

Create a new translation memory by uploading tmx file

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import transmem_api
from gridly.model.trans_mem import TransMem
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
    api_instance = transmem_api.TransmemApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new translation memory by uploading tmx file
        api_response = api_instance.create_with_file(file)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->create_with_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**|  |

### Return type

[**TransMem**](TransMem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a new translation memory based on provided tmx file successfully ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> TransMem delete(tm_id)

Delete a translation memory by id

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import transmem_api
from gridly.model.trans_mem import TransMem
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
    api_instance = transmem_api.TransmemApi(api_client)
    tm_id = "tmId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a translation memory by id
        api_response = api_instance.delete(tm_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tm_id** | **str**|  |

### Return type

[**TransMem**](TransMem.md)

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

# **export**
> file_type export(tm_id)

Export translation memory tmx file

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import transmem_api
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
    api_instance = transmem_api.TransmemApi(api_client)
    tm_id = "tmId_example" # str | 
    format = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    source_lang = "sourceLang_example" # str |  (optional)
    target_langs = [
        "targetLangs_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export translation memory tmx file
        api_response = api_instance.export(tm_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export translation memory tmx file
        api_response = api_instance.export(tm_id, format=format, source_lang=source_lang, target_langs=target_langs)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tm_id** | **str**|  |
 **format** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **source_lang** | **str**|  | [optional]
 **target_langs** | **[str]**|  | [optional]

### Return type

**file_type**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> TransMem get(tm_id)

Get translation memory info by id

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import transmem_api
from gridly.model.trans_mem import TransMem
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
    api_instance = transmem_api.TransmemApi(api_client)
    tm_id = "tmId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get translation memory info by id
        api_response = api_instance.get(tm_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tm_id** | **str**|  |

### Return type

[**TransMem**](TransMem.md)

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

# **import_tmx**
> import_tmx(tm_id, file)

Import a translation memory from tmx file

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import transmem_api
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
    api_instance = transmem_api.TransmemApi(api_client)
    tm_id = "tmId_example" # str | 
    file = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # Import a translation memory from tmx file
        api_instance.import_tmx(tm_id, file)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->import_tmx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tm_id** | **str**|  |
 **file** | **file_type**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import tmx file successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tm**
> [TransMem] list_tm()

List all available translation memories or create default one if there is no translation memory

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import transmem_api
from gridly.model.trans_mem import TransMem
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
    api_instance = transmem_api.TransmemApi(api_client)
    project_id = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all available translation memories or create default one if there is no translation memory
        api_response = api_instance.list_tm(project_id=project_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->list_tm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | [optional]

### Return type

[**[TransMem]**](TransMem.md)

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
> TransMem update(tm_id)

Update a translation memory

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import transmem_api
from gridly.model.update_trans_mem import UpdateTransMem
from gridly.model.trans_mem import TransMem
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
    api_instance = transmem_api.TransmemApi(api_client)
    tm_id = "tmId_example" # str | 
    update_trans_mem = UpdateTransMem(
        name="name_example",
        description="description_example",
        project_ids=[
            1,
        ],
        fuzzy_match=True,
        is_disabled=True,
        is_paused_consuming=True,
        populate_translation_status=TranslationStatus("upToDate"),
        context_lookup=True,
    ) # UpdateTransMem |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a translation memory
        api_response = api_instance.update(tm_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a translation memory
        api_response = api_instance.update(tm_id, update_trans_mem=update_trans_mem)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling TransmemApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tm_id** | **str**|  |
 **update_trans_mem** | [**UpdateTransMem**](UpdateTransMem.md)|  | [optional]

### Return type

[**TransMem**](TransMem.md)

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

