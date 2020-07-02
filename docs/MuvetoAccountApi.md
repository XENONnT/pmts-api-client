# xepmts.MuvetoAccountApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_account_item**](MuvetoAccountApi.md#delete_muveto_account_item) | **DELETE** /muveto/accounts/{muvetoaccountId} | Deletes a MuvetoAccount document
[**get_muveto_account_item**](MuvetoAccountApi.md#get_muveto_account_item) | **GET** /muveto/accounts/{muvetoaccountId} | Retrieves a MuvetoAccount document
[**get_muveto_account_item_by_username**](MuvetoAccountApi.md#get_muveto_account_item_by_username) | **GET** /muveto/accounts/{Username} | Retrieves a MuvetoAccount document by username
[**get_muveto_accounts**](MuvetoAccountApi.md#get_muveto_accounts) | **GET** /muveto/accounts | Retrieves one or more MuvetoAccounts
[**post_muveto_accounts**](MuvetoAccountApi.md#post_muveto_accounts) | **POST** /muveto/accounts | Stores one or more MuvetoAccounts.
[**put_muveto_account_item**](MuvetoAccountApi.md#put_muveto_account_item) | **PUT** /muveto/accounts/{muvetoaccountId} | Replaces a MuvetoAccount document


# **delete_muveto_account_item**
> delete_muveto_account_item(muvetoaccount_id, if_match=if_match)

Deletes a MuvetoAccount document

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
    api_instance = xepmts.MuvetoAccountApi(api_client)
    muvetoaccount_id = 'muvetoaccount_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoAccount document
        api_instance.delete_muveto_account_item(muvetoaccount_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoAccountApi->delete_muveto_account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoaccount_id** | **str**|  | 
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
**204** | MuvetoAccount document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_account_item**
> MuvetoAccount get_muveto_account_item(muvetoaccount_id)

Retrieves a MuvetoAccount document

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
    api_instance = xepmts.MuvetoAccountApi(api_client)
    muvetoaccount_id = 'muvetoaccount_id_example' # str | 

    try:
        # Retrieves a MuvetoAccount document
        api_response = api_instance.get_muveto_account_item(muvetoaccount_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoAccountApi->get_muveto_account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoaccount_id** | **str**|  | 

### Return type

[**MuvetoAccount**](MuvetoAccount.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoAccount document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_account_item_by_username**
> MuvetoAccount get_muveto_account_item_by_username(username)

Retrieves a MuvetoAccount document by username

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
    api_instance = xepmts.MuvetoAccountApi(api_client)
    username = 'username_example' # str | 

    try:
        # Retrieves a MuvetoAccount document by username
        api_response = api_instance.get_muveto_account_item_by_username(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoAccountApi->get_muveto_account_item_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**MuvetoAccount**](MuvetoAccount.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoAccount document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_accounts**
> InlineResponse20035 get_muveto_accounts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoAccounts

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
    api_instance = xepmts.MuvetoAccountApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoAccounts
        api_response = api_instance.get_muveto_accounts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoAccountApi->get_muveto_accounts: %s\n" % e)
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

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoAccounts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_accounts**
> post_muveto_accounts(muveto_account)

Stores one or more MuvetoAccounts.

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
    api_instance = xepmts.MuvetoAccountApi(api_client)
    muveto_account = xepmts.MuvetoAccount() # MuvetoAccount | A MuvetoAccount or list of MuvetoAccount documents

    try:
        # Stores one or more MuvetoAccounts.
        api_instance.post_muveto_accounts(muveto_account)
    except ApiException as e:
        print("Exception when calling MuvetoAccountApi->post_muveto_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_account** | [**MuvetoAccount**](MuvetoAccount.md)| A MuvetoAccount or list of MuvetoAccount documents | 

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

# **put_muveto_account_item**
> put_muveto_account_item(muvetoaccount_id, muveto_account, if_match=if_match)

Replaces a MuvetoAccount document

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
    api_instance = xepmts.MuvetoAccountApi(api_client)
    muvetoaccount_id = 'muvetoaccount_id_example' # str | 
muveto_account = xepmts.MuvetoAccount() # MuvetoAccount | A MuvetoAccount or list of MuvetoAccount documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoAccount document
        api_instance.put_muveto_account_item(muvetoaccount_id, muveto_account, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoAccountApi->put_muveto_account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoaccount_id** | **str**|  | 
 **muveto_account** | [**MuvetoAccount**](MuvetoAccount.md)| A MuvetoAccount or list of MuvetoAccount documents | 
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
**200** | MuvetoAccount document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

