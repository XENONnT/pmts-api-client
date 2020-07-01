# xepmts.TpcVoltageMapApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_voltage_map_item**](TpcVoltageMapApi.md#delete_tpc_voltage_map_item) | **DELETE** /tpc/voltage_maps/{tpcvoltagemapId} | Deletes a TpcVoltageMap document
[**delete_tpc_voltage_maps**](TpcVoltageMapApi.md#delete_tpc_voltage_maps) | **DELETE** /tpc/voltage_maps | Deletes all TpcVoltageMaps
[**get_tpc_voltage_map_item**](TpcVoltageMapApi.md#get_tpc_voltage_map_item) | **GET** /tpc/voltage_maps/{tpcvoltagemapId} | Retrieves a TpcVoltageMap document
[**get_tpc_voltage_map_item_by_name**](TpcVoltageMapApi.md#get_tpc_voltage_map_item_by_name) | **GET** /tpc/voltage_maps/{Name} | Retrieves a TpcVoltageMap document by name
[**get_tpc_voltage_maps**](TpcVoltageMapApi.md#get_tpc_voltage_maps) | **GET** /tpc/voltage_maps | Retrieves one or more TpcVoltageMaps
[**post_tpc_voltage_maps**](TpcVoltageMapApi.md#post_tpc_voltage_maps) | **POST** /tpc/voltage_maps | Stores one or more TpcVoltageMaps.
[**put_tpc_voltage_map_item**](TpcVoltageMapApi.md#put_tpc_voltage_map_item) | **PUT** /tpc/voltage_maps/{tpcvoltagemapId} | Replaces a TpcVoltageMap document


# **delete_tpc_voltage_map_item**
> delete_tpc_voltage_map_item(tpcvoltagemap_id, if_match=if_match)

Deletes a TpcVoltageMap document

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
    api_instance = xepmts.TpcVoltageMapApi(api_client)
    tpcvoltagemap_id = 'tpcvoltagemap_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcVoltageMap document
        api_instance.delete_tpc_voltage_map_item(tpcvoltagemap_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcVoltageMapApi->delete_tpc_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagemap_id** | **str**|  | 
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
**204** | TpcVoltageMap document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tpc_voltage_maps**
> delete_tpc_voltage_maps()

Deletes all TpcVoltageMaps

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
    api_instance = xepmts.TpcVoltageMapApi(api_client)
    
    try:
        # Deletes all TpcVoltageMaps
        api_instance.delete_tpc_voltage_maps()
    except ApiException as e:
        print("Exception when calling TpcVoltageMapApi->delete_tpc_voltage_maps: %s\n" % e)
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

# **get_tpc_voltage_map_item**
> TpcVoltageMap get_tpc_voltage_map_item(tpcvoltagemap_id)

Retrieves a TpcVoltageMap document

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
    api_instance = xepmts.TpcVoltageMapApi(api_client)
    tpcvoltagemap_id = 'tpcvoltagemap_id_example' # str | 

    try:
        # Retrieves a TpcVoltageMap document
        api_response = api_instance.get_tpc_voltage_map_item(tpcvoltagemap_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcVoltageMapApi->get_tpc_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagemap_id** | **str**|  | 

### Return type

[**TpcVoltageMap**](TpcVoltageMap.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcVoltageMap document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_voltage_map_item_by_name**
> TpcVoltageMap get_tpc_voltage_map_item_by_name(name)

Retrieves a TpcVoltageMap document by name

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
    api_instance = xepmts.TpcVoltageMapApi(api_client)
    name = 'name_example' # str | 

    try:
        # Retrieves a TpcVoltageMap document by name
        api_response = api_instance.get_tpc_voltage_map_item_by_name(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcVoltageMapApi->get_tpc_voltage_map_item_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**TpcVoltageMap**](TpcVoltageMap.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcVoltageMap document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_voltage_maps**
> InlineResponse2007 get_tpc_voltage_maps(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcVoltageMaps

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
    api_instance = xepmts.TpcVoltageMapApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcVoltageMaps
        api_response = api_instance.get_tpc_voltage_maps(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcVoltageMapApi->get_tpc_voltage_maps: %s\n" % e)
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

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcVoltageMaps |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_voltage_maps**
> post_tpc_voltage_maps(tpc_voltage_map)

Stores one or more TpcVoltageMaps.

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
    api_instance = xepmts.TpcVoltageMapApi(api_client)
    tpc_voltage_map = xepmts.TpcVoltageMap() # TpcVoltageMap | A TpcVoltageMap or list of TpcVoltageMap documents

    try:
        # Stores one or more TpcVoltageMaps.
        api_instance.post_tpc_voltage_maps(tpc_voltage_map)
    except ApiException as e:
        print("Exception when calling TpcVoltageMapApi->post_tpc_voltage_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_voltage_map** | [**TpcVoltageMap**](TpcVoltageMap.md)| A TpcVoltageMap or list of TpcVoltageMap documents | 

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

# **put_tpc_voltage_map_item**
> put_tpc_voltage_map_item(tpcvoltagemap_id, tpc_voltage_map, if_match=if_match)

Replaces a TpcVoltageMap document

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
    api_instance = xepmts.TpcVoltageMapApi(api_client)
    tpcvoltagemap_id = 'tpcvoltagemap_id_example' # str | 
tpc_voltage_map = xepmts.TpcVoltageMap() # TpcVoltageMap | A TpcVoltageMap or list of TpcVoltageMap documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcVoltageMap document
        api_instance.put_tpc_voltage_map_item(tpcvoltagemap_id, tpc_voltage_map, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcVoltageMapApi->put_tpc_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagemap_id** | **str**|  | 
 **tpc_voltage_map** | [**TpcVoltageMap**](TpcVoltageMap.md)| A TpcVoltageMap or list of TpcVoltageMap documents | 
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
**200** | TpcVoltageMap document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

