# xepmts.NvetoAfterpulseApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_afterpulse_item**](NvetoAfterpulseApi.md#delete_nveto_afterpulse_item) | **DELETE** /nveto/afterpules/{nvetoafterpulseId} | Deletes a NvetoAfterpulse document
[**get_nveto_afterpulse_item**](NvetoAfterpulseApi.md#get_nveto_afterpulse_item) | **GET** /nveto/afterpules/{nvetoafterpulseId} | Retrieves a NvetoAfterpulse document
[**get_nveto_afterpulses**](NvetoAfterpulseApi.md#get_nveto_afterpulses) | **GET** /nveto/afterpules | Retrieves one or more NvetoAfterpulses
[**post_nveto_afterpulses**](NvetoAfterpulseApi.md#post_nveto_afterpulses) | **POST** /nveto/afterpules | Stores one or more NvetoAfterpulses.
[**put_nveto_afterpulse_item**](NvetoAfterpulseApi.md#put_nveto_afterpulse_item) | **PUT** /nveto/afterpules/{nvetoafterpulseId} | Replaces a NvetoAfterpulse document


# **delete_nveto_afterpulse_item**
> delete_nveto_afterpulse_item(nvetoafterpulse_id, if_match=if_match)

Deletes a NvetoAfterpulse document

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
    api_instance = xepmts.NvetoAfterpulseApi(api_client)
    nvetoafterpulse_id = 'nvetoafterpulse_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoAfterpulse document
        api_instance.delete_nveto_afterpulse_item(nvetoafterpulse_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoAfterpulseApi->delete_nveto_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetoafterpulse_id** | **str**|  | 
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
**204** | NvetoAfterpulse document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_afterpulse_item**
> NvetoAfterpulse get_nveto_afterpulse_item(nvetoafterpulse_id)

Retrieves a NvetoAfterpulse document

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
    api_instance = xepmts.NvetoAfterpulseApi(api_client)
    nvetoafterpulse_id = 'nvetoafterpulse_id_example' # str | 

    try:
        # Retrieves a NvetoAfterpulse document
        api_response = api_instance.get_nveto_afterpulse_item(nvetoafterpulse_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoAfterpulseApi->get_nveto_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetoafterpulse_id** | **str**|  | 

### Return type

[**NvetoAfterpulse**](NvetoAfterpulse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoAfterpulse document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_afterpulses**
> InlineResponse20017 get_nveto_afterpulses(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoAfterpulses

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
    api_instance = xepmts.NvetoAfterpulseApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoAfterpulses
        api_response = api_instance.get_nveto_afterpulses(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoAfterpulseApi->get_nveto_afterpulses: %s\n" % e)
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
**200** | An array of NvetoAfterpulses |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_afterpulses**
> post_nveto_afterpulses(nveto_afterpulse)

Stores one or more NvetoAfterpulses.

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
    api_instance = xepmts.NvetoAfterpulseApi(api_client)
    nveto_afterpulse = xepmts.NvetoAfterpulse() # NvetoAfterpulse | A NvetoAfterpulse or list of NvetoAfterpulse documents

    try:
        # Stores one or more NvetoAfterpulses.
        api_instance.post_nveto_afterpulses(nveto_afterpulse)
    except ApiException as e:
        print("Exception when calling NvetoAfterpulseApi->post_nveto_afterpulses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_afterpulse** | [**NvetoAfterpulse**](NvetoAfterpulse.md)| A NvetoAfterpulse or list of NvetoAfterpulse documents | 

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

# **put_nveto_afterpulse_item**
> put_nveto_afterpulse_item(nvetoafterpulse_id, nveto_afterpulse, if_match=if_match)

Replaces a NvetoAfterpulse document

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
    api_instance = xepmts.NvetoAfterpulseApi(api_client)
    nvetoafterpulse_id = 'nvetoafterpulse_id_example' # str | 
nveto_afterpulse = xepmts.NvetoAfterpulse() # NvetoAfterpulse | A NvetoAfterpulse or list of NvetoAfterpulse documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoAfterpulse document
        api_instance.put_nveto_afterpulse_item(nvetoafterpulse_id, nveto_afterpulse, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoAfterpulseApi->put_nveto_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetoafterpulse_id** | **str**|  | 
 **nveto_afterpulse** | [**NvetoAfterpulse**](NvetoAfterpulse.md)| A NvetoAfterpulse or list of NvetoAfterpulse documents | 
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
**200** | NvetoAfterpulse document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

