import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', header = 0, index_col= 'date', parse_dates = True)

# Clean data
df['value'] = df['value'].astype(dtype = 'float64')
botval = df['value'].quantile(0.025)
topval = df['value'].quantile(0.975)
botfil = df['value'] > botval
topfil = df['value'] < topval
df = df[botfil & topfil]
#print(botval, topval)
#df.describe()

def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig, ax = plt.subplots(figsize = (12, 8))
    ax.plot(df_line.index, df_line['value'], '-r')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year 
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar_month_mean = df_bar.groupby(['year', 'month']).mean()
    df_pivot = df_bar_month_mean.pivot_table(index = 'year', columns = 'month', values = 'value')

    # Draw bar plot
    # If using sns, skip lines 39 and 40 and run the following instead (colour will be different and some adjustments needed...): sns.barplot(x = 'year', y = 'value', hue = 'month', data = df_bar, ci = False)
    fig, ax = plt.subplots(figsize = (12, 8))
    df_pivot.plot(kind = 'bar', ax = ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title = 'Months', labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize = (16, 8))
    sns.boxplot(data = df_box, x = 'year', y = 'value', hue = 'year', ax = ax[0], palette = 'bright', orientation = 'vertical', legend = False)
    # pd.concat([pd.Series(df_box['month'].unique()[8:]), pd.Series(df_box['month'].unique()[:8])]).reset_index(drop = True)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data = df_box, x = 'month', y = 'value', hue = 'month', order = month_order, ax = ax[1], palette = 'husl', orientation = 'vertical', legend = False)
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
