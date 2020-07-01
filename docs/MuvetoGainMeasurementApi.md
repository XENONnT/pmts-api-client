# xepmts.MuvetoGainMeasurementApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_gain_measurement_item**](MuvetoGainMeasurementApi.md#delete_muveto_gain_measurement_item) | **DELETE** /muveto/gain_measurements/{muvetogainmeasurementId} | Deletes a MuvetoGainMeasurement document
[**get_muveto_gain_measurement_item**](MuvetoGainMeasurementApi.md#get_muveto_gain_measurement_item) | **GET** /muveto/gain_measurements/{muvetogainmeasurementId} | Retrieves a MuvetoGainMeasurement document
[**get_muveto_gain_measurements**](MuvetoGainMeasurementApi.md#get_muveto_gain_measurements) | **GET** /muveto/gain_measurements | Retrieves one or more MuvetoGainMeasurements
[**post_muveto_gain_measurements**](MuvetoGainMeasurementApi.md#post_muveto_gain_measurements) | **POST** /muveto/gain_measurements | Stores one or more MuvetoGainMeasurements.
[**put_muveto_gain_measurement_item**](MuvetoGainMeasurementApi.md#put_muveto_gain_measurement_item) | **PUT** /muveto/gain_measurements/{muvetogainmeasurementId} | Replaces a MuvetoGainMeasurement document


# **delete_muveto_gain_measurement_item**
> delete_muveto_gain_measurement_item(muvetogainmeasurement_id, if_match=if_match)

Deletes a MuvetoGainMeasurement document

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
    api_instance = xepmts.MuvetoGainMeasurementApi(api_client)
    muvetogainmeasurement_id = 'muvetogainmeasurement_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoGainMeasurement document
        api_instance.delete_muveto_gain_measurement_item(muvetogainmeasurement_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoGainMeasurementApi->delete_muveto_gain_measurement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogainmeasurement_id** | **str**|  | 
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
**204** | MuvetoGainMeasurement document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_gain_measurement_item**
> MuvetoGainMeasurement get_muveto_gain_measurement_item(muvetogainmeasurement_id)

Retrieves a MuvetoGainMeasurement document

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
    api_instance = xepmts.MuvetoGainMeasurementApi(api_client)
    muvetogainmeasurement_id = 'muvetogainmeasurement_id_example' # str | 

    try:
        # Retrieves a MuvetoGainMeasurement document
        api_response = api_instance.get_muveto_gain_measurement_item(muvetogainmeasurement_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoGainMeasurementApi->get_muveto_gain_measurement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogainmeasurement_id** | **str**|  | 

### Return type

[**MuvetoGainMeasurement**](MuvetoGainMeasurement.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoGainMeasurement document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_gain_measurements**
> InlineResponse20032 get_muveto_gain_measurements(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoGainMeasurements

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
    api_instance = xepmts.MuvetoGainMeasurementApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoGainMeasurements
        api_response = api_instance.get_muveto_gain_measurements(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoGainMeasurementApi->get_muveto_gain_measurements: %s\n" % e)
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

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoGainMeasurements |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_gain_measurements**
> post_muveto_gain_measurements(muveto_gain_measurement)

Stores one or more MuvetoGainMeasurements.

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
    api_instance = xepmts.MuvetoGainMeasurementApi(api_client)
    muveto_gain_measurement = xepmts.MuvetoGainMeasurement() # MuvetoGainMeasurement | A MuvetoGainMeasurement or list of MuvetoGainMeasurement documents

    try:
        # Stores one or more MuvetoGainMeasurements.
        api_instance.post_muveto_gain_measurements(muveto_gain_measurement)
    except ApiException as e:
        print("Exception when calling MuvetoGainMeasurementApi->post_muveto_gain_measurements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_gain_measurement** | [**MuvetoGainMeasurement**](MuvetoGainMeasurement.md)| A MuvetoGainMeasurement or list of MuvetoGainMeasurement documents | 

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

# **put_muveto_gain_measurement_item**
> put_muveto_gain_measurement_item(muvetogainmeasurement_id, muveto_gain_measurement, if_match=if_match)

Replaces a MuvetoGainMeasurement document

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
    api_instance = xepmts.MuvetoGainMeasurementApi(api_client)
    muvetogainmeasurement_id = 'muvetogainmeasurement_id_example' # str | 
muveto_gain_measurement = xepmts.MuvetoGainMeasurement() # MuvetoGainMeasurement | A MuvetoGainMeasurement or list of MuvetoGainMeasurement documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoGainMeasurement document
        api_instance.put_muveto_gain_measurement_item(muvetogainmeasurement_id, muveto_gain_measurement, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoGainMeasurementApi->put_muveto_gain_measurement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogainmeasurement_id** | **str**|  | 
 **muveto_gain_measurement** | [**MuvetoGainMeasurement**](MuvetoGainMeasurement.md)| A MuvetoGainMeasurement or list of MuvetoGainMeasurement documents | 
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
**200** | MuvetoGainMeasurement document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

