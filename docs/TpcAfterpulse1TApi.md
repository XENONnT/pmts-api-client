# xepmts.TpcAfterpulse1TApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_afterpulse1_t_item**](TpcAfterpulse1TApi.md#delete_tpc_afterpulse1_t_item) | **DELETE** /xenon1t/tpc/afterpules/{tpcafterpulse1tId} | Deletes a TpcAfterpulse1T document
[**get_tpc_afterpulse1_t_item**](TpcAfterpulse1TApi.md#get_tpc_afterpulse1_t_item) | **GET** /xenon1t/tpc/afterpules/{tpcafterpulse1tId} | Retrieves a TpcAfterpulse1T document
[**get_tpc_afterpulses1_t**](TpcAfterpulse1TApi.md#get_tpc_afterpulses1_t) | **GET** /xenon1t/tpc/afterpules | Retrieves one or more TpcAfterpulses1T
[**post_tpc_afterpulses1_t**](TpcAfterpulse1TApi.md#post_tpc_afterpulses1_t) | **POST** /xenon1t/tpc/afterpules | Stores one or more TpcAfterpulses1T.
[**put_tpc_afterpulse1_t_item**](TpcAfterpulse1TApi.md#put_tpc_afterpulse1_t_item) | **PUT** /xenon1t/tpc/afterpules/{tpcafterpulse1tId} | Replaces a TpcAfterpulse1T document


# **delete_tpc_afterpulse1_t_item**
> delete_tpc_afterpulse1_t_item(tpcafterpulse1t_id, if_match=if_match)

Deletes a TpcAfterpulse1T document

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
    api_instance = xepmts.TpcAfterpulse1TApi(api_client)
    tpcafterpulse1t_id = 'tpcafterpulse1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcAfterpulse1T document
        api_instance.delete_tpc_afterpulse1_t_item(tpcafterpulse1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcAfterpulse1TApi->delete_tpc_afterpulse1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcafterpulse1t_id** | **str**|  | 
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
**204** | TpcAfterpulse1T document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_afterpulse1_t_item**
> TpcAfterpulse1T get_tpc_afterpulse1_t_item(tpcafterpulse1t_id)

Retrieves a TpcAfterpulse1T document

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
    api_instance = xepmts.TpcAfterpulse1TApi(api_client)
    tpcafterpulse1t_id = 'tpcafterpulse1t_id_example' # str | 

    try:
        # Retrieves a TpcAfterpulse1T document
        api_response = api_instance.get_tpc_afterpulse1_t_item(tpcafterpulse1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcAfterpulse1TApi->get_tpc_afterpulse1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcafterpulse1t_id** | **str**|  | 

### Return type

[**TpcAfterpulse1T**](TpcAfterpulse1T.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcAfterpulse1T document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_afterpulses1_t**
> InlineResponse20043 get_tpc_afterpulses1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcAfterpulses1T

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
    api_instance = xepmts.TpcAfterpulse1TApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcAfterpulses1T
        api_response = api_instance.get_tpc_afterpulses1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcAfterpulse1TApi->get_tpc_afterpulses1_t: %s\n" % e)
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

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcAfterpulses1T |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_afterpulses1_t**
> post_tpc_afterpulses1_t(tpc_afterpulse1_t)

Stores one or more TpcAfterpulses1T.

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
    api_instance = xepmts.TpcAfterpulse1TApi(api_client)
    tpc_afterpulse1_t = xepmts.TpcAfterpulse1T() # TpcAfterpulse1T | A TpcAfterpulse1T or list of TpcAfterpulse1T documents

    try:
        # Stores one or more TpcAfterpulses1T.
        api_instance.post_tpc_afterpulses1_t(tpc_afterpulse1_t)
    except ApiException as e:
        print("Exception when calling TpcAfterpulse1TApi->post_tpc_afterpulses1_t: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_afterpulse1_t** | [**TpcAfterpulse1T**](TpcAfterpulse1T.md)| A TpcAfterpulse1T or list of TpcAfterpulse1T documents | 

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

# **put_tpc_afterpulse1_t_item**
> put_tpc_afterpulse1_t_item(tpcafterpulse1t_id, tpc_afterpulse1_t, if_match=if_match)

Replaces a TpcAfterpulse1T document

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
    api_instance = xepmts.TpcAfterpulse1TApi(api_client)
    tpcafterpulse1t_id = 'tpcafterpulse1t_id_example' # str | 
tpc_afterpulse1_t = xepmts.TpcAfterpulse1T() # TpcAfterpulse1T | A TpcAfterpulse1T or list of TpcAfterpulse1T documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcAfterpulse1T document
        api_instance.put_tpc_afterpulse1_t_item(tpcafterpulse1t_id, tpc_afterpulse1_t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcAfterpulse1TApi->put_tpc_afterpulse1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcafterpulse1t_id** | **str**|  | 
 **tpc_afterpulse1_t** | [**TpcAfterpulse1T**](TpcAfterpulse1T.md)| A TpcAfterpulse1T or list of TpcAfterpulse1T documents | 
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
**200** | TpcAfterpulse1T document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

