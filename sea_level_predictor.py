import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', header = 0, index_col = 'Year')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (12, 8))
    ax.scatter(df.index, df['CSIRO Adjusted Sea Level'], s = 20, color = 'red')

    # Create first line of best fit
    lrval1 = linregress(x = df.index, y = df['CSIRO Adjusted Sea Level'])
    slope1, intercept1 = lrval1[0], lrval1[1]
    xextended = pd.concat([pd.Series(df.index), pd.Series(range(2014, 2051, 1))]).reset_index(drop = True)
    line1 = (slope1 * xextended) + intercept1
    ax.plot(xextended, line1, color = 'green')

    # Create second line of best fit
    lrval2 = linregress(x = df.index[df.index >= 2000], y = df[df.index >= 2000]['CSIRO Adjusted Sea Level'])
    slope2, intercept2 = lrval2[0], lrval2[1]
    xrecent = xextended[xextended >= 2000].reset_index(drop = True)
    line2 = (slope2 * xrecent) + intercept2
    ax.plot(xrecent, line2, color = 'blue')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()