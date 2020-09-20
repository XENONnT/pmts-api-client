# xepmts.NvetoDarkCountRateApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_dark_count_rate_item**](NvetoDarkCountRateApi.md#delete_nveto_dark_count_rate_item) | **DELETE** /nveto/dark_counts_rates/{nvetodarkcountrateId} | Deletes a NvetoDarkCountRate document
[**get_nveto_dark_count_rate_item**](NvetoDarkCountRateApi.md#get_nveto_dark_count_rate_item) | **GET** /nveto/dark_counts_rates/{nvetodarkcountrateId} | Retrieves a NvetoDarkCountRate document
[**get_nveto_dark_count_rates**](NvetoDarkCountRateApi.md#get_nveto_dark_count_rates) | **GET** /nveto/dark_counts_rates | Retrieves one or more NvetoDarkCountRates
[**post_nveto_dark_count_rates**](NvetoDarkCountRateApi.md#post_nveto_dark_count_rates) | **POST** /nveto/dark_counts_rates | Stores one or more NvetoDarkCountRates.
[**put_nveto_dark_count_rate_item**](NvetoDarkCountRateApi.md#put_nveto_dark_count_rate_item) | **PUT** /nveto/dark_counts_rates/{nvetodarkcountrateId} | Replaces a NvetoDarkCountRate document


# **delete_nveto_dark_count_rate_item**
> delete_nveto_dark_count_rate_item(nvetodarkcountrate_id, if_match=if_match)

Deletes a NvetoDarkCountRate document

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
    api_instance = xepmts.NvetoDarkCountRateApi(api_client)
    nvetodarkcountrate_id = 'nvetodarkcountrate_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoDarkCountRate document
        api_instance.delete_nveto_dark_count_rate_item(nvetodarkcountrate_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoDarkCountRateApi->delete_nveto_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetodarkcountrate_id** | **str**|  | 
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
**204** | NvetoDarkCountRate document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_dark_count_rate_item**
> NvetoDarkCountRate get_nveto_dark_count_rate_item(nvetodarkcountrate_id)

Retrieves a NvetoDarkCountRate document

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
    api_instance = xepmts.NvetoDarkCountRateApi(api_client)
    nvetodarkcountrate_id = 'nvetodarkcountrate_id_example' # str | 

    try:
        # Retrieves a NvetoDarkCountRate document
        api_response = api_instance.get_nveto_dark_count_rate_item(nvetodarkcountrate_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoDarkCountRateApi->get_nveto_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetodarkcountrate_id** | **str**|  | 

### Return type

[**NvetoDarkCountRate**](NvetoDarkCountRate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoDarkCountRate document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_dark_count_rates**
> InlineResponse20014 get_nveto_dark_count_rates(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoDarkCountRates

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
    api_instance = xepmts.NvetoDarkCountRateApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoDarkCountRates
        api_response = api_instance.get_nveto_dark_count_rates(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoDarkCountRateApi->get_nveto_dark_count_rates: %s\n" % e)
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

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of NvetoDarkCountRates |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_dark_count_rates**
> post_nveto_dark_count_rates(nveto_dark_count_rate)

Stores one or more NvetoDarkCountRates.

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
    api_instance = xepmts.NvetoDarkCountRateApi(api_client)
    nveto_dark_count_rate = xepmts.NvetoDarkCountRate() # NvetoDarkCountRate | A NvetoDarkCountRate or list of NvetoDarkCountRate documents

    try:
        # Stores one or more NvetoDarkCountRates.
        api_instance.post_nveto_dark_count_rates(nveto_dark_count_rate)
    except ApiException as e:
        print("Exception when calling NvetoDarkCountRateApi->post_nveto_dark_count_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_dark_count_rate** | [**NvetoDarkCountRate**](NvetoDarkCountRate.md)| A NvetoDarkCountRate or list of NvetoDarkCountRate documents | 

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

# **put_nveto_dark_count_rate_item**
> put_nveto_dark_count_rate_item(nvetodarkcountrate_id, nveto_dark_count_rate, if_match=if_match)

Replaces a NvetoDarkCountRate document

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
    api_instance = xepmts.NvetoDarkCountRateApi(api_client)
    nvetodarkcountrate_id = 'nvetodarkcountrate_id_example' # str | 
nveto_dark_count_rate = xepmts.NvetoDarkCountRate() # NvetoDarkCountRate | A NvetoDarkCountRate or list of NvetoDarkCountRate documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoDarkCountRate document
        api_instance.put_nveto_dark_count_rate_item(nvetodarkcountrate_id, nveto_dark_count_rate, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoDarkCountRateApi->put_nveto_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetodarkcountrate_id** | **str**|  | 
 **nveto_dark_count_rate** | [**NvetoDarkCountRate**](NvetoDarkCountRate.md)| A NvetoDarkCountRate or list of NvetoDarkCountRate documents | 
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
**200** | NvetoDarkCountRate document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

