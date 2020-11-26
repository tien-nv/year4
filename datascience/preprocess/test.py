import json

# with open('data.txt',mode='r', encoding='utf-8') as file:
#     data = file.readlines()

# result = list()
# for _data in data:
#     print(_data)
#     abc
#     result.append(json.loads(_data))

# print(result[0])
data = "{'ad_id': 110560491, 'list_id': 77721590, 'list_time': 1602761598942, 'date': '4 phút trước', 'account_id': 1382724, 'account_oid': '35b5870a67ecb9fa840301378a07ed2b', 'account_name': 'Cẩm Dương', 'subject': 'Tôi là chính chủ cần bán Gấp nhà 3 tầng như ảnh', 'body': 'Nhà chính chủ mang tên tôi. \nVì lý do cá nhân, tôi đang cần bán gấp. \nNhà 3 tầng, 3 phòng ngủ. Đẹp như ảnh đăng, \nMiễn trung gian cò lái. \nAi đi xem nhà chính chủ liên hệ tôi', 'category': 1020, 'area': 89, 'area_name': 'Huyện Hoài Đức', 'region': 12, 'region_name': 'Hà Nội', 'company_ad': 0, 'type': 's', 'price': 1200000000, 'price_string': '1,2 tỷ', 'image': 'https://cdn.chotot.com/ovhJ8WRIA_FXw7m90EilEvy9Li-dg0KOBBAPqCRuQU0/preset:listing/plain/00d13c21bfe9eca04c57aebcb7c15a26-2686610335480979194.jpg', 'number_of_images': 5, 'ad_features': [{'name': 'price', 'mapping_id': 11, 'expired_time': 1602933529}], 'avatar': 'https://st.chotot.com/imaginary/10e4b6e986af11005bf1a61639118d98d7b9c3f5/profile_avatar/4dc2bb359812eea0ba59a95e40a8aab0de42d481/thumbnail?width=32', 'rooms': 3, 'property_legal_document': 1, 'region_v2': 12000, 'area_v2': 12089, 'ward': 378, 'ward_name': 'Xã La Phù', 'category_name': 'Nhà ở'}"
data  = data.replace("'",'"')
data = json.loads(data)
print(data.keys())