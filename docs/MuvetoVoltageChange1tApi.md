# xepmts.MuvetoVoltageChange1tApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_voltage_change1t_item**](MuvetoVoltageChange1tApi.md#delete_muveto_voltage_change1t_item) | **DELETE** /xenon1t/muveto/voltage_changes/{muvetovoltagechange1tId} | Deletes a MuvetoVoltageChange1t document
[**get_muveto_voltage_change1t_item**](MuvetoVoltageChange1tApi.md#get_muveto_voltage_change1t_item) | **GET** /xenon1t/muveto/voltage_changes/{muvetovoltagechange1tId} | Retrieves a MuvetoVoltageChange1t document
[**get_muveto_voltage_change1ts**](MuvetoVoltageChange1tApi.md#get_muveto_voltage_change1ts) | **GET** /xenon1t/muveto/voltage_changes | Retrieves one or more MuvetoVoltageChange1ts
[**post_muveto_voltage_change1ts**](MuvetoVoltageChange1tApi.md#post_muveto_voltage_change1ts) | **POST** /xenon1t/muveto/voltage_changes | Stores one or more MuvetoVoltageChange1ts.
[**put_muveto_voltage_change1t_item**](MuvetoVoltageChange1tApi.md#put_muveto_voltage_change1t_item) | **PUT** /xenon1t/muveto/voltage_changes/{muvetovoltagechange1tId} | Replaces a MuvetoVoltageChange1t document


# **delete_muveto_voltage_change1t_item**
> delete_muveto_voltage_change1t_item(muvetovoltagechange1t_id, if_match=if_match)

Deletes a MuvetoVoltageChange1t document

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
    api_instance = xepmts.MuvetoVoltageChange1tApi(api_client)
    muvetovoltagechange1t_id = 'muvetovoltagechange1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoVoltageChange1t document
        api_instance.delete_muveto_voltage_change1t_item(muvetovoltagechange1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChange1tApi->delete_muveto_voltage_change1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagechange1t_id** | **str**|  | 
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
**204** | MuvetoVoltageChange1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_voltage_change1t_item**
> MuvetoVoltageChange1t get_muveto_voltage_change1t_item(muvetovoltagechange1t_id)

Retrieves a MuvetoVoltageChange1t document

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
    api_instance = xepmts.MuvetoVoltageChange1tApi(api_client)
    muvetovoltagechange1t_id = 'muvetovoltagechange1t_id_example' # str | 

    try:
        # Retrieves a MuvetoVoltageChange1t document
        api_response = api_instance.get_muveto_voltage_change1t_item(muvetovoltagechange1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChange1tApi->get_muveto_voltage_change1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagechange1t_id** | **str**|  | 

### Return type

[**MuvetoVoltageChange1t**](MuvetoVoltageChange1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoVoltageChange1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_voltage_change1ts**
> InlineResponse20056 get_muveto_voltage_change1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoVoltageChange1ts

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
    api_instance = xepmts.MuvetoVoltageChange1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoVoltageChange1ts
        api_response = api_instance.get_muveto_voltage_change1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChange1tApi->get_muveto_voltage_change1ts: %s\n" % e)
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

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoVoltageChange1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_voltage_change1ts**
> post_muveto_voltage_change1ts(muveto_voltage_change1t)

Stores one or more MuvetoVoltageChange1ts.

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
    api_instance = xepmts.MuvetoVoltageChange1tApi(api_client)
    muveto_voltage_change1t = xepmts.MuvetoVoltageChange1t() # MuvetoVoltageChange1t | A MuvetoVoltageChange1t or list of MuvetoVoltageChange1t documents

    try:
        # Stores one or more MuvetoVoltageChange1ts.
        api_instance.post_muveto_voltage_change1ts(muveto_voltage_change1t)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChange1tApi->post_muveto_voltage_change1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_voltage_change1t** | [**MuvetoVoltageChange1t**](MuvetoVoltageChange1t.md)| A MuvetoVoltageChange1t or list of MuvetoVoltageChange1t documents | 

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

# **put_muveto_voltage_change1t_item**
> put_muveto_voltage_change1t_item(muvetovoltagechange1t_id, muveto_voltage_change1t, if_match=if_match)

Replaces a MuvetoVoltageChange1t document

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
    api_instance = xepmts.MuvetoVoltageChange1tApi(api_client)
    muvetovoltagechange1t_id = 'muvetovoltagechange1t_id_example' # str | 
muveto_voltage_change1t = xepmts.MuvetoVoltageChange1t() # MuvetoVoltageChange1t | A MuvetoVoltageChange1t or list of MuvetoVoltageChange1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoVoltageChange1t document
        api_instance.put_muveto_voltage_change1t_item(muvetovoltagechange1t_id, muveto_voltage_change1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChange1tApi->put_muveto_voltage_change1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagechange1t_id** | **str**|  | 
 **muveto_voltage_change1t** | [**MuvetoVoltageChange1t**](MuvetoVoltageChange1t.md)| A MuvetoVoltageChange1t or list of MuvetoVoltageChange1t documents | 
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
**200** | MuvetoVoltageChange1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

