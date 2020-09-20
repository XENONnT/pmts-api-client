# xepmts.MuvetoAfterpulseApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_afterpulse_item**](MuvetoAfterpulseApi.md#delete_muveto_afterpulse_item) | **DELETE** /muveto/afterpules/{muvetoafterpulseId} | Deletes a MuvetoAfterpulse document
[**get_muveto_afterpulse_item**](MuvetoAfterpulseApi.md#get_muveto_afterpulse_item) | **GET** /muveto/afterpules/{muvetoafterpulseId} | Retrieves a MuvetoAfterpulse document
[**get_muveto_afterpulses**](MuvetoAfterpulseApi.md#get_muveto_afterpulses) | **GET** /muveto/afterpules | Retrieves one or more MuvetoAfterpulses
[**post_muveto_afterpulses**](MuvetoAfterpulseApi.md#post_muveto_afterpulses) | **POST** /muveto/afterpules | Stores one or more MuvetoAfterpulses.
[**put_muveto_afterpulse_item**](MuvetoAfterpulseApi.md#put_muveto_afterpulse_item) | **PUT** /muveto/afterpules/{muvetoafterpulseId} | Replaces a MuvetoAfterpulse document


# **delete_muveto_afterpulse_item**
> delete_muveto_afterpulse_item(muvetoafterpulse_id, if_match=if_match)

Deletes a MuvetoAfterpulse document

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
    api_instance = xepmts.MuvetoAfterpulseApi(api_client)
    muvetoafterpulse_id = 'muvetoafterpulse_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoAfterpulse document
        api_instance.delete_muveto_afterpulse_item(muvetoafterpulse_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulseApi->delete_muveto_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoafterpulse_id** | **str**|  | 
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
**204** | MuvetoAfterpulse document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_afterpulse_item**
> MuvetoAfterpulse get_muveto_afterpulse_item(muvetoafterpulse_id)

Retrieves a MuvetoAfterpulse document

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
    api_instance = xepmts.MuvetoAfterpulseApi(api_client)
    muvetoafterpulse_id = 'muvetoafterpulse_id_example' # str | 

    try:
        # Retrieves a MuvetoAfterpulse document
        api_response = api_instance.get_muveto_afterpulse_item(muvetoafterpulse_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulseApi->get_muveto_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoafterpulse_id** | **str**|  | 

### Return type

[**MuvetoAfterpulse**](MuvetoAfterpulse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoAfterpulse document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_afterpulses**
> InlineResponse20033 get_muveto_afterpulses(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoAfterpulses

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
    api_instance = xepmts.MuvetoAfterpulseApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoAfterpulses
        api_response = api_instance.get_muveto_afterpulses(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulseApi->get_muveto_afterpulses: %s\n" % e)
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

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoAfterpulses |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_afterpulses**
> post_muveto_afterpulses(muveto_afterpulse)

Stores one or more MuvetoAfterpulses.

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
    api_instance = xepmts.MuvetoAfterpulseApi(api_client)
    muveto_afterpulse = xepmts.MuvetoAfterpulse() # MuvetoAfterpulse | A MuvetoAfterpulse or list of MuvetoAfterpulse documents

    try:
        # Stores one or more MuvetoAfterpulses.
        api_instance.post_muveto_afterpulses(muveto_afterpulse)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulseApi->post_muveto_afterpulses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_afterpulse** | [**MuvetoAfterpulse**](MuvetoAfterpulse.md)| A MuvetoAfterpulse or list of MuvetoAfterpulse documents | 

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

# **put_muveto_afterpulse_item**
> put_muveto_afterpulse_item(muvetoafterpulse_id, muveto_afterpulse, if_match=if_match)

Replaces a MuvetoAfterpulse document

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
    api_instance = xepmts.MuvetoAfterpulseApi(api_client)
    muvetoafterpulse_id = 'muvetoafterpulse_id_example' # str | 
muveto_afterpulse = xepmts.MuvetoAfterpulse() # MuvetoAfterpulse | A MuvetoAfterpulse or list of MuvetoAfterpulse documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoAfterpulse document
        api_instance.put_muveto_afterpulse_item(muvetoafterpulse_id, muveto_afterpulse, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulseApi->put_muveto_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoafterpulse_id** | **str**|  | 
 **muveto_afterpulse** | [**MuvetoAfterpulse**](MuvetoAfterpulse.md)| A MuvetoAfterpulse or list of MuvetoAfterpulse documents | 
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
**200** | MuvetoAfterpulse document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

