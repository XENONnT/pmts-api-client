# xepmts.NvetoVoltageChangeApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_voltage_change_item**](NvetoVoltageChangeApi.md#delete_nveto_voltage_change_item) | **DELETE** /nveto/voltage_changes/{nvetovoltagechangeId} | Deletes a NvetoVoltageChange document
[**get_nveto_voltage_change_item**](NvetoVoltageChangeApi.md#get_nveto_voltage_change_item) | **GET** /nveto/voltage_changes/{nvetovoltagechangeId} | Retrieves a NvetoVoltageChange document
[**get_nveto_voltage_changes**](NvetoVoltageChangeApi.md#get_nveto_voltage_changes) | **GET** /nveto/voltage_changes | Retrieves one or more NvetoVoltageChanges
[**post_nveto_voltage_changes**](NvetoVoltageChangeApi.md#post_nveto_voltage_changes) | **POST** /nveto/voltage_changes | Stores one or more NvetoVoltageChanges.
[**put_nveto_voltage_change_item**](NvetoVoltageChangeApi.md#put_nveto_voltage_change_item) | **PUT** /nveto/voltage_changes/{nvetovoltagechangeId} | Replaces a NvetoVoltageChange document


# **delete_nveto_voltage_change_item**
> delete_nveto_voltage_change_item(nvetovoltagechange_id, if_match=if_match)

Deletes a NvetoVoltageChange document

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
    api_instance = xepmts.NvetoVoltageChangeApi(api_client)
    nvetovoltagechange_id = 'nvetovoltagechange_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoVoltageChange document
        api_instance.delete_nveto_voltage_change_item(nvetovoltagechange_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoVoltageChangeApi->delete_nveto_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetovoltagechange_id** | **str**|  | 
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
**204** | NvetoVoltageChange document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_voltage_change_item**
> NvetoVoltageChange get_nveto_voltage_change_item(nvetovoltagechange_id)

Retrieves a NvetoVoltageChange document

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
    api_instance = xepmts.NvetoVoltageChangeApi(api_client)
    nvetovoltagechange_id = 'nvetovoltagechange_id_example' # str | 

    try:
        # Retrieves a NvetoVoltageChange document
        api_response = api_instance.get_nveto_voltage_change_item(nvetovoltagechange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoVoltageChangeApi->get_nveto_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetovoltagechange_id** | **str**|  | 

### Return type

[**NvetoVoltageChange**](NvetoVoltageChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoVoltageChange document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_voltage_changes**
> InlineResponse20017 get_nveto_voltage_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoVoltageChanges

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
    api_instance = xepmts.NvetoVoltageChangeApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoVoltageChanges
        api_response = api_instance.get_nveto_voltage_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoVoltageChangeApi->get_nveto_voltage_changes: %s\n" % e)
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

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of NvetoVoltageChanges |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_voltage_changes**
> post_nveto_voltage_changes(nveto_voltage_change)

Stores one or more NvetoVoltageChanges.

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
    api_instance = xepmts.NvetoVoltageChangeApi(api_client)
    nveto_voltage_change = xepmts.NvetoVoltageChange() # NvetoVoltageChange | A NvetoVoltageChange or list of NvetoVoltageChange documents

    try:
        # Stores one or more NvetoVoltageChanges.
        api_instance.post_nveto_voltage_changes(nveto_voltage_change)
    except ApiException as e:
        print("Exception when calling NvetoVoltageChangeApi->post_nveto_voltage_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_voltage_change** | [**NvetoVoltageChange**](NvetoVoltageChange.md)| A NvetoVoltageChange or list of NvetoVoltageChange documents | 

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

# **put_nveto_voltage_change_item**
> put_nveto_voltage_change_item(nvetovoltagechange_id, nveto_voltage_change, if_match=if_match)

Replaces a NvetoVoltageChange document

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
    api_instance = xepmts.NvetoVoltageChangeApi(api_client)
    nvetovoltagechange_id = 'nvetovoltagechange_id_example' # str | 
nveto_voltage_change = xepmts.NvetoVoltageChange() # NvetoVoltageChange | A NvetoVoltageChange or list of NvetoVoltageChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoVoltageChange document
        api_instance.put_nveto_voltage_change_item(nvetovoltagechange_id, nveto_voltage_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoVoltageChangeApi->put_nveto_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetovoltagechange_id** | **str**|  | 
 **nveto_voltage_change** | [**NvetoVoltageChange**](NvetoVoltageChange.md)| A NvetoVoltageChange or list of NvetoVoltageChange documents | 
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
**200** | NvetoVoltageChange document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

