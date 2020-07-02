# xepmts.NvetoGainApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_gain_item**](NvetoGainApi.md#delete_nveto_gain_item) | **DELETE** /nveto/gains/{nvetogainId} | Deletes a NvetoGain document
[**get_nveto_gain_item**](NvetoGainApi.md#get_nveto_gain_item) | **GET** /nveto/gains/{nvetogainId} | Retrieves a NvetoGain document
[**get_nveto_gains**](NvetoGainApi.md#get_nveto_gains) | **GET** /nveto/gains | Retrieves one or more NvetoGains
[**post_nveto_gains**](NvetoGainApi.md#post_nveto_gains) | **POST** /nveto/gains | Stores one or more NvetoGains.
[**put_nveto_gain_item**](NvetoGainApi.md#put_nveto_gain_item) | **PUT** /nveto/gains/{nvetogainId} | Replaces a NvetoGain document


# **delete_nveto_gain_item**
> delete_nveto_gain_item(nvetogain_id, if_match=if_match)

Deletes a NvetoGain document

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
    api_instance = xepmts.NvetoGainApi(api_client)
    nvetogain_id = 'nvetogain_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoGain document
        api_instance.delete_nveto_gain_item(nvetogain_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoGainApi->delete_nveto_gain_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogain_id** | **str**|  | 
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
**204** | NvetoGain document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_gain_item**
> NvetoGain get_nveto_gain_item(nvetogain_id)

Retrieves a NvetoGain document

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
    api_instance = xepmts.NvetoGainApi(api_client)
    nvetogain_id = 'nvetogain_id_example' # str | 

    try:
        # Retrieves a NvetoGain document
        api_response = api_instance.get_nveto_gain_item(nvetogain_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoGainApi->get_nveto_gain_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogain_id** | **str**|  | 

### Return type

[**NvetoGain**](NvetoGain.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoGain document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_gains**
> InlineResponse20016 get_nveto_gains(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoGains

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
    api_instance = xepmts.NvetoGainApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoGains
        api_response = api_instance.get_nveto_gains(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoGainApi->get_nveto_gains: %s\n" % e)
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

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of NvetoGains |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_gains**
> post_nveto_gains(nveto_gain)

Stores one or more NvetoGains.

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
    api_instance = xepmts.NvetoGainApi(api_client)
    nveto_gain = xepmts.NvetoGain() # NvetoGain | A NvetoGain or list of NvetoGain documents

    try:
        # Stores one or more NvetoGains.
        api_instance.post_nveto_gains(nveto_gain)
    except ApiException as e:
        print("Exception when calling NvetoGainApi->post_nveto_gains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_gain** | [**NvetoGain**](NvetoGain.md)| A NvetoGain or list of NvetoGain documents | 

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

# **put_nveto_gain_item**
> put_nveto_gain_item(nvetogain_id, nveto_gain, if_match=if_match)

Replaces a NvetoGain document

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
    api_instance = xepmts.NvetoGainApi(api_client)
    nvetogain_id = 'nvetogain_id_example' # str | 
nveto_gain = xepmts.NvetoGain() # NvetoGain | A NvetoGain or list of NvetoGain documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoGain document
        api_instance.put_nveto_gain_item(nvetogain_id, nveto_gain, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoGainApi->put_nveto_gain_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogain_id** | **str**|  | 
 **nveto_gain** | [**NvetoGain**](NvetoGain.md)| A NvetoGain or list of NvetoGain documents | 
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
**200** | NvetoGain document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

