# xepmts.NvetoVoltageMapApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_voltage_map_item**](NvetoVoltageMapApi.md#delete_nveto_voltage_map_item) | **DELETE** /nveto/voltage_maps/{nvetovoltagemapId} | Deletes a NvetoVoltageMap document
[**delete_nveto_voltage_maps**](NvetoVoltageMapApi.md#delete_nveto_voltage_maps) | **DELETE** /nveto/voltage_maps | Deletes all NvetoVoltageMaps
[**get_nveto_voltage_map_item**](NvetoVoltageMapApi.md#get_nveto_voltage_map_item) | **GET** /nveto/voltage_maps/{nvetovoltagemapId} | Retrieves a NvetoVoltageMap document
[**get_nveto_voltage_map_item_by_name**](NvetoVoltageMapApi.md#get_nveto_voltage_map_item_by_name) | **GET** /nveto/voltage_maps/{Name} | Retrieves a NvetoVoltageMap document by name
[**get_nveto_voltage_maps**](NvetoVoltageMapApi.md#get_nveto_voltage_maps) | **GET** /nveto/voltage_maps | Retrieves one or more NvetoVoltageMaps
[**post_nveto_voltage_maps**](NvetoVoltageMapApi.md#post_nveto_voltage_maps) | **POST** /nveto/voltage_maps | Stores one or more NvetoVoltageMaps.
[**put_nveto_voltage_map_item**](NvetoVoltageMapApi.md#put_nveto_voltage_map_item) | **PUT** /nveto/voltage_maps/{nvetovoltagemapId} | Replaces a NvetoVoltageMap document


# **delete_nveto_voltage_map_item**
> delete_nveto_voltage_map_item(nvetovoltagemap_id, if_match=if_match)

Deletes a NvetoVoltageMap document

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
    api_instance = xepmts.NvetoVoltageMapApi(api_client)
    nvetovoltagemap_id = 'nvetovoltagemap_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoVoltageMap document
        api_instance.delete_nveto_voltage_map_item(nvetovoltagemap_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoVoltageMapApi->delete_nveto_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetovoltagemap_id** | **str**|  | 
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
**204** | NvetoVoltageMap document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nveto_voltage_maps**
> delete_nveto_voltage_maps()

Deletes all NvetoVoltageMaps

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
    api_instance = xepmts.NvetoVoltageMapApi(api_client)
    
    try:
        # Deletes all NvetoVoltageMaps
        api_instance.delete_nveto_voltage_maps()
    except ApiException as e:
        print("Exception when calling NvetoVoltageMapApi->delete_nveto_voltage_maps: %s\n" % e)
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

# **get_nveto_voltage_map_item**
> NvetoVoltageMap get_nveto_voltage_map_item(nvetovoltagemap_id)

Retrieves a NvetoVoltageMap document

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
    api_instance = xepmts.NvetoVoltageMapApi(api_client)
    nvetovoltagemap_id = 'nvetovoltagemap_id_example' # str | 

    try:
        # Retrieves a NvetoVoltageMap document
        api_response = api_instance.get_nveto_voltage_map_item(nvetovoltagemap_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoVoltageMapApi->get_nveto_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetovoltagemap_id** | **str**|  | 

### Return type

[**NvetoVoltageMap**](NvetoVoltageMap.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoVoltageMap document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_voltage_map_item_by_name**
> NvetoVoltageMap get_nveto_voltage_map_item_by_name(name)

Retrieves a NvetoVoltageMap document by name

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
    api_instance = xepmts.NvetoVoltageMapApi(api_client)
    name = 'name_example' # str | 

    try:
        # Retrieves a NvetoVoltageMap document by name
        api_response = api_instance.get_nveto_voltage_map_item_by_name(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoVoltageMapApi->get_nveto_voltage_map_item_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**NvetoVoltageMap**](NvetoVoltageMap.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoVoltageMap document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_voltage_maps**
> InlineResponse20019 get_nveto_voltage_maps(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoVoltageMaps

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
    api_instance = xepmts.NvetoVoltageMapApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoVoltageMaps
        api_response = api_instance.get_nveto_voltage_maps(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoVoltageMapApi->get_nveto_voltage_maps: %s\n" % e)
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

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of NvetoVoltageMaps |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_voltage_maps**
> post_nveto_voltage_maps(nveto_voltage_map)

Stores one or more NvetoVoltageMaps.

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
    api_instance = xepmts.NvetoVoltageMapApi(api_client)
    nveto_voltage_map = xepmts.NvetoVoltageMap() # NvetoVoltageMap | A NvetoVoltageMap or list of NvetoVoltageMap documents

    try:
        # Stores one or more NvetoVoltageMaps.
        api_instance.post_nveto_voltage_maps(nveto_voltage_map)
    except ApiException as e:
        print("Exception when calling NvetoVoltageMapApi->post_nveto_voltage_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_voltage_map** | [**NvetoVoltageMap**](NvetoVoltageMap.md)| A NvetoVoltageMap or list of NvetoVoltageMap documents | 

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

# **put_nveto_voltage_map_item**
> put_nveto_voltage_map_item(nvetovoltagemap_id, nveto_voltage_map, if_match=if_match)

Replaces a NvetoVoltageMap document

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
    api_instance = xepmts.NvetoVoltageMapApi(api_client)
    nvetovoltagemap_id = 'nvetovoltagemap_id_example' # str | 
nveto_voltage_map = xepmts.NvetoVoltageMap() # NvetoVoltageMap | A NvetoVoltageMap or list of NvetoVoltageMap documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoVoltageMap document
        api_instance.put_nveto_voltage_map_item(nvetovoltagemap_id, nveto_voltage_map, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoVoltageMapApi->put_nveto_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetovoltagemap_id** | **str**|  | 
 **nveto_voltage_map** | [**NvetoVoltageMap**](NvetoVoltageMap.md)| A NvetoVoltageMap or list of NvetoVoltageMap documents | 
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
**200** | NvetoVoltageMap document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

