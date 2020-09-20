# xepmts.TpcAfterpulse1tApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_afterpulse1t_item**](TpcAfterpulse1tApi.md#delete_tpc_afterpulse1t_item) | **DELETE** /xenon1t/tpc/afterpules/{tpcafterpulse1tId} | Deletes a TpcAfterpulse1t document
[**get_tpc_afterpulse1t_item**](TpcAfterpulse1tApi.md#get_tpc_afterpulse1t_item) | **GET** /xenon1t/tpc/afterpules/{tpcafterpulse1tId} | Retrieves a TpcAfterpulse1t document
[**get_tpc_afterpulse1ts**](TpcAfterpulse1tApi.md#get_tpc_afterpulse1ts) | **GET** /xenon1t/tpc/afterpules | Retrieves one or more TpcAfterpulse1ts
[**post_tpc_afterpulse1ts**](TpcAfterpulse1tApi.md#post_tpc_afterpulse1ts) | **POST** /xenon1t/tpc/afterpules | Stores one or more TpcAfterpulse1ts.
[**put_tpc_afterpulse1t_item**](TpcAfterpulse1tApi.md#put_tpc_afterpulse1t_item) | **PUT** /xenon1t/tpc/afterpules/{tpcafterpulse1tId} | Replaces a TpcAfterpulse1t document


# **delete_tpc_afterpulse1t_item**
> delete_tpc_afterpulse1t_item(tpcafterpulse1t_id, if_match=if_match)

Deletes a TpcAfterpulse1t document

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
    api_instance = xepmts.TpcAfterpulse1tApi(api_client)
    tpcafterpulse1t_id = 'tpcafterpulse1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcAfterpulse1t document
        api_instance.delete_tpc_afterpulse1t_item(tpcafterpulse1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcAfterpulse1tApi->delete_tpc_afterpulse1t_item: %s\n" % e)
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
**204** | TpcAfterpulse1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_afterpulse1t_item**
> TpcAfterpulse1t get_tpc_afterpulse1t_item(tpcafterpulse1t_id)

Retrieves a TpcAfterpulse1t document

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
    api_instance = xepmts.TpcAfterpulse1tApi(api_client)
    tpcafterpulse1t_id = 'tpcafterpulse1t_id_example' # str | 

    try:
        # Retrieves a TpcAfterpulse1t document
        api_response = api_instance.get_tpc_afterpulse1t_item(tpcafterpulse1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcAfterpulse1tApi->get_tpc_afterpulse1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcafterpulse1t_id** | **str**|  | 

### Return type

[**TpcAfterpulse1t**](TpcAfterpulse1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcAfterpulse1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_afterpulse1ts**
> InlineResponse20045 get_tpc_afterpulse1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcAfterpulse1ts

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
    api_instance = xepmts.TpcAfterpulse1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcAfterpulse1ts
        api_response = api_instance.get_tpc_afterpulse1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcAfterpulse1tApi->get_tpc_afterpulse1ts: %s\n" % e)
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

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcAfterpulse1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_afterpulse1ts**
> post_tpc_afterpulse1ts(tpc_afterpulse1t)

Stores one or more TpcAfterpulse1ts.

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
    api_instance = xepmts.TpcAfterpulse1tApi(api_client)
    tpc_afterpulse1t = xepmts.TpcAfterpulse1t() # TpcAfterpulse1t | A TpcAfterpulse1t or list of TpcAfterpulse1t documents

    try:
        # Stores one or more TpcAfterpulse1ts.
        api_instance.post_tpc_afterpulse1ts(tpc_afterpulse1t)
    except ApiException as e:
        print("Exception when calling TpcAfterpulse1tApi->post_tpc_afterpulse1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_afterpulse1t** | [**TpcAfterpulse1t**](TpcAfterpulse1t.md)| A TpcAfterpulse1t or list of TpcAfterpulse1t documents | 

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

# **put_tpc_afterpulse1t_item**
> put_tpc_afterpulse1t_item(tpcafterpulse1t_id, tpc_afterpulse1t, if_match=if_match)

Replaces a TpcAfterpulse1t document

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
    api_instance = xepmts.TpcAfterpulse1tApi(api_client)
    tpcafterpulse1t_id = 'tpcafterpulse1t_id_example' # str | 
tpc_afterpulse1t = xepmts.TpcAfterpulse1t() # TpcAfterpulse1t | A TpcAfterpulse1t or list of TpcAfterpulse1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcAfterpulse1t document
        api_instance.put_tpc_afterpulse1t_item(tpcafterpulse1t_id, tpc_afterpulse1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcAfterpulse1tApi->put_tpc_afterpulse1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcafterpulse1t_id** | **str**|  | 
 **tpc_afterpulse1t** | [**TpcAfterpulse1t**](TpcAfterpulse1t.md)| A TpcAfterpulse1t or list of TpcAfterpulse1t documents | 
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
**200** | TpcAfterpulse1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

