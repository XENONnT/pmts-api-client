# xepmts.NvetoAccountApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_account_item**](NvetoAccountApi.md#delete_nveto_account_item) | **DELETE** /nveto/accounts/{nvetoaccountId} | Deletes a NvetoAccount document
[**get_nveto_account_item**](NvetoAccountApi.md#get_nveto_account_item) | **GET** /nveto/accounts/{nvetoaccountId} | Retrieves a NvetoAccount document
[**get_nveto_account_item_by_username**](NvetoAccountApi.md#get_nveto_account_item_by_username) | **GET** /nveto/accounts/{Username} | Retrieves a NvetoAccount document by username
[**get_nveto_accounts**](NvetoAccountApi.md#get_nveto_accounts) | **GET** /nveto/accounts | Retrieves one or more NvetoAccounts
[**post_nveto_accounts**](NvetoAccountApi.md#post_nveto_accounts) | **POST** /nveto/accounts | Stores one or more NvetoAccounts.
[**put_nveto_account_item**](NvetoAccountApi.md#put_nveto_account_item) | **PUT** /nveto/accounts/{nvetoaccountId} | Replaces a NvetoAccount document


# **delete_nveto_account_item**
> delete_nveto_account_item(nvetoaccount_id, if_match=if_match)

Deletes a NvetoAccount document

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
    api_instance = xepmts.NvetoAccountApi(api_client)
    nvetoaccount_id = 'nvetoaccount_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoAccount document
        api_instance.delete_nveto_account_item(nvetoaccount_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoAccountApi->delete_nveto_account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetoaccount_id** | **str**|  | 
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
**204** | NvetoAccount document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_account_item**
> NvetoAccount get_nveto_account_item(nvetoaccount_id)

Retrieves a NvetoAccount document

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
    api_instance = xepmts.NvetoAccountApi(api_client)
    nvetoaccount_id = 'nvetoaccount_id_example' # str | 

    try:
        # Retrieves a NvetoAccount document
        api_response = api_instance.get_nveto_account_item(nvetoaccount_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoAccountApi->get_nveto_account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetoaccount_id** | **str**|  | 

### Return type

[**NvetoAccount**](NvetoAccount.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoAccount document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_account_item_by_username**
> NvetoAccount get_nveto_account_item_by_username(username)

Retrieves a NvetoAccount document by username

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
    api_instance = xepmts.NvetoAccountApi(api_client)
    username = 'username_example' # str | 

    try:
        # Retrieves a NvetoAccount document by username
        api_response = api_instance.get_nveto_account_item_by_username(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoAccountApi->get_nveto_account_item_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**NvetoAccount**](NvetoAccount.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoAccount document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_accounts**
> InlineResponse20023 get_nveto_accounts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoAccounts

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
    api_instance = xepmts.NvetoAccountApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoAccounts
        api_response = api_instance.get_nveto_accounts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoAccountApi->get_nveto_accounts: %s\n" % e)
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

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of NvetoAccounts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_accounts**
> post_nveto_accounts(nveto_account)

Stores one or more NvetoAccounts.

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
    api_instance = xepmts.NvetoAccountApi(api_client)
    nveto_account = xepmts.NvetoAccount() # NvetoAccount | A NvetoAccount or list of NvetoAccount documents

    try:
        # Stores one or more NvetoAccounts.
        api_instance.post_nveto_accounts(nveto_account)
    except ApiException as e:
        print("Exception when calling NvetoAccountApi->post_nveto_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_account** | [**NvetoAccount**](NvetoAccount.md)| A NvetoAccount or list of NvetoAccount documents | 

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

# **put_nveto_account_item**
> put_nveto_account_item(nvetoaccount_id, nveto_account, if_match=if_match)

Replaces a NvetoAccount document

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
    api_instance = xepmts.NvetoAccountApi(api_client)
    nvetoaccount_id = 'nvetoaccount_id_example' # str | 
nveto_account = xepmts.NvetoAccount() # NvetoAccount | A NvetoAccount or list of NvetoAccount documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoAccount document
        api_instance.put_nveto_account_item(nvetoaccount_id, nveto_account, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoAccountApi->put_nveto_account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetoaccount_id** | **str**|  | 
 **nveto_account** | [**NvetoAccount**](NvetoAccount.md)| A NvetoAccount or list of NvetoAccount documents | 
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
**200** | NvetoAccount document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

