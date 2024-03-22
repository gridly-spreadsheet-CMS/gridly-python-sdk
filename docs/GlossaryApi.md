# gridly.GlossaryApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](GlossaryApi.md#create) | **POST** /v1/glossaries | Create a new glossary
[**delete**](GlossaryApi.md#delete) | **DELETE** /v1/glossaries/{id} | Delete a glossary
[**export_file**](GlossaryApi.md#export_file) | **GET** /v1/glossaries/{id}/export | Export a glossary
[**get**](GlossaryApi.md#get) | **GET** /v1/glossaries/{id} | get glossary info
[**get_all**](GlossaryApi.md#get_all) | **GET** /v1/glossaries | List all glossaries
[**import_file**](GlossaryApi.md#import_file) | **POST** /v1/glossaries/{id}/import | Import a glossary from file
[**update**](GlossaryApi.md#update) | **PUT** /v1/glossaries/{id} | Update glossary info


# **create**
> Glossary create()

Create a new glossary

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import glossary_api
from gridly.model.glossary import Glossary
from gridly.model.create_glossary import CreateGlossary
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
    api_instance = glossary_api.GlossaryApi(api_client)
    create_glossary = CreateGlossary(
        name="o",
        description="description_example",
        langs=[
            "langs_example",
        ],
        projects=[
            GlossaryProject(
                project_id=1,
                database_ids=[
                    "database_ids_example",
                ],
            ),
        ],
    ) # CreateGlossary |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new glossary
        api_response = api_instance.create(create_glossary=create_glossary)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling GlossaryApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_glossary** | [**CreateGlossary**](CreateGlossary.md)|  | [optional]

### Return type

[**Glossary**](Glossary.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a new glossary successful ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)

Delete a glossary

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import glossary_api
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
    api_instance = glossary_api.GlossaryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a glossary
        api_instance.delete(id)
    except gridly.ApiException as e:
        print("Exception when calling GlossaryApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

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

# **export_file**
> export_file(id)

Export a glossary

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import glossary_api
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
    api_instance = glossary_api.GlossaryApi(api_client)
    id = 1 # int | 
    fields = [
        "fields_example",
    ] # [str] |  (optional)
    format = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    langs = [
        "langs_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export a glossary
        api_instance.export_file(id)
    except gridly.ApiException as e:
        print("Exception when calling GlossaryApi->export_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export a glossary
        api_instance.export_file(id, fields=fields, format=format, langs=langs)
    except gridly.ApiException as e:
        print("Exception when calling GlossaryApi->export_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **fields** | **[str]**|  | [optional]
 **format** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **langs** | **[str]**|  | [optional]

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

# **get**
> Glossary get(id)

get glossary info

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import glossary_api
from gridly.model.glossary import Glossary
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
    api_instance = glossary_api.GlossaryApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # get glossary info
        api_response = api_instance.get(id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling GlossaryApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Glossary**](Glossary.md)

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

# **get_all**
> [Glossary] get_all()

List all glossaries

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import glossary_api
from gridly.model.glossary import Glossary
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
    api_instance = glossary_api.GlossaryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all glossaries
        api_response = api_instance.get_all()
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling GlossaryApi->get_all: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Glossary]**](Glossary.md)

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

# **import_file**
> import_file(id)

Import a glossary from file

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import glossary_api
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
    api_instance = glossary_api.GlossaryApi(api_client)
    id = 1 # int | 
    import_option = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)
    file = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import a glossary from file
        api_instance.import_file(id)
    except gridly.ApiException as e:
        print("Exception when calling GlossaryApi->import_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import a glossary from file
        api_instance.import_file(id, import_option=import_option, file=file)
    except gridly.ApiException as e:
        print("Exception when calling GlossaryApi->import_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **import_option** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]
 **file** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(id)

Update glossary info

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import glossary_api
from gridly.model.update_glossary import UpdateGlossary
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
    api_instance = glossary_api.GlossaryApi(api_client)
    id = 1 # int | 
    update_glossary = UpdateGlossary(
        name="name_example",
        description="description_example",
        langs=[
            "langs_example",
        ],
        projects=[
            GlossaryProject(
                project_id=1,
                database_ids=[
                    "database_ids_example",
                ],
            ),
        ],
    ) # UpdateGlossary |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update glossary info
        api_instance.update(id)
    except gridly.ApiException as e:
        print("Exception when calling GlossaryApi->update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update glossary info
        api_instance.update(id, update_glossary=update_glossary)
    except gridly.ApiException as e:
        print("Exception when calling GlossaryApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **update_glossary** | [**UpdateGlossary**](UpdateGlossary.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

