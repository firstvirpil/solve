import requests

from configuration6 import SERVICE_URL
from src.baseclasses.response6 import Response


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(200)

# z = {
#     'meta': {
#         'pagination': {
#             'total': 5052,
#             'pages': 506,
#             'page': 1,
#             'limit': 10,
#             'links': {
#                 'previous': None,
#                 'current': 'https://gorest.co.in/public/v1/users?page=1',
#                 'next': 'https://gorest.co.in/public/v1/users?page=2'
#             }
#         }
#     },
#     'data': [
#         {
#             'id': 5146, 'name': 'Acharyasuta Bhattacharya',
#             'email': 'bhattacharya_acharyasuta@monahan-oberbrunner.org',
#             'gender': 'male', 'status': 'active'},
#         {
#             'id': 5138,
#             'name': 'Bhaanumati Ahluwalia',
#             'email': 'ahluwalia_bhaanumati@legros-harber.name',
#             'gender': 'male', 'status': 'active'},
#         {
#             'id': 5135,
#             'name': 'Devak Mahajan CPA',
#             'email': 'devak_mahajan_cpa@stark.net',
#             'gender': 'male', 'status': 'inactive'
#         },
#         {
#             'id': 5124, 'name': 'Aashritha Panicker',
#             'email': 'panicker_aashritha@turner-dach.org',
#             'gender': 'male', 'status': 'active'
#         },
#         {
#             'id': 5122,
#             'name': 'Upendra Pillai',
#             'email': 'pillai_upendra@beatty.name',
#             'gender': 'male', 'status': 'active'
#         },
#         {
#             'id': 5121,
#             'name': 'Pres.Jyotsana Gupta',
#             'email': 'gupta_jyotsana_pres@pfeffer.com',
#             'gender': 'male',
#             'status': 'active'
#         },
#         {
#             'id': 5119, 'name': 'Rupinder Kakkar',
#             'email': 'kakkar_rupinder@watsica-sanford.com',
#             'gender': 'male',
#             'status': 'active'
#         },
#         {
#             'id': 5117,
#             'name': 'Chandini Bhattacharya',
#             'email': 'bhattacharya_chandini@robel.com',
#             'gender': 'female',
#             'status': 'active'
#         },
#         {
#             'id': 5116,
#             'name': 'Vimala Banerjee',
#             'email': 'vimala_banerjee@weber.io',
#             'gender': 'male',
#             'status': 'inactive'
#         },
#         {
#             'id': 5115,
#             'name': 'Devasree Rana',
#             'email': 'rana_devasree@torp.net',
#             'gender': 'female',
#             'status': 'inactive'
#         }
#     ]
# }
