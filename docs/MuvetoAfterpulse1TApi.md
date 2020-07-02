# xepmts.MuvetoAfterpulse1TApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_afterpulse1_t_item**](MuvetoAfterpulse1TApi.md#delete_muveto_afterpulse1_t_item) | **DELETE** /xenon1t/muveto/afterpules/{muvetoafterpulse1tId} | Deletes a MuvetoAfterpulse1T document
[**get_muveto_afterpulse1_t_item**](MuvetoAfterpulse1TApi.md#get_muveto_afterpulse1_t_item) | **GET** /xenon1t/muveto/afterpules/{muvetoafterpulse1tId} | Retrieves a MuvetoAfterpulse1T document
[**get_muveto_afterpulses1_t**](MuvetoAfterpulse1TApi.md#get_muveto_afterpulses1_t) | **GET** /xenon1t/muveto/afterpules | Retrieves one or more MuvetoAfterpulses1T
[**post_muveto_afterpulses1_t**](MuvetoAfterpulse1TApi.md#post_muveto_afterpulses1_t) | **POST** /xenon1t/muveto/afterpules | Stores one or more MuvetoAfterpulses1T.
[**put_muveto_afterpulse1_t_item**](MuvetoAfterpulse1TApi.md#put_muveto_afterpulse1_t_item) | **PUT** /xenon1t/muveto/afterpules/{muvetoafterpulse1tId} | Replaces a MuvetoAfterpulse1T document


# **delete_muveto_afterpulse1_t_item**
> delete_muveto_afterpulse1_t_item(muvetoafterpulse1t_id, if_match=if_match)

Deletes a MuvetoAfterpulse1T document

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
    api_instance = xepmts.MuvetoAfterpulse1TApi(api_client)
    muvetoafterpulse1t_id = 'muvetoafterpulse1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoAfterpulse1T document
        api_instance.delete_muveto_afterpulse1_t_item(muvetoafterpulse1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1TApi->delete_muveto_afterpulse1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoafterpulse1t_id** | **str**|  | 
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
**204** | MuvetoAfterpulse1T document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_afterpulse1_t_item**
> MuvetoAfterpulse1T get_muveto_afterpulse1_t_item(muvetoafterpulse1t_id)

Retrieves a MuvetoAfterpulse1T document

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
    api_instance = xepmts.MuvetoAfterpulse1TApi(api_client)
    muvetoafterpulse1t_id = 'muvetoafterpulse1t_id_example' # str | 

    try:
        # Retrieves a MuvetoAfterpulse1T document
        api_response = api_instance.get_muveto_afterpulse1_t_item(muvetoafterpulse1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1TApi->get_muveto_afterpulse1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoafterpulse1t_id** | **str**|  | 

### Return type

[**MuvetoAfterpulse1T**](MuvetoAfterpulse1T.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoAfterpulse1T document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_afterpulses1_t**
> InlineResponse20055 get_muveto_afterpulses1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoAfterpulses1T

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
    api_instance = xepmts.MuvetoAfterpulse1TApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoAfterpulses1T
        api_response = api_instance.get_muveto_afterpulses1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1TApi->get_muveto_afterpulses1_t: %s\n" % e)
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

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoAfterpulses1T |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_afterpulses1_t**
> post_muveto_afterpulses1_t(muveto_afterpulse1_t)

Stores one or more MuvetoAfterpulses1T.

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
    api_instance = xepmts.MuvetoAfterpulse1TApi(api_client)
    muveto_afterpulse1_t = xepmts.MuvetoAfterpulse1T() # MuvetoAfterpulse1T | A MuvetoAfterpulse1T or list of MuvetoAfterpulse1T documents

    try:
        # Stores one or more MuvetoAfterpulses1T.
        api_instance.post_muveto_afterpulses1_t(muveto_afterpulse1_t)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1TApi->post_muveto_afterpulses1_t: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_afterpulse1_t** | [**MuvetoAfterpulse1T**](MuvetoAfterpulse1T.md)| A MuvetoAfterpulse1T or list of MuvetoAfterpulse1T documents | 

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

# **put_muveto_afterpulse1_t_item**
> put_muveto_afterpulse1_t_item(muvetoafterpulse1t_id, muveto_afterpulse1_t, if_match=if_match)

Replaces a MuvetoAfterpulse1T document

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
    api_instance = xepmts.MuvetoAfterpulse1TApi(api_client)
    muvetoafterpulse1t_id = 'muvetoafterpulse1t_id_example' # str | 
muveto_afterpulse1_t = xepmts.MuvetoAfterpulse1T() # MuvetoAfterpulse1T | A MuvetoAfterpulse1T or list of MuvetoAfterpulse1T documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoAfterpulse1T document
        api_instance.put_muveto_afterpulse1_t_item(muvetoafterpulse1t_id, muveto_afterpulse1_t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1TApi->put_muveto_afterpulse1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoafterpulse1t_id** | **str**|  | 
 **muveto_afterpulse1_t** | [**MuvetoAfterpulse1T**](MuvetoAfterpulse1T.md)| A MuvetoAfterpulse1T or list of MuvetoAfterpulse1T documents | 
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
**200** | MuvetoAfterpulse1T document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

