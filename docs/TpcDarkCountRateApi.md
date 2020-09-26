# xepmts.TpcDarkCountRateApi

All URIs are relative to *https://xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_dark_count_rate_item**](TpcDarkCountRateApi.md#delete_tpc_dark_count_rate_item) | **DELETE** /tpc/dark_counts_rates/{tpcdarkcountrateId} | Deletes a TpcDarkCountRate document
[**get_tpc_dark_count_rate_item**](TpcDarkCountRateApi.md#get_tpc_dark_count_rate_item) | **GET** /tpc/dark_counts_rates/{tpcdarkcountrateId} | Retrieves a TpcDarkCountRate document
[**get_tpc_dark_count_rates**](TpcDarkCountRateApi.md#get_tpc_dark_count_rates) | **GET** /tpc/dark_counts_rates | Retrieves one or more TpcDarkCountRates
[**patch_tpc_dark_count_rate_item**](TpcDarkCountRateApi.md#patch_tpc_dark_count_rate_item) | **PATCH** /tpc/dark_counts_rates/{tpcdarkcountrateId} | Updates a TpcDarkCountRate document
[**post_tpc_dark_count_rates**](TpcDarkCountRateApi.md#post_tpc_dark_count_rates) | **POST** /tpc/dark_counts_rates | Stores one or more TpcDarkCountRates.
[**put_tpc_dark_count_rate_item**](TpcDarkCountRateApi.md#put_tpc_dark_count_rate_item) | **PUT** /tpc/dark_counts_rates/{tpcdarkcountrateId} | Replaces a TpcDarkCountRate document


# **delete_tpc_dark_count_rate_item**
> delete_tpc_dark_count_rate_item(tpcdarkcountrate_id, if_match=if_match)

Deletes a TpcDarkCountRate document

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
    api_instance = xepmts.TpcDarkCountRateApi(api_client)
    tpcdarkcountrate_id = 'tpcdarkcountrate_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcDarkCountRate document
        api_instance.delete_tpc_dark_count_rate_item(tpcdarkcountrate_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcDarkCountRateApi->delete_tpc_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcdarkcountrate_id** | **str**|  | 
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
**204** | TpcDarkCountRate document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_dark_count_rate_item**
> TpcDarkCountRate get_tpc_dark_count_rate_item(tpcdarkcountrate_id)

Retrieves a TpcDarkCountRate document

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
    api_instance = xepmts.TpcDarkCountRateApi(api_client)
    tpcdarkcountrate_id = 'tpcdarkcountrate_id_example' # str | 

    try:
        # Retrieves a TpcDarkCountRate document
        api_response = api_instance.get_tpc_dark_count_rate_item(tpcdarkcountrate_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcDarkCountRateApi->get_tpc_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcdarkcountrate_id** | **str**|  | 

### Return type

[**TpcDarkCountRate**](TpcDarkCountRate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcDarkCountRate document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_dark_count_rates**
> InlineResponse2003 get_tpc_dark_count_rates(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcDarkCountRates

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
    api_instance = xepmts.TpcDarkCountRateApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcDarkCountRates
        api_response = api_instance.get_tpc_dark_count_rates(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcDarkCountRateApi->get_tpc_dark_count_rates: %s\n" % e)
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

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcDarkCountRates |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tpc_dark_count_rate_item**
> patch_tpc_dark_count_rate_item(tpcdarkcountrate_id, tpc_dark_count_rate, if_match=if_match)

Updates a TpcDarkCountRate document

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
    api_instance = xepmts.TpcDarkCountRateApi(api_client)
    tpcdarkcountrate_id = 'tpcdarkcountrate_id_example' # str | 
tpc_dark_count_rate = xepmts.TpcDarkCountRate() # TpcDarkCountRate | A TpcDarkCountRate or list of TpcDarkCountRate documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a TpcDarkCountRate document
        api_instance.patch_tpc_dark_count_rate_item(tpcdarkcountrate_id, tpc_dark_count_rate, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcDarkCountRateApi->patch_tpc_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcdarkcountrate_id** | **str**|  | 
 **tpc_dark_count_rate** | [**TpcDarkCountRate**](TpcDarkCountRate.md)| A TpcDarkCountRate or list of TpcDarkCountRate documents | 
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
**200** | TpcDarkCountRate document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_dark_count_rates**
> post_tpc_dark_count_rates(tpc_dark_count_rate)

Stores one or more TpcDarkCountRates.

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
    api_instance = xepmts.TpcDarkCountRateApi(api_client)
    tpc_dark_count_rate = xepmts.TpcDarkCountRate() # TpcDarkCountRate | A TpcDarkCountRate or list of TpcDarkCountRate documents

    try:
        # Stores one or more TpcDarkCountRates.
        api_instance.post_tpc_dark_count_rates(tpc_dark_count_rate)
    except ApiException as e:
        print("Exception when calling TpcDarkCountRateApi->post_tpc_dark_count_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_dark_count_rate** | [**TpcDarkCountRate**](TpcDarkCountRate.md)| A TpcDarkCountRate or list of TpcDarkCountRate documents | 

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

# **put_tpc_dark_count_rate_item**
> put_tpc_dark_count_rate_item(tpcdarkcountrate_id, tpc_dark_count_rate, if_match=if_match)

Replaces a TpcDarkCountRate document

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
    api_instance = xepmts.TpcDarkCountRateApi(api_client)
    tpcdarkcountrate_id = 'tpcdarkcountrate_id_example' # str | 
tpc_dark_count_rate = xepmts.TpcDarkCountRate() # TpcDarkCountRate | A TpcDarkCountRate or list of TpcDarkCountRate documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcDarkCountRate document
        api_instance.put_tpc_dark_count_rate_item(tpcdarkcountrate_id, tpc_dark_count_rate, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcDarkCountRateApi->put_tpc_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcdarkcountrate_id** | **str**|  | 
 **tpc_dark_count_rate** | [**TpcDarkCountRate**](TpcDarkCountRate.md)| A TpcDarkCountRate or list of TpcDarkCountRate documents | 
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
**200** | TpcDarkCountRate document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

