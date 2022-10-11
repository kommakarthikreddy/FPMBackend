from lockshop.test.test import test_custom_get, test_custom_error, test_custom_post, \
    test_database_get, test_database_post

api_routes = [
    ('/api/lockshop/custom/get', test_custom_get, ["GET"]),
    ('/api/lockshop/test/custom/error', test_custom_error, ["GET"]),
    ('/api/lockshop/test/custom/post', test_custom_post, ["POST"]),
    ('/api/lockshop/test/database/get', test_database_get, ["GET"]),
    ('/api/lockshop/test/database/post', test_database_post, ["POST"])
]
