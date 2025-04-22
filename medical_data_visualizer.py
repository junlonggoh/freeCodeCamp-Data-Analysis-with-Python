import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv', header = 0, index_col = 0)

# 2
bmi = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = np.where(bmi > 25, 1, 0)
# Alternatively, convert from Boolean to integers: df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(by = ['cardio', 'variable', 'value']).value_counts().reset_index()
    df_cat = df_cat.rename(columns={'0': 'total'})

    # 7
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']).sort_values(by = ['cardio', 'variable', 'value'], ascending = True)
    df_cat_catplot = sns.catplot(data = df_cat, kind = 'count', col = 'cardio', x = 'variable', hue = 'value')
    df_cat_catplot.set_ylabels('total')
    
    # 8
    fig = df_cat_catplot.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    filter_ap = (df['ap_lo'] <= df['ap_hi'])
    filter_height = (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    filter_weight = (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))
    df_heat = df[filter_ap & filter_height & filter_weight]

    # 12
    corr = df_heat.reset_index().corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype = bool))

    # 14
    fig, ax = plt.subplots(figsize = (15, 12))

    # 15
    sns.heatmap(data = corr, annot = True, fmt = '0.1f', linewidths = 1, square = True, mask = mask, ax = ax)
    ax.set_title('Correlation Matrix')
    ax.set_xticklabels(ax.get_xticklabels(), rotation = 45, ha = 'right')
    ax.set_yticklabels(ax.get_yticklabels(), rotation = 0)

    # 16
    fig.savefig('heatmap.png')
    return fig
