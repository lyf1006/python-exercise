def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

#关键字形参调用时等号两边不要有空格
my_profile = build_profile('Yufei', 'Liu', age=12, sex='female', field='CS')
print(my_profile)