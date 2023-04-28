# Changes Made to snscrape Python Module

We have made some changes to the snscrape python module to add Twitter authentication. These changes were made to improve the functionality of the module for our project. We are not the owners of snscrape and have only made changes for our specific use case.

The following lines were changed in the snscrape/modules/twitter.py file:

- Lines 674 to 680: added Twitter authentication to the request headers
- Lines 2030 to 2046: changed paginationVariables
- Lines 2049 to 2070: changed features
- Line 2074: changed api url

These changes allow us to use snscrape to scrape Twitter data with authenticated requests. By adding Twitter authentication, we can access tweets and other data that may not be available through unauthenticated requests.

Please note that these changes were made for our specific use case and may not be applicable to all users of the snscrape module. We recommend that users review the code changes and ensure that they are compatible with their own projects before using the modified module.