# xepmts.TpcAfterpulseApi

All URIs are relative to *https://xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_afterpulse_item**](TpcAfterpulseApi.md#delete_tpc_afterpulse_item) | **DELETE** /tpc/afterpules/{tpcafterpulseId} | Deletes a TpcAfterpulse document
[**get_tpc_afterpulse_item**](TpcAfterpulseApi.md#get_tpc_afterpulse_item) | **GET** /tpc/afterpules/{tpcafterpulseId} | Retrieves a TpcAfterpulse document
[**get_tpc_afterpulses**](TpcAfterpulseApi.md#get_tpc_afterpulses) | **GET** /tpc/afterpules | Retrieves one or more TpcAfterpulses
[**patch_tpc_afterpulse_item**](TpcAfterpulseApi.md#patch_tpc_afterpulse_item) | **PATCH** /tpc/afterpules/{tpcafterpulseId} | Updates a TpcAfterpulse document
[**post_tpc_afterpulses**](TpcAfterpulseApi.md#post_tpc_afterpulses) | **POST** /tpc/afterpules | Stores one or more TpcAfterpulses.
[**put_tpc_afterpulse_item**](TpcAfterpulseApi.md#put_tpc_afterpulse_item) | **PUT** /tpc/afterpules/{tpcafterpulseId} | Replaces a TpcAfterpulse document


# **delete_tpc_afterpulse_item**
> delete_tpc_afterpulse_item(tpcafterpulse_id, if_match=if_match)

Deletes a TpcAfterpulse document

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcAfterpulseApi(api_client)
    tpcafterpulse_id = 'tpcafterpulse_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcAfterpulse document
        api_instance.delete_tpc_afterpulse_item(tpcafterpulse_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcAfterpulseApi->delete_tpc_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcafterpulse_id** | **str**|  | 
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
**204** | TpcAfterpulse document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_afterpulse_item**
> TpcAfterpulse get_tpc_afterpulse_item(tpcafterpulse_id)

Retrieves a TpcAfterpulse document

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcAfterpulseApi(api_client)
    tpcafterpulse_id = 'tpcafterpulse_id_example' # str | 

    try:
        # Retrieves a TpcAfterpulse document
        api_response = api_instance.get_tpc_afterpulse_item(tpcafterpulse_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcAfterpulseApi->get_tpc_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcafterpulse_id** | **str**|  | 

### Return type

[**TpcAfterpulse**](TpcAfterpulse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcAfterpulse document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_afterpulses**
> InlineResponse2001 get_tpc_afterpulses(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcAfterpulses

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcAfterpulseApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcAfterpulses
        api_response = api_instance.get_tpc_afterpulses(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcAfterpulseApi->get_tpc_afterpulses: %s\n" % e)
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

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcAfterpulses |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tpc_afterpulse_item**
> patch_tpc_afterpulse_item(tpcafterpulse_id, tpc_afterpulse, if_match=if_match)

Updates a TpcAfterpulse document

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcAfterpulseApi(api_client)
    tpcafterpulse_id = 'tpcafterpulse_id_example' # str | 
tpc_afterpulse = xepmts.TpcAfterpulse() # TpcAfterpulse | A TpcAfterpulse or list of TpcAfterpulse documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a TpcAfterpulse document
        api_instance.patch_tpc_afterpulse_item(tpcafterpulse_id, tpc_afterpulse, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcAfterpulseApi->patch_tpc_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcafterpulse_id** | **str**|  | 
 **tpc_afterpulse** | [**TpcAfterpulse**](TpcAfterpulse.md)| A TpcAfterpulse or list of TpcAfterpulse documents | 
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
**200** | TpcAfterpulse document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_afterpulses**
> post_tpc_afterpulses(tpc_afterpulse)

Stores one or more TpcAfterpulses.

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcAfterpulseApi(api_client)
    tpc_afterpulse = xepmts.TpcAfterpulse() # TpcAfterpulse | A TpcAfterpulse or list of TpcAfterpulse documents

    try:
        # Stores one or more TpcAfterpulses.
        api_instance.post_tpc_afterpulses(tpc_afterpulse)
    except ApiException as e:
        print("Exception when calling TpcAfterpulseApi->post_tpc_afterpulses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_afterpulse** | [**TpcAfterpulse**](TpcAfterpulse.md)| A TpcAfterpulse or list of TpcAfterpulse documents | 

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

# **put_tpc_afterpulse_item**
> put_tpc_afterpulse_item(tpcafterpulse_id, tpc_afterpulse, if_match=if_match)

Replaces a TpcAfterpulse document

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcAfterpulseApi(api_client)
    tpcafterpulse_id = 'tpcafterpulse_id_example' # str | 
tpc_afterpulse = xepmts.TpcAfterpulse() # TpcAfterpulse | A TpcAfterpulse or list of TpcAfterpulse documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcAfterpulse document
        api_instance.put_tpc_afterpulse_item(tpcafterpulse_id, tpc_afterpulse, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcAfterpulseApi->put_tpc_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcafterpulse_id** | **str**|  | 
 **tpc_afterpulse** | [**TpcAfterpulse**](TpcAfterpulse.md)| A TpcAfterpulse or list of TpcAfterpulse documents | 
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
**200** | TpcAfterpulse document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

