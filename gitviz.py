import requests
from plotly.graph_objs import Bar
from plotly import offline

###Make an API Call and store the response ###
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

### Store API response in a variable. ###
response_dict = response.json()
### Process results ###
print(response_dict.keys())


### Explore information about the repositories ###
print(f"Total Repositories: {response_dict['total_count']}")
repository_dict = response_dict['items']
print(f"Repositories returned: {len(repository_dict)}")


### Examining the first repository ###
# first_repo_dict = repository_dict[0]
# print(first_repo_dict)
# print(f"\nKeys: {len(first_repo_dict)}")
# for key in sorted(first_repo_dict.keys()):
#     print(key)

# print("\nSelected information about first repository:")
# print(f"Name: {first_repo_dict['name']}")
# print(f"Owner: {first_repo_dict['owner']['login']}")
# print(f"Stars: {first_repo_dict['stargazers_count']}")
# print(f"Repository: {first_repo_dict['html_url']}")
# print(f"Created: {first_repo_dict['created_at']}")
# print(f"Updated: {first_repo_dict['updated_at']}")
# print(f"Description: {first_repo_dict['description']}")

### Printing info from every item in the repository dictionary ###
# print("\nSelected information about each repository:")
# for repo in repository_dict:
#        print(f"\nName: {repo['name']}")
#        print(f"Owner: {repo['owner']['login']}")
#        print(f"Stars: {repo['stargazers_count']}")
#        print(f"Repository: {repo['html_url']}")
#        print(f"Description: {repo['description']}")

repo_info, stars, labels = [], [], []
for repo in repository_dict:
    repo_name = repo['name']
    repo_url = repo['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_info.append(repo_link)
    stars.append(repo['stargazers_count'])
    owner = repo['owner']['login']
    description = repo['description']
    label = f"Owner: {owner}<br />Description: {description}"
    labels.append(label)


### Putting the API Data in a Plotly Viz ###
data = [{
        'type': 'bar',
        'x': repo_info,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {
                'width': 1.5,
                'color': 'rgb(25, 25, 25)'
            }
        },
        'opacity': 0.6,
        }]
my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
