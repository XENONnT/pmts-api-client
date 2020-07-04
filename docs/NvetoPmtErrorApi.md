# xepmts.NvetoPmtErrorApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_pmt_error_item**](NvetoPmtErrorApi.md#delete_nveto_pmt_error_item) | **DELETE** /nveto/pmt_errors/{nvetopmterrorId} | Deletes a NvetoPmtError document
[**get_nveto_pmt_error_item**](NvetoPmtErrorApi.md#get_nveto_pmt_error_item) | **GET** /nveto/pmt_errors/{nvetopmterrorId} | Retrieves a NvetoPmtError document
[**get_nveto_pmt_errors**](NvetoPmtErrorApi.md#get_nveto_pmt_errors) | **GET** /nveto/pmt_errors | Retrieves one or more NvetoPmtErrors
[**post_nveto_pmt_errors**](NvetoPmtErrorApi.md#post_nveto_pmt_errors) | **POST** /nveto/pmt_errors | Stores one or more NvetoPmtErrors.
[**put_nveto_pmt_error_item**](NvetoPmtErrorApi.md#put_nveto_pmt_error_item) | **PUT** /nveto/pmt_errors/{nvetopmterrorId} | Replaces a NvetoPmtError document


# **delete_nveto_pmt_error_item**
> delete_nveto_pmt_error_item(nvetopmterror_id, if_match=if_match)

Deletes a NvetoPmtError document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.NvetoPmtErrorApi(api_client)
    nvetopmterror_id = 'nvetopmterror_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoPmtError document
        api_instance.delete_nveto_pmt_error_item(nvetopmterror_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoPmtErrorApi->delete_nveto_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetopmterror_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NvetoPmtError document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_pmt_error_item**
> NvetoPmtError get_nveto_pmt_error_item(nvetopmterror_id)

Retrieves a NvetoPmtError document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.NvetoPmtErrorApi(api_client)
    nvetopmterror_id = 'nvetopmterror_id_example' # str | 

    try:
        # Retrieves a NvetoPmtError document
        api_response = api_instance.get_nveto_pmt_error_item(nvetopmterror_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoPmtErrorApi->get_nveto_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetopmterror_id** | **str**|  | 

### Return type

[**NvetoPmtError**](NvetoPmtError.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoPmtError document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_pmt_errors**
> InlineResponse20013 get_nveto_pmt_errors(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoPmtErrors

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.NvetoPmtErrorApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoPmtErrors
        api_response = api_instance.get_nveto_pmt_errors(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoPmtErrorApi->get_nveto_pmt_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **projection** | **str**| the projections query parameter (ex.: {\&quot;name\&quot;: 1}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of NvetoPmtErrors |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_pmt_errors**
> post_nveto_pmt_errors(nveto_pmt_error)

Stores one or more NvetoPmtErrors.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.NvetoPmtErrorApi(api_client)
    nveto_pmt_error = xepmts.NvetoPmtError() # NvetoPmtError | A NvetoPmtError or list of NvetoPmtError documents

    try:
        # Stores one or more NvetoPmtErrors.
        api_instance.post_nveto_pmt_errors(nveto_pmt_error)
    except ApiException as e:
        print("Exception when calling NvetoPmtErrorApi->post_nveto_pmt_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_pmt_error** | [**NvetoPmtError**](NvetoPmtError.md)| A NvetoPmtError or list of NvetoPmtError documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | operation has been successful |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_nveto_pmt_error_item**
> put_nveto_pmt_error_item(nvetopmterror_id, nveto_pmt_error, if_match=if_match)

Replaces a NvetoPmtError document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.NvetoPmtErrorApi(api_client)
    nvetopmterror_id = 'nvetopmterror_id_example' # str | 
nveto_pmt_error = xepmts.NvetoPmtError() # NvetoPmtError | A NvetoPmtError or list of NvetoPmtError documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoPmtError document
        api_instance.put_nveto_pmt_error_item(nvetopmterror_id, nveto_pmt_error, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoPmtErrorApi->put_nveto_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetopmterror_id** | **str**|  | 
 **nveto_pmt_error** | [**NvetoPmtError**](NvetoPmtError.md)| A NvetoPmtError or list of NvetoPmtError documents | 
 **if_match** | **str**| Current value of the _etag field | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoPmtError document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

