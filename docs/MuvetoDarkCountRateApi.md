# xepmts.MuvetoDarkCountRateApi

All URIs are relative to *https://xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_dark_count_rate_item**](MuvetoDarkCountRateApi.md#delete_muveto_dark_count_rate_item) | **DELETE** /muveto/dark_counts_rates/{muvetodarkcountrateId} | Deletes a MuvetoDarkCountRate document
[**get_muveto_dark_count_rate_item**](MuvetoDarkCountRateApi.md#get_muveto_dark_count_rate_item) | **GET** /muveto/dark_counts_rates/{muvetodarkcountrateId} | Retrieves a MuvetoDarkCountRate document
[**get_muveto_dark_count_rates**](MuvetoDarkCountRateApi.md#get_muveto_dark_count_rates) | **GET** /muveto/dark_counts_rates | Retrieves one or more MuvetoDarkCountRates
[**patch_muveto_dark_count_rate_item**](MuvetoDarkCountRateApi.md#patch_muveto_dark_count_rate_item) | **PATCH** /muveto/dark_counts_rates/{muvetodarkcountrateId} | Updates a MuvetoDarkCountRate document
[**post_muveto_dark_count_rates**](MuvetoDarkCountRateApi.md#post_muveto_dark_count_rates) | **POST** /muveto/dark_counts_rates | Stores one or more MuvetoDarkCountRates.
[**put_muveto_dark_count_rate_item**](MuvetoDarkCountRateApi.md#put_muveto_dark_count_rate_item) | **PUT** /muveto/dark_counts_rates/{muvetodarkcountrateId} | Replaces a MuvetoDarkCountRate document


# **delete_muveto_dark_count_rate_item**
> delete_muveto_dark_count_rate_item(muvetodarkcountrate_id, if_match=if_match)

Deletes a MuvetoDarkCountRate document

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
    api_instance = xepmts.MuvetoDarkCountRateApi(api_client)
    muvetodarkcountrate_id = 'muvetodarkcountrate_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoDarkCountRate document
        api_instance.delete_muveto_dark_count_rate_item(muvetodarkcountrate_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRateApi->delete_muveto_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetodarkcountrate_id** | **str**|  | 
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
**204** | MuvetoDarkCountRate document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_dark_count_rate_item**
> MuvetoDarkCountRate get_muveto_dark_count_rate_item(muvetodarkcountrate_id)

Retrieves a MuvetoDarkCountRate document

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
    api_instance = xepmts.MuvetoDarkCountRateApi(api_client)
    muvetodarkcountrate_id = 'muvetodarkcountrate_id_example' # str | 

    try:
        # Retrieves a MuvetoDarkCountRate document
        api_response = api_instance.get_muveto_dark_count_rate_item(muvetodarkcountrate_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRateApi->get_muveto_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetodarkcountrate_id** | **str**|  | 

### Return type

[**MuvetoDarkCountRate**](MuvetoDarkCountRate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoDarkCountRate document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_dark_count_rates**
> InlineResponse20026 get_muveto_dark_count_rates(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoDarkCountRates

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
    api_instance = xepmts.MuvetoDarkCountRateApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoDarkCountRates
        api_response = api_instance.get_muveto_dark_count_rates(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRateApi->get_muveto_dark_count_rates: %s\n" % e)
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

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoDarkCountRates |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_muveto_dark_count_rate_item**
> patch_muveto_dark_count_rate_item(muvetodarkcountrate_id, muveto_dark_count_rate, if_match=if_match)

Updates a MuvetoDarkCountRate document

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
    api_instance = xepmts.MuvetoDarkCountRateApi(api_client)
    muvetodarkcountrate_id = 'muvetodarkcountrate_id_example' # str | 
muveto_dark_count_rate = xepmts.MuvetoDarkCountRate() # MuvetoDarkCountRate | A MuvetoDarkCountRate or list of MuvetoDarkCountRate documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a MuvetoDarkCountRate document
        api_instance.patch_muveto_dark_count_rate_item(muvetodarkcountrate_id, muveto_dark_count_rate, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRateApi->patch_muveto_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetodarkcountrate_id** | **str**|  | 
 **muveto_dark_count_rate** | [**MuvetoDarkCountRate**](MuvetoDarkCountRate.md)| A MuvetoDarkCountRate or list of MuvetoDarkCountRate documents | 
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
**200** | MuvetoDarkCountRate document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_dark_count_rates**
> post_muveto_dark_count_rates(muveto_dark_count_rate)

Stores one or more MuvetoDarkCountRates.

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
    api_instance = xepmts.MuvetoDarkCountRateApi(api_client)
    muveto_dark_count_rate = xepmts.MuvetoDarkCountRate() # MuvetoDarkCountRate | A MuvetoDarkCountRate or list of MuvetoDarkCountRate documents

    try:
        # Stores one or more MuvetoDarkCountRates.
        api_instance.post_muveto_dark_count_rates(muveto_dark_count_rate)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRateApi->post_muveto_dark_count_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_dark_count_rate** | [**MuvetoDarkCountRate**](MuvetoDarkCountRate.md)| A MuvetoDarkCountRate or list of MuvetoDarkCountRate documents | 

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

# **put_muveto_dark_count_rate_item**
> put_muveto_dark_count_rate_item(muvetodarkcountrate_id, muveto_dark_count_rate, if_match=if_match)

Replaces a MuvetoDarkCountRate document

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
    api_instance = xepmts.MuvetoDarkCountRateApi(api_client)
    muvetodarkcountrate_id = 'muvetodarkcountrate_id_example' # str | 
muveto_dark_count_rate = xepmts.MuvetoDarkCountRate() # MuvetoDarkCountRate | A MuvetoDarkCountRate or list of MuvetoDarkCountRate documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoDarkCountRate document
        api_instance.put_muveto_dark_count_rate_item(muvetodarkcountrate_id, muveto_dark_count_rate, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRateApi->put_muveto_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetodarkcountrate_id** | **str**|  | 
 **muveto_dark_count_rate** | [**MuvetoDarkCountRate**](MuvetoDarkCountRate.md)| A MuvetoDarkCountRate or list of MuvetoDarkCountRate documents | 
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
**200** | MuvetoDarkCountRate document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

