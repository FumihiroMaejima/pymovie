import os
import json
from attrdict import AttrDict

# TMDB API INFO
MOVIE_API_DOMAIN = os.getenv('TMDB_API_DOMAIN', 'pymovie')
MOVIE_API_KEY = os.getenv('TMDB_API_KEY', 'pymovie')
## api routing
MOVIE_TEST_API_ROUTE = '3/movie/550'
MOVIE_POPULAR_API_ROUTE = '3/movie/popular'
MOVIE_SEARCH_API_ROUTE = '3/search/movie/'
## common parameter
MOVIE_COMMON_GET_PARAMETER_KEY_API_KEY = 'api_key'  # valueは省略
MOVIE_COMMON_GET_PARAMETER_KEY_LANG = 'language'
MOVIE_COMMON_GET_PARAMETER_VALUE_LANG = 'ja-JP'
MOVIE_COMMON_GET_PARAMETER_KEY_PAGE = 'page'
MOVIE_COMMON_GET_PARAMETER_VALUE_PAGE = 1

# TMDB IMAGE INFO
MOVIE_IMAGE_DOMAIN = os.getenv('TMDB_IMAGE_API_DOMAIN', 'pymovie')

"""
Movie Image of API Config
type: json
"""
MOVIE_IMAGE_CONFIG = AttrDict(json.loads('{}'))
MOVIE_IMAGE_CONFIG.poster_size_185_url = MOVIE_IMAGE_DOMAIN + 't/p/w185'
MOVIE_IMAGE_CONFIG.poster_size_342_url = MOVIE_IMAGE_DOMAIN + 't/p/w342'

"""
Movie Test API Config
type: json
"""
API_TEST_CONFIG = AttrDict(json.loads('{}'))
API_TEST_CONFIG.test_api_url = MOVIE_API_DOMAIN + MOVIE_TEST_API_ROUTE
# get request parameter
API_TEST_CONFIG.param_api_key = MOVIE_COMMON_GET_PARAMETER_KEY_API_KEY
API_TEST_CONFIG.value_api_key = MOVIE_API_KEY
API_TEST_CONFIG.param_language = MOVIE_COMMON_GET_PARAMETER_KEY_LANG
API_TEST_CONFIG.value_language = MOVIE_COMMON_GET_PARAMETER_VALUE_LANG

"""
Movie Popular API Config
type: json
"""
API_POPULAR_CONFIG = AttrDict(json.loads('{}'))
API_POPULAR_CONFIG.test_api_url = MOVIE_API_DOMAIN + MOVIE_POPULAR_API_ROUTE
# get request parameter
API_POPULAR_CONFIG.param_api_key = MOVIE_COMMON_GET_PARAMETER_KEY_API_KEY
API_POPULAR_CONFIG.value_api_key = MOVIE_API_KEY
API_POPULAR_CONFIG.param_language = MOVIE_COMMON_GET_PARAMETER_KEY_LANG
API_POPULAR_CONFIG.value_language = MOVIE_COMMON_GET_PARAMETER_VALUE_LANG
API_POPULAR_CONFIG.param_page = MOVIE_COMMON_GET_PARAMETER_KEY_PAGE
API_POPULAR_CONFIG.value_page = MOVIE_COMMON_GET_PARAMETER_VALUE_PAGE


"""
Movie Search API Config
type: json
"""
API_SEARCH_CONFIG = AttrDict(json.loads('{}'))
API_SEARCH_CONFIG.search_url = MOVIE_API_DOMAIN + MOVIE_SEARCH_API_ROUTE
## common paramerter
API_SEARCH_CONFIG.param_api_key = MOVIE_COMMON_GET_PARAMETER_KEY_API_KEY
API_SEARCH_CONFIG.value_api_key = MOVIE_API_KEY
API_SEARCH_CONFIG.param_language = MOVIE_COMMON_GET_PARAMETER_KEY_LANG
API_SEARCH_CONFIG.value_language = MOVIE_COMMON_GET_PARAMETER_VALUE_LANG
API_SEARCH_CONFIG.param_page = MOVIE_COMMON_GET_PARAMETER_KEY_PAGE
API_SEARCH_CONFIG.value_page = MOVIE_COMMON_GET_PARAMETER_VALUE_PAGE
## query paramerter
API_SEARCH_CONFIG.param_query = 'query'
API_SEARCH_CONFIG.value_query = ''
