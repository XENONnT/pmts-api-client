# xepmts.MuvetoCurrentChange1TApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_current_change1_t_item**](MuvetoCurrentChange1TApi.md#delete_muveto_current_change1_t_item) | **DELETE** /xenon1t/muveto/current_changes/{muvetocurrentchange1tId} | Deletes a MuvetoCurrentChange1T document
[**get_muveto_current_change1_t_item**](MuvetoCurrentChange1TApi.md#get_muveto_current_change1_t_item) | **GET** /xenon1t/muveto/current_changes/{muvetocurrentchange1tId} | Retrieves a MuvetoCurrentChange1T document
[**get_muveto_current_changes1_t**](MuvetoCurrentChange1TApi.md#get_muveto_current_changes1_t) | **GET** /xenon1t/muveto/current_changes | Retrieves one or more MuvetoCurrentChanges1T
[**post_muveto_current_changes1_t**](MuvetoCurrentChange1TApi.md#post_muveto_current_changes1_t) | **POST** /xenon1t/muveto/current_changes | Stores one or more MuvetoCurrentChanges1T.
[**put_muveto_current_change1_t_item**](MuvetoCurrentChange1TApi.md#put_muveto_current_change1_t_item) | **PUT** /xenon1t/muveto/current_changes/{muvetocurrentchange1tId} | Replaces a MuvetoCurrentChange1T document


# **delete_muveto_current_change1_t_item**
> delete_muveto_current_change1_t_item(muvetocurrentchange1t_id, if_match=if_match)

Deletes a MuvetoCurrentChange1T document

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
    api_instance = xepmts.MuvetoCurrentChange1TApi(api_client)
    muvetocurrentchange1t_id = 'muvetocurrentchange1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoCurrentChange1T document
        api_instance.delete_muveto_current_change1_t_item(muvetocurrentchange1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoCurrentChange1TApi->delete_muveto_current_change1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetocurrentchange1t_id** | **str**|  | 
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
**204** | MuvetoCurrentChange1T document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_current_change1_t_item**
> MuvetoCurrentChange1T get_muveto_current_change1_t_item(muvetocurrentchange1t_id)

Retrieves a MuvetoCurrentChange1T document

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
    api_instance = xepmts.MuvetoCurrentChange1TApi(api_client)
    muvetocurrentchange1t_id = 'muvetocurrentchange1t_id_example' # str | 

    try:
        # Retrieves a MuvetoCurrentChange1T document
        api_response = api_instance.get_muveto_current_change1_t_item(muvetocurrentchange1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoCurrentChange1TApi->get_muveto_current_change1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetocurrentchange1t_id** | **str**|  | 

### Return type

[**MuvetoCurrentChange1T**](MuvetoCurrentChange1T.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoCurrentChange1T document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_current_changes1_t**
> InlineResponse20053 get_muveto_current_changes1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoCurrentChanges1T

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
    api_instance = xepmts.MuvetoCurrentChange1TApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoCurrentChanges1T
        api_response = api_instance.get_muveto_current_changes1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoCurrentChange1TApi->get_muveto_current_changes1_t: %s\n" % e)
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

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoCurrentChanges1T |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_current_changes1_t**
> post_muveto_current_changes1_t(muveto_current_change1_t)

Stores one or more MuvetoCurrentChanges1T.

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
    api_instance = xepmts.MuvetoCurrentChange1TApi(api_client)
    muveto_current_change1_t = xepmts.MuvetoCurrentChange1T() # MuvetoCurrentChange1T | A MuvetoCurrentChange1T or list of MuvetoCurrentChange1T documents

    try:
        # Stores one or more MuvetoCurrentChanges1T.
        api_instance.post_muveto_current_changes1_t(muveto_current_change1_t)
    except ApiException as e:
        print("Exception when calling MuvetoCurrentChange1TApi->post_muveto_current_changes1_t: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_current_change1_t** | [**MuvetoCurrentChange1T**](MuvetoCurrentChange1T.md)| A MuvetoCurrentChange1T or list of MuvetoCurrentChange1T documents | 

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

# **put_muveto_current_change1_t_item**
> put_muveto_current_change1_t_item(muvetocurrentchange1t_id, muveto_current_change1_t, if_match=if_match)

Replaces a MuvetoCurrentChange1T document

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
    api_instance = xepmts.MuvetoCurrentChange1TApi(api_client)
    muvetocurrentchange1t_id = 'muvetocurrentchange1t_id_example' # str | 
muveto_current_change1_t = xepmts.MuvetoCurrentChange1T() # MuvetoCurrentChange1T | A MuvetoCurrentChange1T or list of MuvetoCurrentChange1T documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoCurrentChange1T document
        api_instance.put_muveto_current_change1_t_item(muvetocurrentchange1t_id, muveto_current_change1_t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoCurrentChange1TApi->put_muveto_current_change1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetocurrentchange1t_id** | **str**|  | 
 **muveto_current_change1_t** | [**MuvetoCurrentChange1T**](MuvetoCurrentChange1T.md)| A MuvetoCurrentChange1T or list of MuvetoCurrentChange1T documents | 
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
**200** | MuvetoCurrentChange1T document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

