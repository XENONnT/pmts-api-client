# xepmts.MuvetoPmtErrorApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_pmt_error_item**](MuvetoPmtErrorApi.md#delete_muveto_pmt_error_item) | **DELETE** /muveto/pmt_errors/{muvetopmterrorId} | Deletes a MuvetoPmtError document
[**get_muveto_pmt_error_item**](MuvetoPmtErrorApi.md#get_muveto_pmt_error_item) | **GET** /muveto/pmt_errors/{muvetopmterrorId} | Retrieves a MuvetoPmtError document
[**get_muveto_pmt_errors**](MuvetoPmtErrorApi.md#get_muveto_pmt_errors) | **GET** /muveto/pmt_errors | Retrieves one or more MuvetoPmtErrors
[**post_muveto_pmt_errors**](MuvetoPmtErrorApi.md#post_muveto_pmt_errors) | **POST** /muveto/pmt_errors | Stores one or more MuvetoPmtErrors.
[**put_muveto_pmt_error_item**](MuvetoPmtErrorApi.md#put_muveto_pmt_error_item) | **PUT** /muveto/pmt_errors/{muvetopmterrorId} | Replaces a MuvetoPmtError document


# **delete_muveto_pmt_error_item**
> delete_muveto_pmt_error_item(muvetopmterror_id, if_match=if_match)

Deletes a MuvetoPmtError document

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
    api_instance = xepmts.MuvetoPmtErrorApi(api_client)
    muvetopmterror_id = 'muvetopmterror_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoPmtError document
        api_instance.delete_muveto_pmt_error_item(muvetopmterror_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoPmtErrorApi->delete_muveto_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetopmterror_id** | **str**|  | 
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
**204** | MuvetoPmtError document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_pmt_error_item**
> MuvetoPmtError get_muveto_pmt_error_item(muvetopmterror_id)

Retrieves a MuvetoPmtError document

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
    api_instance = xepmts.MuvetoPmtErrorApi(api_client)
    muvetopmterror_id = 'muvetopmterror_id_example' # str | 

    try:
        # Retrieves a MuvetoPmtError document
        api_response = api_instance.get_muveto_pmt_error_item(muvetopmterror_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoPmtErrorApi->get_muveto_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetopmterror_id** | **str**|  | 

### Return type

[**MuvetoPmtError**](MuvetoPmtError.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoPmtError document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_pmt_errors**
> InlineResponse20024 get_muveto_pmt_errors(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoPmtErrors

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
    api_instance = xepmts.MuvetoPmtErrorApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoPmtErrors
        api_response = api_instance.get_muveto_pmt_errors(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoPmtErrorApi->get_muveto_pmt_errors: %s\n" % e)
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

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoPmtErrors |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_pmt_errors**
> post_muveto_pmt_errors(muveto_pmt_error)

Stores one or more MuvetoPmtErrors.

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
    api_instance = xepmts.MuvetoPmtErrorApi(api_client)
    muveto_pmt_error = xepmts.MuvetoPmtError() # MuvetoPmtError | A MuvetoPmtError or list of MuvetoPmtError documents

    try:
        # Stores one or more MuvetoPmtErrors.
        api_instance.post_muveto_pmt_errors(muveto_pmt_error)
    except ApiException as e:
        print("Exception when calling MuvetoPmtErrorApi->post_muveto_pmt_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_pmt_error** | [**MuvetoPmtError**](MuvetoPmtError.md)| A MuvetoPmtError or list of MuvetoPmtError documents | 

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

# **put_muveto_pmt_error_item**
> put_muveto_pmt_error_item(muvetopmterror_id, muveto_pmt_error, if_match=if_match)

Replaces a MuvetoPmtError document

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
    api_instance = xepmts.MuvetoPmtErrorApi(api_client)
    muvetopmterror_id = 'muvetopmterror_id_example' # str | 
muveto_pmt_error = xepmts.MuvetoPmtError() # MuvetoPmtError | A MuvetoPmtError or list of MuvetoPmtError documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoPmtError document
        api_instance.put_muveto_pmt_error_item(muvetopmterror_id, muveto_pmt_error, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoPmtErrorApi->put_muveto_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetopmterror_id** | **str**|  | 
 **muveto_pmt_error** | [**MuvetoPmtError**](MuvetoPmtError.md)| A MuvetoPmtError or list of MuvetoPmtError documents | 
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
**200** | MuvetoPmtError document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

