# xepmts.TpcGainMeasurementApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_gain_measurement_item**](TpcGainMeasurementApi.md#delete_tpc_gain_measurement_item) | **DELETE** /tpc/gain_measurements/{tpcgainmeasurementId} | Deletes a TpcGainMeasurement document
[**get_tpc_gain_measurement_item**](TpcGainMeasurementApi.md#get_tpc_gain_measurement_item) | **GET** /tpc/gain_measurements/{tpcgainmeasurementId} | Retrieves a TpcGainMeasurement document
[**get_tpc_gain_measurements**](TpcGainMeasurementApi.md#get_tpc_gain_measurements) | **GET** /tpc/gain_measurements | Retrieves one or more TpcGainMeasurements
[**post_tpc_gain_measurements**](TpcGainMeasurementApi.md#post_tpc_gain_measurements) | **POST** /tpc/gain_measurements | Stores one or more TpcGainMeasurements.
[**put_tpc_gain_measurement_item**](TpcGainMeasurementApi.md#put_tpc_gain_measurement_item) | **PUT** /tpc/gain_measurements/{tpcgainmeasurementId} | Replaces a TpcGainMeasurement document


# **delete_tpc_gain_measurement_item**
> delete_tpc_gain_measurement_item(tpcgainmeasurement_id, if_match=if_match)

Deletes a TpcGainMeasurement document

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
    api_instance = xepmts.TpcGainMeasurementApi(api_client)
    tpcgainmeasurement_id = 'tpcgainmeasurement_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcGainMeasurement document
        api_instance.delete_tpc_gain_measurement_item(tpcgainmeasurement_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcGainMeasurementApi->delete_tpc_gain_measurement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcgainmeasurement_id** | **str**|  | 
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
**204** | TpcGainMeasurement document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_gain_measurement_item**
> TpcGainMeasurement get_tpc_gain_measurement_item(tpcgainmeasurement_id)

Retrieves a TpcGainMeasurement document

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
    api_instance = xepmts.TpcGainMeasurementApi(api_client)
    tpcgainmeasurement_id = 'tpcgainmeasurement_id_example' # str | 

    try:
        # Retrieves a TpcGainMeasurement document
        api_response = api_instance.get_tpc_gain_measurement_item(tpcgainmeasurement_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcGainMeasurementApi->get_tpc_gain_measurement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcgainmeasurement_id** | **str**|  | 

### Return type

[**TpcGainMeasurement**](TpcGainMeasurement.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcGainMeasurement document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_gain_measurements**
> InlineResponse20013 get_tpc_gain_measurements(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcGainMeasurements

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
    api_instance = xepmts.TpcGainMeasurementApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcGainMeasurements
        api_response = api_instance.get_tpc_gain_measurements(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcGainMeasurementApi->get_tpc_gain_measurements: %s\n" % e)
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

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcGainMeasurements |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_gain_measurements**
> post_tpc_gain_measurements(tpc_gain_measurement)

Stores one or more TpcGainMeasurements.

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
    api_instance = xepmts.TpcGainMeasurementApi(api_client)
    tpc_gain_measurement = xepmts.TpcGainMeasurement() # TpcGainMeasurement | A TpcGainMeasurement or list of TpcGainMeasurement documents

    try:
        # Stores one or more TpcGainMeasurements.
        api_instance.post_tpc_gain_measurements(tpc_gain_measurement)
    except ApiException as e:
        print("Exception when calling TpcGainMeasurementApi->post_tpc_gain_measurements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_gain_measurement** | [**TpcGainMeasurement**](TpcGainMeasurement.md)| A TpcGainMeasurement or list of TpcGainMeasurement documents | 

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

# **put_tpc_gain_measurement_item**
> put_tpc_gain_measurement_item(tpcgainmeasurement_id, tpc_gain_measurement, if_match=if_match)

Replaces a TpcGainMeasurement document

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
    api_instance = xepmts.TpcGainMeasurementApi(api_client)
    tpcgainmeasurement_id = 'tpcgainmeasurement_id_example' # str | 
tpc_gain_measurement = xepmts.TpcGainMeasurement() # TpcGainMeasurement | A TpcGainMeasurement or list of TpcGainMeasurement documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcGainMeasurement document
        api_instance.put_tpc_gain_measurement_item(tpcgainmeasurement_id, tpc_gain_measurement, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcGainMeasurementApi->put_tpc_gain_measurement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcgainmeasurement_id** | **str**|  | 
 **tpc_gain_measurement** | [**TpcGainMeasurement**](TpcGainMeasurement.md)| A TpcGainMeasurement or list of TpcGainMeasurement documents | 
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
**200** | TpcGainMeasurement document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

