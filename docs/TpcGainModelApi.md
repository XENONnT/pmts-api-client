# xepmts.TpcGainModelApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_gain_model_item**](TpcGainModelApi.md#delete_tpc_gain_model_item) | **DELETE** /tpc/gain_models/{tpcgainmodelId} | Deletes a TpcGainModel document
[**get_tpc_gain_model_item**](TpcGainModelApi.md#get_tpc_gain_model_item) | **GET** /tpc/gain_models/{tpcgainmodelId} | Retrieves a TpcGainModel document
[**get_tpc_gain_models**](TpcGainModelApi.md#get_tpc_gain_models) | **GET** /tpc/gain_models | Retrieves one or more TpcGainModels
[**post_tpc_gain_models**](TpcGainModelApi.md#post_tpc_gain_models) | **POST** /tpc/gain_models | Stores one or more TpcGainModels.
[**put_tpc_gain_model_item**](TpcGainModelApi.md#put_tpc_gain_model_item) | **PUT** /tpc/gain_models/{tpcgainmodelId} | Replaces a TpcGainModel document


# **delete_tpc_gain_model_item**
> delete_tpc_gain_model_item(tpcgainmodel_id, if_match=if_match)

Deletes a TpcGainModel document

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
    api_instance = xepmts.TpcGainModelApi(api_client)
    tpcgainmodel_id = 'tpcgainmodel_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcGainModel document
        api_instance.delete_tpc_gain_model_item(tpcgainmodel_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcGainModelApi->delete_tpc_gain_model_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcgainmodel_id** | **str**|  | 
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
**204** | TpcGainModel document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_gain_model_item**
> TpcGainModel get_tpc_gain_model_item(tpcgainmodel_id)

Retrieves a TpcGainModel document

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
    api_instance = xepmts.TpcGainModelApi(api_client)
    tpcgainmodel_id = 'tpcgainmodel_id_example' # str | 

    try:
        # Retrieves a TpcGainModel document
        api_response = api_instance.get_tpc_gain_model_item(tpcgainmodel_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcGainModelApi->get_tpc_gain_model_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcgainmodel_id** | **str**|  | 

### Return type

[**TpcGainModel**](TpcGainModel.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcGainModel document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_gain_models**
> InlineResponse2001 get_tpc_gain_models(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcGainModels

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
    api_instance = xepmts.TpcGainModelApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcGainModels
        api_response = api_instance.get_tpc_gain_models(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcGainModelApi->get_tpc_gain_models: %s\n" % e)
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

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcGainModels |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_gain_models**
> post_tpc_gain_models(tpc_gain_model)

Stores one or more TpcGainModels.

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
    api_instance = xepmts.TpcGainModelApi(api_client)
    tpc_gain_model = xepmts.TpcGainModel() # TpcGainModel | A TpcGainModel or list of TpcGainModel documents

    try:
        # Stores one or more TpcGainModels.
        api_instance.post_tpc_gain_models(tpc_gain_model)
    except ApiException as e:
        print("Exception when calling TpcGainModelApi->post_tpc_gain_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_gain_model** | [**TpcGainModel**](TpcGainModel.md)| A TpcGainModel or list of TpcGainModel documents | 

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

# **put_tpc_gain_model_item**
> put_tpc_gain_model_item(tpcgainmodel_id, tpc_gain_model, if_match=if_match)

Replaces a TpcGainModel document

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
    api_instance = xepmts.TpcGainModelApi(api_client)
    tpcgainmodel_id = 'tpcgainmodel_id_example' # str | 
tpc_gain_model = xepmts.TpcGainModel() # TpcGainModel | A TpcGainModel or list of TpcGainModel documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcGainModel document
        api_instance.put_tpc_gain_model_item(tpcgainmodel_id, tpc_gain_model, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcGainModelApi->put_tpc_gain_model_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcgainmodel_id** | **str**|  | 
 **tpc_gain_model** | [**TpcGainModel**](TpcGainModel.md)| A TpcGainModel or list of TpcGainModel documents | 
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
**200** | TpcGainModel document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

