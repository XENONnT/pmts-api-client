# xepmts.HighVoltageChangeApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_high_voltage_change_item**](HighVoltageChangeApi.md#delete_high_voltage_change_item) | **DELETE** /hv_changes/{highvoltagechangeId} | Deletes a HighVoltageChange document
[**get_high_voltage_change_item**](HighVoltageChangeApi.md#get_high_voltage_change_item) | **GET** /hv_changes/{highvoltagechangeId} | Retrieves a HighVoltageChange document
[**get_high_voltage_changes**](HighVoltageChangeApi.md#get_high_voltage_changes) | **GET** /hv_changes | Retrieves one or more HighVoltageChanges
[**post_high_voltage_changes**](HighVoltageChangeApi.md#post_high_voltage_changes) | **POST** /hv_changes | Stores one or more HighVoltageChanges.
[**put_high_voltage_change_item**](HighVoltageChangeApi.md#put_high_voltage_change_item) | **PUT** /hv_changes/{highvoltagechangeId} | Replaces a HighVoltageChange document


# **delete_high_voltage_change_item**
> delete_high_voltage_change_item(highvoltagechange_id, if_match=if_match)

Deletes a HighVoltageChange document

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
    api_instance = xepmts.HighVoltageChangeApi(api_client)
    highvoltagechange_id = 'highvoltagechange_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a HighVoltageChange document
        api_instance.delete_high_voltage_change_item(highvoltagechange_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling HighVoltageChangeApi->delete_high_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **highvoltagechange_id** | **str**|  | 
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
**204** | HighVoltageChange document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_high_voltage_change_item**
> HighVoltageChange get_high_voltage_change_item(highvoltagechange_id)

Retrieves a HighVoltageChange document

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
    api_instance = xepmts.HighVoltageChangeApi(api_client)
    highvoltagechange_id = 'highvoltagechange_id_example' # str | 

    try:
        # Retrieves a HighVoltageChange document
        api_response = api_instance.get_high_voltage_change_item(highvoltagechange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HighVoltageChangeApi->get_high_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **highvoltagechange_id** | **str**|  | 

### Return type

[**HighVoltageChange**](HighVoltageChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HighVoltageChange document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_high_voltage_changes**
> InlineResponse20011 get_high_voltage_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more HighVoltageChanges

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
    api_instance = xepmts.HighVoltageChangeApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more HighVoltageChanges
        api_response = api_instance.get_high_voltage_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HighVoltageChangeApi->get_high_voltage_changes: %s\n" % e)
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

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of HighVoltageChanges |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_high_voltage_changes**
> post_high_voltage_changes(high_voltage_change)

Stores one or more HighVoltageChanges.

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
    api_instance = xepmts.HighVoltageChangeApi(api_client)
    high_voltage_change = xepmts.HighVoltageChange() # HighVoltageChange | A HighVoltageChange or list of HighVoltageChange documents

    try:
        # Stores one or more HighVoltageChanges.
        api_instance.post_high_voltage_changes(high_voltage_change)
    except ApiException as e:
        print("Exception when calling HighVoltageChangeApi->post_high_voltage_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **high_voltage_change** | [**HighVoltageChange**](HighVoltageChange.md)| A HighVoltageChange or list of HighVoltageChange documents | 

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

# **put_high_voltage_change_item**
> put_high_voltage_change_item(highvoltagechange_id, high_voltage_change, if_match=if_match)

Replaces a HighVoltageChange document

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
    api_instance = xepmts.HighVoltageChangeApi(api_client)
    highvoltagechange_id = 'highvoltagechange_id_example' # str | 
high_voltage_change = xepmts.HighVoltageChange() # HighVoltageChange | A HighVoltageChange or list of HighVoltageChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a HighVoltageChange document
        api_instance.put_high_voltage_change_item(highvoltagechange_id, high_voltage_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling HighVoltageChangeApi->put_high_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **highvoltagechange_id** | **str**|  | 
 **high_voltage_change** | [**HighVoltageChange**](HighVoltageChange.md)| A HighVoltageChange or list of HighVoltageChange documents | 
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
**200** | HighVoltageChange document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

