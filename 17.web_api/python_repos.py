import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories: " , response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))

#某个description 为空时，报错 nothing can decode错误
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

#可视化, show_legend 参数表示是否显示图表侧边小方块（条形的含义）
my_style = LS('#333366', base_style=LCS)
#包装一个配置对象
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 14
my_config.label_font_size = 14
my_config.major_label_font_size = 18
#缩短较长的项目名为15个字符，鼠标指向显示完全
my_config.truncate_label = 15
#隐藏水平线
my_config.show_y_guides = False
my_config.width = 1000

#传入配置对象
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

# print("Repositories returned: ", len(repo_dicts))

# #研究每一个仓库
# print("\nSelected information about each repository: ")
# for repo_dict in repo_dicts:
#     print('Name: ', repo_dict['name'])
#     print('Owner: ', repo_dict['owner']['login'])
#     print('Stars: ', repo_dict['stargazers_count'])
#     print('Repository: ', repo_dict['html_url'])
#     print('Description: ', repo_dict['description'], '\n')