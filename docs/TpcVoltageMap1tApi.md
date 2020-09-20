# xepmts.TpcVoltageMap1tApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_voltage_map1t_item**](TpcVoltageMap1tApi.md#delete_tpc_voltage_map1t_item) | **DELETE** /xenon1t/tpc/voltage_maps/{tpcvoltagemap1tId} | Deletes a TpcVoltageMap1t document
[**delete_tpc_voltage_map1ts**](TpcVoltageMap1tApi.md#delete_tpc_voltage_map1ts) | **DELETE** /xenon1t/tpc/voltage_maps | Deletes all TpcVoltageMap1ts
[**get_tpc_voltage_map1t_item**](TpcVoltageMap1tApi.md#get_tpc_voltage_map1t_item) | **GET** /xenon1t/tpc/voltage_maps/{tpcvoltagemap1tId} | Retrieves a TpcVoltageMap1t document
[**get_tpc_voltage_map1t_item_by_name**](TpcVoltageMap1tApi.md#get_tpc_voltage_map1t_item_by_name) | **GET** /xenon1t/tpc/voltage_maps/{Name} | Retrieves a TpcVoltageMap1t document by name
[**get_tpc_voltage_map1ts**](TpcVoltageMap1tApi.md#get_tpc_voltage_map1ts) | **GET** /xenon1t/tpc/voltage_maps | Retrieves one or more TpcVoltageMap1ts
[**post_tpc_voltage_map1ts**](TpcVoltageMap1tApi.md#post_tpc_voltage_map1ts) | **POST** /xenon1t/tpc/voltage_maps | Stores one or more TpcVoltageMap1ts.
[**put_tpc_voltage_map1t_item**](TpcVoltageMap1tApi.md#put_tpc_voltage_map1t_item) | **PUT** /xenon1t/tpc/voltage_maps/{tpcvoltagemap1tId} | Replaces a TpcVoltageMap1t document


# **delete_tpc_voltage_map1t_item**
> delete_tpc_voltage_map1t_item(tpcvoltagemap1t_id, if_match=if_match)

Deletes a TpcVoltageMap1t document

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
    api_instance = xepmts.TpcVoltageMap1tApi(api_client)
    tpcvoltagemap1t_id = 'tpcvoltagemap1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcVoltageMap1t document
        api_instance.delete_tpc_voltage_map1t_item(tpcvoltagemap1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcVoltageMap1tApi->delete_tpc_voltage_map1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagemap1t_id** | **str**|  | 
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
**204** | TpcVoltageMap1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tpc_voltage_map1ts**
> delete_tpc_voltage_map1ts()

Deletes all TpcVoltageMap1ts

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
    api_instance = xepmts.TpcVoltageMap1tApi(api_client)
    
    try:
        # Deletes all TpcVoltageMap1ts
        api_instance.delete_tpc_voltage_map1ts()
    except ApiException as e:
        print("Exception when calling TpcVoltageMap1tApi->delete_tpc_voltage_map1ts: %s\n" % e)
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

# **get_tpc_voltage_map1t_item**
> TpcVoltageMap1t get_tpc_voltage_map1t_item(tpcvoltagemap1t_id)

Retrieves a TpcVoltageMap1t document

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
    api_instance = xepmts.TpcVoltageMap1tApi(api_client)
    tpcvoltagemap1t_id = 'tpcvoltagemap1t_id_example' # str | 

    try:
        # Retrieves a TpcVoltageMap1t document
        api_response = api_instance.get_tpc_voltage_map1t_item(tpcvoltagemap1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcVoltageMap1tApi->get_tpc_voltage_map1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagemap1t_id** | **str**|  | 

### Return type

[**TpcVoltageMap1t**](TpcVoltageMap1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcVoltageMap1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_voltage_map1t_item_by_name**
> TpcVoltageMap1t get_tpc_voltage_map1t_item_by_name(name)

Retrieves a TpcVoltageMap1t document by name

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
    api_instance = xepmts.TpcVoltageMap1tApi(api_client)
    name = 'name_example' # str | 

    try:
        # Retrieves a TpcVoltageMap1t document by name
        api_response = api_instance.get_tpc_voltage_map1t_item_by_name(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcVoltageMap1tApi->get_tpc_voltage_map1t_item_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**TpcVoltageMap1t**](TpcVoltageMap1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcVoltageMap1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_voltage_map1ts**
> InlineResponse20046 get_tpc_voltage_map1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcVoltageMap1ts

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
    api_instance = xepmts.TpcVoltageMap1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcVoltageMap1ts
        api_response = api_instance.get_tpc_voltage_map1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcVoltageMap1tApi->get_tpc_voltage_map1ts: %s\n" % e)
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

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcVoltageMap1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_voltage_map1ts**
> post_tpc_voltage_map1ts(tpc_voltage_map1t)

Stores one or more TpcVoltageMap1ts.

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
    api_instance = xepmts.TpcVoltageMap1tApi(api_client)
    tpc_voltage_map1t = xepmts.TpcVoltageMap1t() # TpcVoltageMap1t | A TpcVoltageMap1t or list of TpcVoltageMap1t documents

    try:
        # Stores one or more TpcVoltageMap1ts.
        api_instance.post_tpc_voltage_map1ts(tpc_voltage_map1t)
    except ApiException as e:
        print("Exception when calling TpcVoltageMap1tApi->post_tpc_voltage_map1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_voltage_map1t** | [**TpcVoltageMap1t**](TpcVoltageMap1t.md)| A TpcVoltageMap1t or list of TpcVoltageMap1t documents | 

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

# **put_tpc_voltage_map1t_item**
> put_tpc_voltage_map1t_item(tpcvoltagemap1t_id, tpc_voltage_map1t, if_match=if_match)

Replaces a TpcVoltageMap1t document

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
    api_instance = xepmts.TpcVoltageMap1tApi(api_client)
    tpcvoltagemap1t_id = 'tpcvoltagemap1t_id_example' # str | 
tpc_voltage_map1t = xepmts.TpcVoltageMap1t() # TpcVoltageMap1t | A TpcVoltageMap1t or list of TpcVoltageMap1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcVoltageMap1t document
        api_instance.put_tpc_voltage_map1t_item(tpcvoltagemap1t_id, tpc_voltage_map1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcVoltageMap1tApi->put_tpc_voltage_map1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagemap1t_id** | **str**|  | 
 **tpc_voltage_map1t** | [**TpcVoltageMap1t**](TpcVoltageMap1t.md)| A TpcVoltageMap1t or list of TpcVoltageMap1t documents | 
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
**200** | TpcVoltageMap1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

