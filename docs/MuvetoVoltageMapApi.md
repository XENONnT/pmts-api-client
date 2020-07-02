# xepmts.MuvetoVoltageMapApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_voltage_map_item**](MuvetoVoltageMapApi.md#delete_muveto_voltage_map_item) | **DELETE** /muveto/voltage_maps/{muvetovoltagemapId} | Deletes a MuvetoVoltageMap document
[**delete_muveto_voltage_maps**](MuvetoVoltageMapApi.md#delete_muveto_voltage_maps) | **DELETE** /muveto/voltage_maps | Deletes all MuvetoVoltageMaps
[**get_muveto_voltage_map_item**](MuvetoVoltageMapApi.md#get_muveto_voltage_map_item) | **GET** /muveto/voltage_maps/{muvetovoltagemapId} | Retrieves a MuvetoVoltageMap document
[**get_muveto_voltage_map_item_by_name**](MuvetoVoltageMapApi.md#get_muveto_voltage_map_item_by_name) | **GET** /muveto/voltage_maps/{Name} | Retrieves a MuvetoVoltageMap document by name
[**get_muveto_voltage_maps**](MuvetoVoltageMapApi.md#get_muveto_voltage_maps) | **GET** /muveto/voltage_maps | Retrieves one or more MuvetoVoltageMaps
[**post_muveto_voltage_maps**](MuvetoVoltageMapApi.md#post_muveto_voltage_maps) | **POST** /muveto/voltage_maps | Stores one or more MuvetoVoltageMaps.
[**put_muveto_voltage_map_item**](MuvetoVoltageMapApi.md#put_muveto_voltage_map_item) | **PUT** /muveto/voltage_maps/{muvetovoltagemapId} | Replaces a MuvetoVoltageMap document


# **delete_muveto_voltage_map_item**
> delete_muveto_voltage_map_item(muvetovoltagemap_id, if_match=if_match)

Deletes a MuvetoVoltageMap document

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
    api_instance = xepmts.MuvetoVoltageMapApi(api_client)
    muvetovoltagemap_id = 'muvetovoltagemap_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoVoltageMap document
        api_instance.delete_muveto_voltage_map_item(muvetovoltagemap_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMapApi->delete_muveto_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagemap_id** | **str**|  | 
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
**204** | MuvetoVoltageMap document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_muveto_voltage_maps**
> delete_muveto_voltage_maps()

Deletes all MuvetoVoltageMaps

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
    api_instance = xepmts.MuvetoVoltageMapApi(api_client)
    
    try:
        # Deletes all MuvetoVoltageMaps
        api_instance.delete_muveto_voltage_maps()
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMapApi->delete_muveto_voltage_maps: %s\n" % e)
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

# **get_muveto_voltage_map_item**
> MuvetoVoltageMap get_muveto_voltage_map_item(muvetovoltagemap_id)

Retrieves a MuvetoVoltageMap document

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
    api_instance = xepmts.MuvetoVoltageMapApi(api_client)
    muvetovoltagemap_id = 'muvetovoltagemap_id_example' # str | 

    try:
        # Retrieves a MuvetoVoltageMap document
        api_response = api_instance.get_muveto_voltage_map_item(muvetovoltagemap_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMapApi->get_muveto_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagemap_id** | **str**|  | 

### Return type

[**MuvetoVoltageMap**](MuvetoVoltageMap.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoVoltageMap document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_voltage_map_item_by_name**
> MuvetoVoltageMap get_muveto_voltage_map_item_by_name(name)

Retrieves a MuvetoVoltageMap document by name

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
    api_instance = xepmts.MuvetoVoltageMapApi(api_client)
    name = 'name_example' # str | 

    try:
        # Retrieves a MuvetoVoltageMap document by name
        api_response = api_instance.get_muveto_voltage_map_item_by_name(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMapApi->get_muveto_voltage_map_item_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**MuvetoVoltageMap**](MuvetoVoltageMap.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoVoltageMap document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_voltage_maps**
> InlineResponse20032 get_muveto_voltage_maps(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoVoltageMaps

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
    api_instance = xepmts.MuvetoVoltageMapApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoVoltageMaps
        api_response = api_instance.get_muveto_voltage_maps(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMapApi->get_muveto_voltage_maps: %s\n" % e)
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

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoVoltageMaps |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_voltage_maps**
> post_muveto_voltage_maps(muveto_voltage_map)

Stores one or more MuvetoVoltageMaps.

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
    api_instance = xepmts.MuvetoVoltageMapApi(api_client)
    muveto_voltage_map = xepmts.MuvetoVoltageMap() # MuvetoVoltageMap | A MuvetoVoltageMap or list of MuvetoVoltageMap documents

    try:
        # Stores one or more MuvetoVoltageMaps.
        api_instance.post_muveto_voltage_maps(muveto_voltage_map)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMapApi->post_muveto_voltage_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_voltage_map** | [**MuvetoVoltageMap**](MuvetoVoltageMap.md)| A MuvetoVoltageMap or list of MuvetoVoltageMap documents | 

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

# **put_muveto_voltage_map_item**
> put_muveto_voltage_map_item(muvetovoltagemap_id, muveto_voltage_map, if_match=if_match)

Replaces a MuvetoVoltageMap document

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
    api_instance = xepmts.MuvetoVoltageMapApi(api_client)
    muvetovoltagemap_id = 'muvetovoltagemap_id_example' # str | 
muveto_voltage_map = xepmts.MuvetoVoltageMap() # MuvetoVoltageMap | A MuvetoVoltageMap or list of MuvetoVoltageMap documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoVoltageMap document
        api_instance.put_muveto_voltage_map_item(muvetovoltagemap_id, muveto_voltage_map, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageMapApi->put_muveto_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagemap_id** | **str**|  | 
 **muveto_voltage_map** | [**MuvetoVoltageMap**](MuvetoVoltageMap.md)| A MuvetoVoltageMap or list of MuvetoVoltageMap documents | 
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
**200** | MuvetoVoltageMap document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

