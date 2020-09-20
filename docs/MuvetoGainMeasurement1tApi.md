# xepmts.MuvetoGainMeasurement1tApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_gain_measurement1t_item**](MuvetoGainMeasurement1tApi.md#delete_muveto_gain_measurement1t_item) | **DELETE** /xenon1t/muveto/gain_measurements/{muvetogainmeasurement1tId} | Deletes a MuvetoGainMeasurement1t document
[**get_muveto_gain_measurement1t_item**](MuvetoGainMeasurement1tApi.md#get_muveto_gain_measurement1t_item) | **GET** /xenon1t/muveto/gain_measurements/{muvetogainmeasurement1tId} | Retrieves a MuvetoGainMeasurement1t document
[**get_muveto_gain_measurement1ts**](MuvetoGainMeasurement1tApi.md#get_muveto_gain_measurement1ts) | **GET** /xenon1t/muveto/gain_measurements | Retrieves one or more MuvetoGainMeasurement1ts
[**post_muveto_gain_measurement1ts**](MuvetoGainMeasurement1tApi.md#post_muveto_gain_measurement1ts) | **POST** /xenon1t/muveto/gain_measurements | Stores one or more MuvetoGainMeasurement1ts.
[**put_muveto_gain_measurement1t_item**](MuvetoGainMeasurement1tApi.md#put_muveto_gain_measurement1t_item) | **PUT** /xenon1t/muveto/gain_measurements/{muvetogainmeasurement1tId} | Replaces a MuvetoGainMeasurement1t document


# **delete_muveto_gain_measurement1t_item**
> delete_muveto_gain_measurement1t_item(muvetogainmeasurement1t_id, if_match=if_match)

Deletes a MuvetoGainMeasurement1t document

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
    api_instance = xepmts.MuvetoGainMeasurement1tApi(api_client)
    muvetogainmeasurement1t_id = 'muvetogainmeasurement1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoGainMeasurement1t document
        api_instance.delete_muveto_gain_measurement1t_item(muvetogainmeasurement1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoGainMeasurement1tApi->delete_muveto_gain_measurement1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogainmeasurement1t_id** | **str**|  | 
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
**204** | MuvetoGainMeasurement1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_gain_measurement1t_item**
> MuvetoGainMeasurement1t get_muveto_gain_measurement1t_item(muvetogainmeasurement1t_id)

Retrieves a MuvetoGainMeasurement1t document

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
    api_instance = xepmts.MuvetoGainMeasurement1tApi(api_client)
    muvetogainmeasurement1t_id = 'muvetogainmeasurement1t_id_example' # str | 

    try:
        # Retrieves a MuvetoGainMeasurement1t document
        api_response = api_instance.get_muveto_gain_measurement1t_item(muvetogainmeasurement1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoGainMeasurement1tApi->get_muveto_gain_measurement1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogainmeasurement1t_id** | **str**|  | 

### Return type

[**MuvetoGainMeasurement1t**](MuvetoGainMeasurement1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoGainMeasurement1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_gain_measurement1ts**
> InlineResponse20061 get_muveto_gain_measurement1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoGainMeasurement1ts

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
    api_instance = xepmts.MuvetoGainMeasurement1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoGainMeasurement1ts
        api_response = api_instance.get_muveto_gain_measurement1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoGainMeasurement1tApi->get_muveto_gain_measurement1ts: %s\n" % e)
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

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoGainMeasurement1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_gain_measurement1ts**
> post_muveto_gain_measurement1ts(muveto_gain_measurement1t)

Stores one or more MuvetoGainMeasurement1ts.

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
    api_instance = xepmts.MuvetoGainMeasurement1tApi(api_client)
    muveto_gain_measurement1t = xepmts.MuvetoGainMeasurement1t() # MuvetoGainMeasurement1t | A MuvetoGainMeasurement1t or list of MuvetoGainMeasurement1t documents

    try:
        # Stores one or more MuvetoGainMeasurement1ts.
        api_instance.post_muveto_gain_measurement1ts(muveto_gain_measurement1t)
    except ApiException as e:
        print("Exception when calling MuvetoGainMeasurement1tApi->post_muveto_gain_measurement1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_gain_measurement1t** | [**MuvetoGainMeasurement1t**](MuvetoGainMeasurement1t.md)| A MuvetoGainMeasurement1t or list of MuvetoGainMeasurement1t documents | 

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

# **put_muveto_gain_measurement1t_item**
> put_muveto_gain_measurement1t_item(muvetogainmeasurement1t_id, muveto_gain_measurement1t, if_match=if_match)

Replaces a MuvetoGainMeasurement1t document

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
    api_instance = xepmts.MuvetoGainMeasurement1tApi(api_client)
    muvetogainmeasurement1t_id = 'muvetogainmeasurement1t_id_example' # str | 
muveto_gain_measurement1t = xepmts.MuvetoGainMeasurement1t() # MuvetoGainMeasurement1t | A MuvetoGainMeasurement1t or list of MuvetoGainMeasurement1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoGainMeasurement1t document
        api_instance.put_muveto_gain_measurement1t_item(muvetogainmeasurement1t_id, muveto_gain_measurement1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoGainMeasurement1tApi->put_muveto_gain_measurement1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogainmeasurement1t_id** | **str**|  | 
 **muveto_gain_measurement1t** | [**MuvetoGainMeasurement1t**](MuvetoGainMeasurement1t.md)| A MuvetoGainMeasurement1t or list of MuvetoGainMeasurement1t documents | 
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
**200** | MuvetoGainMeasurement1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

