import pandas as pd
import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    """
    Fetches data from the given URL and returns the BeautifulSoup object.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to fetch data from {url}")
        return None

def get_table_data(soup, div_id):
    """
    Extracts table data from the specified div ID in the BeautifulSoup object.
    """
    data_div = soup.find('div', {'id': div_id})
    if data_div:
        table = data_div.find('table')
        if table:
            df = pd.read_html(str(table))[0]
            return df
    print(f"No data found for div_id: {div_id}")
    return None

def update_column_names(df):
    """
    Updates column names of the DataFrame by joining MultiIndex columns.
    """
    if isinstance(df.columns, pd.MultiIndex):
        new_columns = [('_'.join(col) if 'Unnamed' not in col[0] else col[1]) for col in df.columns]
        df.columns = new_columns
    return df

# Dictionary to map league names to their respective URLs
league_urls = {
    'EPL': 'https://fbref.com/en/comps/9/Premier-League-Stats',
    'Bundesliga': 'https://fbref.com/en/comps/20/Bundesliga-Stats',
    'LaLiga': 'https://fbref.com/en/comps/12/La-Liga-Stats',
    'SerieA': 'https://fbref.com/en/comps/11/Serie-A-Stats',
    'Ligue1': 'https://fbref.com/en/comps/13/Ligue-1-Stats'
}

# Initialize an empty list to store results
all_results = []

# Iterate over each league
for league_name, league_url in league_urls.items():
    # Fetching data from the URL
    soup = fetch_data(league_url)

    # Extracting various statistics
    team_table = get_table_data(soup, f'div_results2023-2024{league_url.split("/")[-2]}1_overall')
    squad_possession = get_table_data(soup, 'div_stats_squads_possession_for')
    squad_stats = get_table_data(soup, 'div_stats_squads_standard_for')
    squad_shooting = get_table_data(soup, 'div_stats_squads_shooting_for')
    squad_passing = get_table_data(soup, 'div_stats_squads_passing_for')
    squad_goal_shot_creation = get_table_data(soup, 'div_stats_squads_gca_for')
    squad_defensive = get_table_data(soup, 'div_stats_squads_defense_for')

    # Update column names for all DataFrames
    squad_possession = update_column_names(squad_possession)
    squad_stats = update_column_names(squad_stats)
    squad_shooting = update_column_names(squad_shooting)
    squad_passing = update_column_names(squad_passing)
    squad_goal_shot_creation = update_column_names(squad_goal_shot_creation)
    squad_defensive = update_column_names(squad_defensive)

    # Merging all DataFrames
    result = pd.merge(team_table, squad_possession, on='Squad', how='left')
    result = pd.merge(result, squad_stats, on='Squad', how='left')
    result = pd.merge(result, squad_shooting, on='Squad', how='left')
    result = pd.merge(result, squad_passing, on='Squad', how='left')
    result = pd.merge(result, squad_goal_shot_creation, on='Squad', how='left')
    result = pd.merge(result, squad_defensive, on='Squad', how='left')

    # Add a new column for league name
    result['League'] = league_name

    # Columns to drop
    columns_to_drop = ['Last 5', 'Attendance', 'Top Team Scorer', 'Goalkeeper', 'Notes',
                       '# Pl_y', 'Poss_y', 'Playing Time_MP', 'Playing Time_Starts',
                       'Playing Time_Min', 'Playing Time_90s', 'Per 90 Minutes_Gls',
                       'Per 90 Minutes_Ast', 'Per 90 Minutes_G+A', 'Per 90 Minutes_G-PK',
                       'Per 90 Minutes_G+A-PK', 'Per 90 Minutes_xG', 'Per 90 Minutes_xAG',
                       'Per 90 Minutes_xG+xAG', 'Per 90 Minutes_npxG', 'Per 90 Minutes_npxG+xAG',
                       '# Pl_x', '90s_y', '# Pl_y', '90s_x', '# Pl_x', '90s_y', '# Pl_y', '90s']

    # Dropping unnecessary columns
    result = result.drop(columns=columns_to_drop, axis=1)

    # Append the result to the list
    all_results.append(result)

# Concatenate all results into a single DataFrame
final_result = pd.concat(all_results)

# Displaying the first 5 rows of the final result
print(final_result.head(5))

# Saving the final result to a CSV file
final_result.to_csv('all_leagues_2023_2024.csv', index=False)
