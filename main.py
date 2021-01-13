import argparse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-nb", "--repos_number", help="""an integer representing the number of repos to see (max:20)""")
    return parser.parse_args()

def data_prep(path, number_repos):
    repo_data = pd.read_csv(path)
    # converting stars into integer
    stars = []
    for star in repo_data["star"].to_list():
        if star[-1] =='k':
            star = float(star[:-1]) * 1000
        else:
            star = float(star)
        stars.append(int(star))
    repo_data["star"] = stars
    # sorting values
    repo_data = repo_data.sort_values(by="star", axis=0, ascending=False)
    return repo_data.head(number_repos)

def generate_graph(data):
    fig, ax = plt.subplots(tight_layout=True)

    ind = 0.2  # the x locations for the groups
    width = 0.1  # the width of the bars

    for i in range(len(data)):
        rects1 = ax.bar(ind*i - width/len(data), int(data["star"].iloc[i]), width, color="blue")

    ax.set_xlabel('repositories')
    ax.set_title('Top 2020 github repositories according to the dataset')
    ax.set_xticks(np.arange(10)/5)
    ax.set_xticklabels(data["name"].to_list())

    ax.grid()

    plt.show()


def main():
    data = data_prep("Github_data.csv", 10)
    generate_graph(data[['name', 'star']])

if __name__ == '__main__':
    main()
