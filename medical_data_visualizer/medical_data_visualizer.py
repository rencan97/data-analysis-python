import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")
df.head()


# Add 'overweight' column
def map_overweight(value):
    if value > 25: return 1
    else: return 0
df['overweight'] = (df['weight']/(df['height']/100)**2).map(map_overweight)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def applymap_normalize(value):
    if value > 1: return 1
    else: return 0
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].applymap(applymap_normalize)
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars="cardio", value_vars= ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby("cardio").value_counts().to_frame("total").reset_index()
    
    # Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    fig = sns.catplot(df_cat, x = "variable", order = df_cat['variable'].sort_values().unique(), y = "total", col = "cardio", hue = "value", kind="bar").fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] <= df['weight'].quantile(0.975))]

    print(df_heat)
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", ax = ax)
    
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

draw_heat_map()