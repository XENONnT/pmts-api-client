# xepmts.MuvetoVoltageMap1TApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_voltage_map1_t_item**](MuvetoVoltageMap1TApi.md#delete_muveto_voltage_map1_t_item) | **DELETE** /xenon1t/muveto/voltage_maps/{muvetovoltagemap1tId} | Deletes a MuvetoVoltageMap1T document
[**delete_muveto_voltage_maps1_t**](MuvetoVoltageMap1TApi.md#delete_muveto_voltage_maps1_t) | **DELETE** /xenon1t/muveto/voltage_maps | Deletes all MuvetoVoltageMaps1T
[**get_muveto_voltage_map1_t_item**](MuvetoVoltageMap1TApi.md#get_muveto_voltage_map1_t_item) | **GET** /xenon1t/muveto/voltage_maps/{muvetovoltagemap1tId} | Retrieves a MuvetoVoltageMap1T document
[**get_muveto_voltage_map1_t_item_by_name**](MuvetoVoltageMap1TApi.md#get_muveto_voltage_map1_t_item_by_name) | **GET** /xenon1t/muveto/voltage_maps/{Name} | Retrieves a MuvetoVoltageMap1T document by name
[**get_muveto_voltage_maps1_t**](MuvetoVoltageMap1TApi.md#get_muveto_voltage_maps1_t) | **GET** /xenon1t/muveto/voltage_maps | Retrieves one or more MuvetoVoltageMaps1T
[**post_muveto_voltage_maps1_t**](MuvetoVoltageMap1TApi.md#post_muveto_voltage_maps1_t) | **POST** /xenon1t/muveto/voltage_maps | Stores one or more MuvetoVoltageMaps1T.
[**put_muveto_voltage_map1_t_item**](MuvetoVoltageMap1TApi.md#put_muveto_voltage_map1_t_item) | **PUT** /xenon1t/muveto/voltage_maps/{muvetovoltagemap1tId} | Replaces a MuvetoVoltageMap1T document


# **delete_muveto_voltage_map1_t_item**
> delete_muveto_voltage_map1_t_item(muvetovoltagemap1t_id, if_match=if_match)

Deletes a MuvetoVoltageMap1T document

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
    api_instance = xepmts.MuvetoVoltageMap1TApi(api_client)
    muvetovoltagemap1t_id = 'muvetovoltagemap1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoVoltageMap1T document
        api_instance.delete_muveto_voltage_map1_t_item(muvetovoltagemap1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMap1TApi->delete_muveto_voltage_map1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagemap1t_id** | **str**|  | 
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
**204** | MuvetoVoltageMap1T document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_muveto_voltage_maps1_t**
> delete_muveto_voltage_maps1_t()

Deletes all MuvetoVoltageMaps1T

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
    api_instance = xepmts.MuvetoVoltageMap1TApi(api_client)
    
    try:
        # Deletes all MuvetoVoltageMaps1T
        api_instance.delete_muveto_voltage_maps1_t()
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMap1TApi->delete_muveto_voltage_maps1_t: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**204** | operation has been successful |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_voltage_map1_t_item**
> MuvetoVoltageMap1T get_muveto_voltage_map1_t_item(muvetovoltagemap1t_id)

Retrieves a MuvetoVoltageMap1T document

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
    api_instance = xepmts.MuvetoVoltageMap1TApi(api_client)
    muvetovoltagemap1t_id = 'muvetovoltagemap1t_id_example' # str | 

    try:
        # Retrieves a MuvetoVoltageMap1T document
        api_response = api_instance.get_muveto_voltage_map1_t_item(muvetovoltagemap1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMap1TApi->get_muveto_voltage_map1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagemap1t_id** | **str**|  | 

### Return type

[**MuvetoVoltageMap1T**](MuvetoVoltageMap1T.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoVoltageMap1T document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_voltage_map1_t_item_by_name**
> MuvetoVoltageMap1T get_muveto_voltage_map1_t_item_by_name(name)

Retrieves a MuvetoVoltageMap1T document by name

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
    api_instance = xepmts.MuvetoVoltageMap1TApi(api_client)
    name = 'name_example' # str | 

    try:
        # Retrieves a MuvetoVoltageMap1T document by name
        api_response = api_instance.get_muveto_voltage_map1_t_item_by_name(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMap1TApi->get_muveto_voltage_map1_t_item_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**MuvetoVoltageMap1T**](MuvetoVoltageMap1T.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoVoltageMap1T document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_voltage_maps1_t**
> InlineResponse20056 get_muveto_voltage_maps1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoVoltageMaps1T

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
    api_instance = xepmts.MuvetoVoltageMap1TApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoVoltageMaps1T
        api_response = api_instance.get_muveto_voltage_maps1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMap1TApi->get_muveto_voltage_maps1_t: %s\n" % e)
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
**200** | An array of MuvetoVoltageMaps1T |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_voltage_maps1_t**
> post_muveto_voltage_maps1_t(muveto_voltage_map1_t)

Stores one or more MuvetoVoltageMaps1T.

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
    api_instance = xepmts.MuvetoVoltageMap1TApi(api_client)
    muveto_voltage_map1_t = xepmts.MuvetoVoltageMap1T() # MuvetoVoltageMap1T | A MuvetoVoltageMap1T or list of MuvetoVoltageMap1T documents

    try:
        # Stores one or more MuvetoVoltageMaps1T.
        api_instance.post_muveto_voltage_maps1_t(muveto_voltage_map1_t)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMap1TApi->post_muveto_voltage_maps1_t: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_voltage_map1_t** | [**MuvetoVoltageMap1T**](MuvetoVoltageMap1T.md)| A MuvetoVoltageMap1T or list of MuvetoVoltageMap1T documents | 

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

# **put_muveto_voltage_map1_t_item**
> put_muveto_voltage_map1_t_item(muvetovoltagemap1t_id, muveto_voltage_map1_t, if_match=if_match)

Replaces a MuvetoVoltageMap1T document

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
    api_instance = xepmts.MuvetoVoltageMap1TApi(api_client)
    muvetovoltagemap1t_id = 'muvetovoltagemap1t_id_example' # str | 
muveto_voltage_map1_t = xepmts.MuvetoVoltageMap1T() # MuvetoVoltageMap1T | A MuvetoVoltageMap1T or list of MuvetoVoltageMap1T documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoVoltageMap1T document
        api_instance.put_muveto_voltage_map1_t_item(muvetovoltagemap1t_id, muveto_voltage_map1_t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMap1TApi->put_muveto_voltage_map1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagemap1t_id** | **str**|  | 
 **muveto_voltage_map1_t** | [**MuvetoVoltageMap1T**](MuvetoVoltageMap1T.md)| A MuvetoVoltageMap1T or list of MuvetoVoltageMap1T documents | 
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
**200** | MuvetoVoltageMap1T document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

