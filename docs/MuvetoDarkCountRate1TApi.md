# xepmts.MuvetoDarkCountRate1TApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_dark_count_rate1_t_item**](MuvetoDarkCountRate1TApi.md#delete_muveto_dark_count_rate1_t_item) | **DELETE** /xenon1t/muveto/dark_counts_rates/{muvetodarkcountrate1tId} | Deletes a MuvetoDarkCountRate1T document
[**get_muveto_dark_count_rate1_t_item**](MuvetoDarkCountRate1TApi.md#get_muveto_dark_count_rate1_t_item) | **GET** /xenon1t/muveto/dark_counts_rates/{muvetodarkcountrate1tId} | Retrieves a MuvetoDarkCountRate1T document
[**get_muveto_dark_count_rates1_t**](MuvetoDarkCountRate1TApi.md#get_muveto_dark_count_rates1_t) | **GET** /xenon1t/muveto/dark_counts_rates | Retrieves one or more MuvetoDarkCountRates1T
[**post_muveto_dark_count_rates1_t**](MuvetoDarkCountRate1TApi.md#post_muveto_dark_count_rates1_t) | **POST** /xenon1t/muveto/dark_counts_rates | Stores one or more MuvetoDarkCountRates1T.
[**put_muveto_dark_count_rate1_t_item**](MuvetoDarkCountRate1TApi.md#put_muveto_dark_count_rate1_t_item) | **PUT** /xenon1t/muveto/dark_counts_rates/{muvetodarkcountrate1tId} | Replaces a MuvetoDarkCountRate1T document


# **delete_muveto_dark_count_rate1_t_item**
> delete_muveto_dark_count_rate1_t_item(muvetodarkcountrate1t_id, if_match=if_match)

Deletes a MuvetoDarkCountRate1T document

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
    api_instance = xepmts.MuvetoDarkCountRate1TApi(api_client)
    muvetodarkcountrate1t_id = 'muvetodarkcountrate1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoDarkCountRate1T document
        api_instance.delete_muveto_dark_count_rate1_t_item(muvetodarkcountrate1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRate1TApi->delete_muveto_dark_count_rate1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetodarkcountrate1t_id** | **str**|  | 
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
**204** | MuvetoDarkCountRate1T document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_dark_count_rate1_t_item**
> MuvetoDarkCountRate1T get_muveto_dark_count_rate1_t_item(muvetodarkcountrate1t_id)

Retrieves a MuvetoDarkCountRate1T document

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
    api_instance = xepmts.MuvetoDarkCountRate1TApi(api_client)
    muvetodarkcountrate1t_id = 'muvetodarkcountrate1t_id_example' # str | 

    try:
        # Retrieves a MuvetoDarkCountRate1T document
        api_response = api_instance.get_muveto_dark_count_rate1_t_item(muvetodarkcountrate1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRate1TApi->get_muveto_dark_count_rate1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetodarkcountrate1t_id** | **str**|  | 

### Return type

[**MuvetoDarkCountRate1T**](MuvetoDarkCountRate1T.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoDarkCountRate1T document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_dark_count_rates1_t**
> InlineResponse20049 get_muveto_dark_count_rates1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoDarkCountRates1T

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
    api_instance = xepmts.MuvetoDarkCountRate1TApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoDarkCountRates1T
        api_response = api_instance.get_muveto_dark_count_rates1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRate1TApi->get_muveto_dark_count_rates1_t: %s\n" % e)
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

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoDarkCountRates1T |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_dark_count_rates1_t**
> post_muveto_dark_count_rates1_t(muveto_dark_count_rate1_t)

Stores one or more MuvetoDarkCountRates1T.

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
    api_instance = xepmts.MuvetoDarkCountRate1TApi(api_client)
    muveto_dark_count_rate1_t = xepmts.MuvetoDarkCountRate1T() # MuvetoDarkCountRate1T | A MuvetoDarkCountRate1T or list of MuvetoDarkCountRate1T documents

    try:
        # Stores one or more MuvetoDarkCountRates1T.
        api_instance.post_muveto_dark_count_rates1_t(muveto_dark_count_rate1_t)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRate1TApi->post_muveto_dark_count_rates1_t: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_dark_count_rate1_t** | [**MuvetoDarkCountRate1T**](MuvetoDarkCountRate1T.md)| A MuvetoDarkCountRate1T or list of MuvetoDarkCountRate1T documents | 

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

# **put_muveto_dark_count_rate1_t_item**
> put_muveto_dark_count_rate1_t_item(muvetodarkcountrate1t_id, muveto_dark_count_rate1_t, if_match=if_match)

Replaces a MuvetoDarkCountRate1T document

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
    api_instance = xepmts.MuvetoDarkCountRate1TApi(api_client)
    muvetodarkcountrate1t_id = 'muvetodarkcountrate1t_id_example' # str | 
muveto_dark_count_rate1_t = xepmts.MuvetoDarkCountRate1T() # MuvetoDarkCountRate1T | A MuvetoDarkCountRate1T or list of MuvetoDarkCountRate1T documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoDarkCountRate1T document
        api_instance.put_muveto_dark_count_rate1_t_item(muvetodarkcountrate1t_id, muveto_dark_count_rate1_t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoDarkCountRate1TApi->put_muveto_dark_count_rate1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetodarkcountrate1t_id** | **str**|  | 
 **muveto_dark_count_rate1_t** | [**MuvetoDarkCountRate1T**](MuvetoDarkCountRate1T.md)| A MuvetoDarkCountRate1T or list of MuvetoDarkCountRate1T documents | 
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
**200** | MuvetoDarkCountRate1T document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

