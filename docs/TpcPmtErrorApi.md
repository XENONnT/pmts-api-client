# xepmts.TpcPmtErrorApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_pmt_error_item**](TpcPmtErrorApi.md#delete_tpc_pmt_error_item) | **DELETE** /tpc/pmt_errors/{tpcpmterrorId} | Deletes a TpcPmtError document
[**get_tpc_pmt_error_item**](TpcPmtErrorApi.md#get_tpc_pmt_error_item) | **GET** /tpc/pmt_errors/{tpcpmterrorId} | Retrieves a TpcPmtError document
[**get_tpc_pmt_errors**](TpcPmtErrorApi.md#get_tpc_pmt_errors) | **GET** /tpc/pmt_errors | Retrieves one or more TpcPmtErrors
[**patch_tpc_pmt_error_item**](TpcPmtErrorApi.md#patch_tpc_pmt_error_item) | **PATCH** /tpc/pmt_errors/{tpcpmterrorId} | Updates a TpcPmtError document
[**post_tpc_pmt_errors**](TpcPmtErrorApi.md#post_tpc_pmt_errors) | **POST** /tpc/pmt_errors | Stores one or more TpcPmtErrors.
[**put_tpc_pmt_error_item**](TpcPmtErrorApi.md#put_tpc_pmt_error_item) | **PUT** /tpc/pmt_errors/{tpcpmterrorId} | Replaces a TpcPmtError document


# **delete_tpc_pmt_error_item**
> delete_tpc_pmt_error_item(tpcpmterror_id, if_match=if_match)

Deletes a TpcPmtError document

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

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcPmtErrorApi(api_client)
    tpcpmterror_id = 'tpcpmterror_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcPmtError document
        api_instance.delete_tpc_pmt_error_item(tpcpmterror_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcPmtErrorApi->delete_tpc_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmterror_id** | **str**|  | 
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
**204** | TpcPmtError document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_pmt_error_item**
> TpcPmtError get_tpc_pmt_error_item(tpcpmterror_id)

Retrieves a TpcPmtError document

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

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcPmtErrorApi(api_client)
    tpcpmterror_id = 'tpcpmterror_id_example' # str | 

    try:
        # Retrieves a TpcPmtError document
        api_response = api_instance.get_tpc_pmt_error_item(tpcpmterror_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcPmtErrorApi->get_tpc_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmterror_id** | **str**|  | 

### Return type

[**TpcPmtError**](TpcPmtError.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcPmtError document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_pmt_errors**
> InlineResponse2009 get_tpc_pmt_errors(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcPmtErrors

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

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcPmtErrorApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcPmtErrors
        api_response = api_instance.get_tpc_pmt_errors(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcPmtErrorApi->get_tpc_pmt_errors: %s\n" % e)
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

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcPmtErrors |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tpc_pmt_error_item**
> patch_tpc_pmt_error_item(tpcpmterror_id, tpc_pmt_error, if_match=if_match)

Updates a TpcPmtError document

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

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcPmtErrorApi(api_client)
    tpcpmterror_id = 'tpcpmterror_id_example' # str | 
tpc_pmt_error = xepmts.TpcPmtError() # TpcPmtError | A TpcPmtError or list of TpcPmtError documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a TpcPmtError document
        api_instance.patch_tpc_pmt_error_item(tpcpmterror_id, tpc_pmt_error, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcPmtErrorApi->patch_tpc_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmterror_id** | **str**|  | 
 **tpc_pmt_error** | [**TpcPmtError**](TpcPmtError.md)| A TpcPmtError or list of TpcPmtError documents | 
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
**200** | TpcPmtError document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_pmt_errors**
> post_tpc_pmt_errors(tpc_pmt_error)

Stores one or more TpcPmtErrors.

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

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcPmtErrorApi(api_client)
    tpc_pmt_error = xepmts.TpcPmtError() # TpcPmtError | A TpcPmtError or list of TpcPmtError documents

    try:
        # Stores one or more TpcPmtErrors.
        api_instance.post_tpc_pmt_errors(tpc_pmt_error)
    except ApiException as e:
        print("Exception when calling TpcPmtErrorApi->post_tpc_pmt_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_pmt_error** | [**TpcPmtError**](TpcPmtError.md)| A TpcPmtError or list of TpcPmtError documents | 

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

# **put_tpc_pmt_error_item**
> put_tpc_pmt_error_item(tpcpmterror_id, tpc_pmt_error, if_match=if_match)

Replaces a TpcPmtError document

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

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcPmtErrorApi(api_client)
    tpcpmterror_id = 'tpcpmterror_id_example' # str | 
tpc_pmt_error = xepmts.TpcPmtError() # TpcPmtError | A TpcPmtError or list of TpcPmtError documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcPmtError document
        api_instance.put_tpc_pmt_error_item(tpcpmterror_id, tpc_pmt_error, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcPmtErrorApi->put_tpc_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmterror_id** | **str**|  | 
 **tpc_pmt_error** | [**TpcPmtError**](TpcPmtError.md)| A TpcPmtError or list of TpcPmtError documents | 
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
**200** | TpcPmtError document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

