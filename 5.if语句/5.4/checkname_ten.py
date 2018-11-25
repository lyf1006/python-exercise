current_users = ['Mary','Lily','admin','Jack','Tom']
new_users = ['John','qingqian','mary','xiaoxiannv','Tom']

for user in new_users:
    #列表解析，实现忽略大小写的比较
    if user.lower() in [current_user.lower() for current_user in current_users]: 
        print("该用户名已被占用，请更换。")
    else:
        print("设置用户名成功。")