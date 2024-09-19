# # # # # from espn_api.basketball import League
# # # # # import streamlit as st
# # # # # import datetime
# # # # # from datetime import datetime
# # # # # import plotly.express as px
# # # # # import pandas as pd
# # # # # # swid='{B930EA19-EB1C-47CD-B230-C9A674365B87}',
# # # # # # espn_s2='AECt%2FzRlxgX0ONDBmXm%2FmZnRjdEGtqr6xajwnwyH5y2r8dp%2Ff1fwHHlgNqJbjf64de9Bnq8AhxO9BFz6jJ6APzFMBuH713J1ntVm%2FB40eCqRkyPsfq8WJCbiH4AGsEaHhv4wwzW32ogMACsZZ75eZ3AgB6p2V15xy35AYP4mABywoe3tMI9tr3wBxpcpFNt%2F%2BwsMyjPrj0H5rbhPIcTW8UuoRIrjRmj87KS9gqgfZcUj15y4qcweRL%2FMFyB%2BodHrtpCk6fYJVyjSqJ2P9K1Rkvm3r1yDjMbThmILeZcI%2FoNuJw%3D%3D'
# # # # # #id = 145228487
# # # # # page = st.sidebar.selectbox('',['Team Data','Matchup Data','Draft Data'])
# # # # # currentyear = datetime.now().year
# # # # # st.title('Fantasy Basketball Tool')
# # # # # leageid = st.text_input('League ID',value=145228487)
# # # # # swid = st.text_input('swid',value='{B930EA19-EB1C-47CD-B230-C9A674365B87}')
# # # # # espn_s2 = st.text_input('espn_s2',value='AECt%2FzRlxgX0ONDBmXm%2FmZnRjdEGtqr6xajwnwyH5y2r8dp%2Ff1fwHHlgNqJbjf64de9Bnq8AhxO9BFz6jJ6APzFMBuH713J1ntVm%2FB40eCqRkyPsfq8WJCbiH4AGsEaHhv4wwzW32ogMACsZZ75eZ3AgB6p2V15xy35AYP4mABywoe3tMI9tr3wBxpcpFNt%2F%2BwsMyjPrj0H5rbhPIcTW8UuoRIrjRmj87KS9gqgfZcUj15y4qcweRL%2FMFyB%2BodHrtpCk6fYJVyjSqJ2P9K1Rkvm3r1yDjMbThmILeZcI%2FoNuJw%3D%3D')
# # # # # year = st.number_input('Season',step=1,value=currentyear)
# # # # # teamlist = []
# # # # # league = League(league_id=leageid, year=year,debug=False,swid=swid,espn_s2=espn_s2)
# # # # # if page == 'Team Data':
# # # # #     playerlist = []
# # # # #     for team in league.teams:
# # # # #         teamlist.append(team.team_name)
# # # # #     selectteam = st.selectbox('Select a team', teamlist)
# # # # #     print('')
# # # # #     team = league.teams[5]
# # # # #     draft = league.player_info(name='Stephen Curry')
# # # # #     # st.write(draft)
# # # # #     for team in league.teams:
# # # # #         if team.team_name == selectteam:
# # # # #             realteam = team
# # # # #     for player in realteam.roster:
# # # # #         playerlist.append(player.name)
# # # # #     logo = realteam.logo_url
# # # # #     col1,col2 = st.columns(2)
# # # # #     with col1:
# # # # #         st.subheader(realteam.team_name)
# # # # #         st.write(f"Owner: {realteam.owners[0]['firstName']} {realteam.owners[0]['lastName']}")
# # # # #         st.write(f'Record: {realteam.wins}-{realteam.losses}-{realteam.ties}')
# # # # #         st.write(f'Standing: {realteam.standing}')

# # # # #     with col2:
# # # # #         st.image(logo,width=200)
# # # # #     selectplayer = st.selectbox('Roster', playerlist)
# # # # #     for player in realteam.roster:
# # # # #         if player.name == selectplayer:
# # # # #             realplayer = player
# # # # #     st.write(realplayer.name)
# # # # #     st.write(f'Position: {realplayer.position}')

# # # # #     st.write(f'Position Rank: {realplayer.posRank}')

# # # # #     st.write(f'Projected Average: {realplayer.projected_avg_points} Fantasy Points')
# # # # #     st.write(f'Actual Average: {realplayer.avg_points} Fantasy Points')
# # # # #     accuracy_percentage = (1 - abs((realplayer.avg_points - realplayer.projected_avg_points) / realplayer.avg_points)) * 100
# # # # #     st.write(f'Projection Accuracy: {round(accuracy_percentage, 2)}%')
# # # # #     st.write(f'Acquired by: {realplayer.acquisitionType.lower()}')

# # # # #     seasonstats = realplayer.stats[f'{currentyear}_total']
# # # # #     # st.write(league.box_scores(matchup_period=4))
# # # # #     # st.write(seasonstats['avg'])

    

# # # # #     # print(player)
# # # # #     # print(league.recent_activity(size=10))
# # # # #     # print(league.members)
# # # # # elif page == 'Draft Data':
# # # # #     st.subheader('Full Draft')
# # # # #     st.write(player for player in league.draft)
# # # # # elif page == 'Matchup Data':
# # # # #     st.subheader('Matchups')
# # # # #     box = league.box_scores()     
# # # # #     week = st.selectbox('Select a week',range(1,22))
# # # # #     matchups = league.scoreboard(week)
# # # # #     for matchup in matchups:
# # # # #         st.write(f'Home: {matchup.home_team.team_name}: {matchup.home_final_score}')
# # # # #         st.write(f'Away: {matchup.away_team.team_name}: {matchup.away_final_score}')
# # # # #         st.write(f'Winner: {matchup.winner}')
# # # # #         st.write('---')
# # # # #     for bo in box:
# # # # #         hlineup = bo.home_lineup
# # # # #         alineup = bo.away_lineup
# # # # #         co1,co2 = st.columns(2)
# # # # #         with co1:
# # # # #             with st.expander(bo.home_team.team_name + ' Player Breakdown'):
# # # # #                 # for player in hlineup:
# # # # #                 #     st.write(f'{player.name} - {player.points} PTS')
                
# # # # #                 player_names = [player.name for player in hlineup]
# # # # #                 player_points = [player.points for player in hlineup]

# # # # #                 # Create DataFrame
# # # # #                 df = pd.DataFrame({'Player': player_names, 'Points': player_points})

# # # # #                 fig = px.bar(df, x='Player', y='Points',
# # # # #                             title='Player Points',
# # # # #                             labels={'Player': 'Player Name', 'Points': 'Points'},
# # # # #                             color='Points',  # Optional: color bars based on points
# # # # #                             text='Points')  # Optional: show the points on the bars

# # # # #                 # Update layout for better visual appeal
# # # # #                 fig.update_layout(xaxis_title='Player Name',
# # # # #                                 yaxis_title='Points',
# # # # #                                 xaxis_tickangle=-45,  # Tilt x-axis labels for better readability
# # # # #                                 plot_bgcolor='white',  # Set background color to white
# # # # #                                 title_x=0.5,  # Center the title
# # # # #                                 title_font_size=20)  # Set title font size

# # # # #                 # Display the chart
# # # # #                 st.plotly_chart(fig)

# # # # #         with co2:
# # # # #             with st.expander(bo.away_team.team_name  + ' Player Breakdown'):
# # # # #                 # for player in alineup:
# # # # #                 #     st.write(f'{player.name} - {player.points} PTS')
# # # # #                 player_names = [player.name for player in hlineup]
# # # # #                 player_points = [player.points for player in hlineup]

# # # # #                 # Create DataFrame
# # # # #                 df = pd.DataFrame({'Player': player_names, 'Points': player_points})

# # # # #                 fig = px.bar(df, x='Player', y='Points',
# # # # #                             title='Player Points',
# # # # #                             labels={'Player': 'Player Name', 'Points': 'Points'},
# # # # #                             color='Points',  # Optional: color bars based on points
# # # # #                             text='Points')  # Optional: show the points on the bars

# # # # #                 # Update layout for better visual appeal
# # # # #                 fig.update_layout(xaxis_title='Player Name',
# # # # #                                 yaxis_title='Points',
# # # # #                                 xaxis_tickangle=-45,  # Tilt x-axis labels for better readability
# # # # #                                 plot_bgcolor='white',  # Set background color to white
# # # # #                                 title_x=0.5,  # Center the title
# # # # #                                 title_font_size=20)  # Set title font size

# # # # #                 # Display the chart
# # # # #                 st.plotly_chart(fig)        
# # # # game_id = '440825110'

# # # # game_url = 'https://api-secure.sports.yahoo.com/v1/editorial/s/boxscore/mlb.g.' + game_id + \
# # # #             '?lang=en-US&region=US&tz=America%2FChicago&ysp_redesign=1&mode=&v=4&ysp_enable_last_update=1&polling=1'

# # # # from matplotlib import pyplot as plt
# # # # import requests
# # # # import streamlit as st
# # # # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'}
# # # # response = requests.get(game_url, headers=headers)
# # # # game_data = response.json()

# # # # pitches = game_data['service']['boxscore']['gamepitches']['mlb.g.'+game_id]
# # # # st.write(pitches)

# # # # # print("Total number of pitches thrown during the game: " + str(len(pitches)))

# # # # import pandas as pd
# # # # pitch_df = pd.DataFrame(pitches)
# # # # transpose_pitch_df = pitch_df.transpose()
# # # # transpose_pitch_df.head()
# # # # for val in transpose_pitch_df.columns:
# # # #     transpose_pitch_df[val] = pd.to_numeric(transpose_pitch_df[val], errors='coerce')
# # # # import seaborn as sns
# # # # from bs4 import BeautifulSoup
# # # # pitcher_url = 'http://sports.yahoo.com/mlb/players/' + str(transpose_pitch_df['pitcher']['10100']) + '/'
# # # # req = requests.get(pitcher_url)
# # # # html = req.text
# # # # soup = BeautifulSoup(html, 'html.parser')
# # # # # print("On the mound to start the game: " + soup.title.string)
# # # # batter_url = 'http://sports.yahoo.com/mlb/players/' + str(transpose_pitch_df['batter']['10100']) + '/'
# # # # req = requests.get(batter_url)
# # # # html = req.text
# # # # soup = BeautifulSoup(html, 'html.parser')
# # # # # print("First batter faced: " + soup.title.string)
# # # # # pitcher_list = transpose_pitch_df.pitcher.unique()
# # # # # for pitcher in pitcher_list:
# # # # #     pitcher_url = 'http://sports.yahoo.com/mlb/players/' + str(pitcher) + '/'
# # # # #     req = requests.get(pitcher_url)
# # # # #     html = req.text
# # # # #     soup = BeautifulSoup(html, 'html.parser')
# # # # #     pitcher_info = soup.title.string
# # # # #     print(pitcher_info)
# # # # transpose_pitch_df.to_csv('yahoo.csv')
# # # # # import matplotlib.pyplot as plt
# # # # # import seaborn as sns

# # # # # # Create the scatter plot
# # # # # plt.figure(figsize=(6, 6))

# # # # # # Plot the 'Strikes/Hits/Fouls' in red
# # # # # sns.scatterplot(x=transpose_pitch_df.horizontal,
# # # # #                 y=transpose_pitch_df.vertical,
# # # # #                 color='r',
# # # # #                 marker='o',
# # # # #                 s=50,
# # # # #                 label='Strikes/Hits/Fouls',
# # # # #                 alpha=1.0)

# # # # # # Plot the 'Balls' in blue
# # # # # sns.scatterplot(x=transpose_pitch_df.horizontal,
# # # # #                 y=transpose_pitch_df.vertical,
# # # # #                 color='b',
# # # # #                 marker='o',
# # # # #                 s=50,
# # # # #                 label='Balls',
# # # # #                 alpha=1.0)

# # # # # # Set axis limits
# # # # # plt.xlim(-20000, 20000)
# # # # # plt.ylim(-20000, 20000)

# # # # # # Add a title and legend
# # # # # plt.title('Corey Kluber: World Series Game 7', fontsize=18)
# # # # # plt.legend(loc='lower right', frameon=True, shadow=True)

# # # # # # Add Data Source and Author (commented out for now)
# # # # # #plt.text(-20000, -20000, 'Data Source: Yahoo!\nAuthor: Gregory Brunner, @gregbrunn', fontsize=12)

# # # # # # Remove axis labels and tick marks if desired
# # # # # # plt.xlabel('')
# # # # # # plt.ylabel('')
# # # # # # plt.tick_params(labelbottom=False, labelleft=False)

# # # # # plt.show()

# # # # import plotly.graph_objects as go
# # # # import pandas as pd

# # # # # Sample data for demonstration purposes
# # # # # Ensure your DataFrame has 'horizontal', 'vertical', and 'z' columns
# # # # # You can replace 'z' with the actual column name you want to use for the z-axis

# # # # # Example DataFrame (you should replace this with your actual DataFrame)
# # # # # transpose_pitch_df = pd.DataFrame({
# # # # #     'horizontal': np.random.uniform(-20000, 20000, 100),
# # # # #     'vertical': np.random.uniform(-20000, 20000, 100),
# # # # #     'z': np.random.uniform(-20000, 20000, 100),
# # # # #     'type': np.random.choice(['Strikes/Hits/Fouls', 'Balls'], 100)
# # # # # })

# # # # # Create a 3D scatter plot
# # # # fig = go.Figure()

# # # # # Add traces for 'Strikes/Hits/Fouls'
# # # # fig.add_trace(go.Scatter3d(
# # # #     x=transpose_pitch_df['horizontal'],
# # # #     y=len(transpose_pitch_df)*[0],
# # # #     z=transpose_pitch_df['vertical'],
# # # #     mode='markers',
# # # #     marker=dict(size=5, color='red'),
# # # #     name='Strikes/Hits/Fouls',
# # # #     hoverinfo='text',
# # # #     # text=transpose_pitch_df[transpose_pitch_df['type'] == 'Strikes/Hits/Fouls']['type']
# # # # ))

# # # # # # Add traces for 'Balls'
# # # # # fig.add_trace(go.Scatter3d(
# # # # #     x=transpose_pitch_df[transpose_pitch_df['type'] == 'Balls']['horizontal'],
# # # # #     y=[0],
# # # # #     z=transpose_pitch_df[transpose_pitch_df['type'] == 'Balls']['vertical'],
# # # # #     mode='markers',
# # # # #     marker=dict(size=5, color='blue'),
# # # # #     name='Balls',
# # # # #     hoverinfo='text',
# # # # #     text=transpose_pitch_df[transpose_pitch_df['type'] == 'Balls']['type']
# # # # # ))

# # # # # Update layout for the 3D plot
# # # # import streamlit as st
# # # # fig.update_layout(
# # # #     title='Corey Kluber: World Series Game 7',
# # # #     scene=dict(
# # # #         xaxis_title='Horizontal Coordinate',
# # # #         yaxis_title='Vertical Coordinate',
# # # #         zaxis_title='Z Coordinate',
# # # #         xaxis=dict(range=[-20000, 20000]),
# # # #         yaxis=dict(range=[-20000, 20000]),
# # # #         zaxis=dict(range=[-20000, 20000])
# # # #     ),
# # # #     legend_title='Type'
# # # # )

# # # # # Show the plot
# # # # st.plotly_chart(fig)

# # # # from pybaseball import statcast_pitcher
# # # # from pybaseball import playerid_lookup

# # # # # find Chris Sale's player id (mlbam_key)
# # # # # playerid_lookup('hicks','jordan')

# # # # # get all available data

# # # # # get data for July 15th, 2017
# # # # data = statcast_pitcher('2024-08-24', '2024-08-24', player_id=663855)

# # # # data.to_csv('yahoo.csv')

# # # # import nflgame

# # # # games = nflgame.games(2013, week=1)
# # # # plays = nflgame.combine_plays(games)
# # # # for p in plays.sort('passing_yds').limit(5):
# # # #     print(p)
# # # import streamlit as st
# # # import sportsdataverse
# # # import sportsdataverse.nfl.nfl_pbp as nfl_pbp
# # # import pandas as pd
# # # game_id = 401547276  # Replace with your actual game ID
# # # nfl_pbp_instance = nfl_pbp.NFLPlayProcess(gameId=game_id)
# # # pbp_data = nfl_pbp_instance.espn_nfl_pbp()
# # # # for key, value in pbp_data.items():
# # # #     st.write(f"Key: {key}")
# # # #     st.write(f"Value: {value}")
# # # #     st.write()
# # # # Check if 'drives' key exists in the dictionary
# # # if 'drives' in pbp_data:
# # #     # Extract drives
# # #     drives = pbp_data['drives']
    
# # #     drives2 = drives['previous']
# # #     # plays = drives2['plays']
# # #     # import pandas as pd
# # #     # df = pd.DataFrame(plays)
# # #     # st.write(df)
# # #     # Check if drives2 is a list
# # #     if isinstance(drives2, list):
# # #         all_plays = []
        
# # #         # Iterate over each item in the list
# # #         for drive in drives2:
# # #             if isinstance(drive, dict) and 'plays' in drive:
# # #                 plays = drive['plays']
                
# # #                 # Check if 'plays' is a list of dictionaries
# # #                 if isinstance(plays, list) and all(isinstance(play, dict) for play in plays):
# # #                     all_plays.extend(plays)
        
# # #         # Convert the collected plays to a DataFrame
# # #         if all_plays:
# # #             plays_df = pd.DataFrame(all_plays)
            
# # #             # Display the DataFrame with Streamlit
# # #             st.write("All Play-by-Play Data:")
# # #             st.write(plays_df)
# # #         else:
# # #             st.write("No valid 'plays' data found in the drives2 list.")
# # #     else:
# # #         st.write("drives2 is not a list.")



# # import sportsdataverse.nfl.nfl_loaders as sdv

# # # Define the game_id you're interested in
# # game_id = 2024090801

# # # Fetch the NFL game rosters
# # nfl_df = sdv.load_nfl_rosters(seasons=range(2020,2021),return_as_pandas=True)

# # # Display the data
# # nfl_df.to_csv('yahoo.csv')

# import streamlit as st
# import plotly.express as px
# import pandas as pd
# import nfl_data_py as nfl
# import requests
# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# from random import randint
# from datetime import date
# from datetime import datetime
# current_year = datetime.now().year
# st.set_page_config(page_title="NFL Passing Analyzer",page_icon='data:image/jpeg;base64,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',layout='wide')
# def display_player_image(player_id, width2, caption2):
#     # Construct the URL for the player image using the player ID
#     image_url = f"https://a.espncdn.com/combiner/i?img=/i/headshots/nfl/players/full/{player_id}.png&w=350&h=254"
    
#     # Check if the image URL returns a successful response
#     response = requests.head(image_url)
    
#     if response.status_code == 200:
#         # If image is available, display it
#         st.markdown(
#     f'<div style="display: flex; flex-direction: column; align-items: center;">'
#     f'<img src="{image_url}" style="width: {width2}px;">'
#     f'<p style="text-align: center; font-size: 30px;">{caption2}</p>'  # Adjust font-size as needed
#     f'</div>',
#     unsafe_allow_html=True
# )
    
#         # st.image(image_url, width=width2, caption=caption2)
#     else:
#         image_url = "https://cdn.nba.com/headshots/nba/latest/1040x760/fallback.png"
#         st.markdown(
#         f'<div style="display: flex; flex-direction: column; align-items: center;">'
#         f'<img src="{image_url}" style="width: {width2}px;">'
#         f'<p style="text-align: center;">{"Image Unavailable"}</p>'
#         f'</div>',
#         unsafe_allow_html=True
#     )
#         # If image is not available, display a message


# st.markdown("""
#     <style>
#     .big-font {
#         font-size: 100px !important;
#         text-align: center;
#     }
#     </style>
#     <p class="big-font">NFL Passing Analyzer</p>
#     """, unsafe_allow_html=True)
# ids = nfl.import_ids()

# import plotly.graph_objects as go
# import numpy as np
# from sportsdataverse.nfl.nfl_loaders import load_nfl_pbp


# # Create a list of seasons
# seasons = list(range(2006, current_year + 1))

# # Set the default selection to the current year
# default_season = current_year

# # Create the selectbox
# selected_season = st.selectbox('Select a season', seasons, index=seasons.index(default_season))
# if selected_season:
#     pbp = load_nfl_pbp(seasons=selected_season,return_as_pandas=True)
#     pbp.to_csv('test.csv')


#     # Example NFL coordinates (x, y, z)
#     nfl_coordinates = [
#         (10, 20, 0),
#         (50, 25, 0),
#         (90, 30, 0),
#         (100, 40, 0),
#     ]
#     # Plot the coordinates on the field
# df = pd.read_csv('test.csv')

# df = df.dropna(subset=['name'])
# df = df[df['play_type'] == 'pass']
# df = df[~df['desc'].str.contains('sack', case=False, na=False)]

# # df['name'] = df['name'].replace('Rayne Prescott', 'Dak Prescott')
# qbs = df['passer_player_name'].unique()
# qb_name = st.selectbox('Select a quarterback', qbs)
# if qb_name:
#     # ids = ids[ids['name'] == qb_name]
#     # ids = ids[ids['position'] == 'QB']
#     # st.write(df['play_type_nfl'].unique())

#     df = df.loc[(df['name'].str.contains(qb_name))]
#     weeks = df['week'].unique()
#     weeks.sort()
#     selected_week = st.multiselect('Select a week', weeks,)
#     df = df[df['week'].isin(selected_week)]
#     yac = st.checkbox('YAC')
#     if yac:
#         length=100
#         l1=110
#         l2=100
#     else:
#         length=60
#         l1=70
#         l2=60

#     def determine_pass_type(desc):
#         if 'intercept' in desc.lower() and 'touchdown' in desc.lower():
#             return 'INTERCEPTION'
#         elif 'touchdown' in desc.lower():
#             return 'TOUCHDOWN'
#         elif 'incomplete' in desc.lower():
#             return 'INCOMPLETE'
#         elif 'intercept' in desc.lower():
#             return 'INTERCEPTION'
#         else:
#             return 'COMPLETE'  # Handle any cases that don't match

#     # Apply the function to create the new column
#     df['pass_type'] = df['desc'].apply(determine_pass_type)
#     # st.write(df)
#     passes = df['pass_type'].unique()
#     filter = st.multiselect('Filter by:', passes,default=passes)
#     df = df[df['pass_type'].isin(filter)]
#     # df['team1'] = 'home'
#     # game_shots_df = df
#     # nfl2 = nfl.import_ngs_data(stat_type='passing',years=range(selected_season,selected_season+1))
#     # nfl2 = nfl2[nfl2['player_display_name'] == qb_name]
#     # nfl2 = nfl2[nfl2['season'] == selected_season]
#     # nfl2 = nfl2[nfl2['week'].isin(selected_week)]
#     # complete_count = nfl2['completions'].sum()
#     # interception_count = nfl2['interceptions'].sum()
#     # touchdown_count = nfl2['pass_touchdowns'].sum()
#     # total_passes = nfl2['attempts'].sum()
#     # yards = nfl2['pass_yards'].sum()



#     def draw_football_field(length,l1,l2):
#         # Define the field dimensions
#         field_length = 120  # 100 yards + 2 end zones of 10 yards each
#         field_width = 53.33  # 53.33 yards wide (160 feet)
        
#         # Create the field as a filled rectangle
#         field_x = [0, field_length, field_length, 0, 0]
#         field_y = [0, 0, field_width, field_width, 0]
#         field_z = [0, 0, 0, 0, 0]


#         # fig = px.line_3d(
#         #     data_frame=court_lines_df,
#         #     x='x',
#         #     y='y',
#         #     z='z',
#         #     line_group='line_group',
#         #     color='color',
#         #     color_discrete_map={
#         #         'court': 'rgba(0,0,0,0)',
#         #         'hoop': '#e47041'
#         #     }
#         # )
#             # Add horizontal lines
#         for i in range(10,l1,10):
#             fig.add_trace(go.Scatter3d(
#                 x=[25],  # X position for the annotation
#                 y=[i],  # Y position for the annotation
#                 z=[0],  # Z position for the annotation, slightly above the field
#                 mode='text',
#                 text=[f'+{i}'],  # Text for the annotation
#                 textposition='top center',  # Adjusted position for better visibility
#                 textfont=dict(size=20, color='gold'),  # Font size and color
#                 showlegend=False,
#                 hoverinfo='none'
#             ))
#             fig.add_trace(go.Scatter3d(
#                 x=[-25],  # X position for the annotation
#                 y=[i],  # Y position for the annotation
#                 z=[0],  # Z position for the annotation, slightly above the field
#                 mode='text',
#                 text=[f'+{i}'],  # Text for the annotation
#                 textposition='top center',  # Adjusted position for better visibility
#                 textfont=dict(size=20, color='gold'),  # Font size and color
#                 showlegend=False,
#                 hoverinfo='none'
#             ))
#         for i in range(-10, l2, 5):

#             fig.add_trace(go.Scatter3d(
#                 x=[-field_width/2, field_width/2],
#                 y=[i, i],
#                 z=[0, 0],
#                 mode='lines',
#                 line=dict(color=linecol, width=1.5, dash='solid'),
#                 showlegend=False,
#                 hoverinfo='none'
#             ))
        
#         # # Add thicker horizontal lines

#         for i in range(-10, l2, 10):

#             fig.add_trace(go.Scatter3d(
#                 x=[-field_width/2, field_width/2],
#                 y=[i, i],
#                 z=[0, 0],
#                 mode='lines',
#                 line=dict(color=linecol, width=4, dash='solid'),
#                 showlegend=False,
#                 hoverinfo='none'
#             ))
#         # Add annotations for vertical hash marks
#         for j in range(-15, l2, 1):
#             fig.add_trace(go.Scatter3d(
#                 x=[-3.1, 3.1],
#                 y=[j, j],
#                 z=[0, 0],
#                 mode='text',
#                 marker=dict(size=0, color=linecol),
#                 text=['-', '-'],
#                 textposition='top center',
#                 showlegend=False,
#                 hoverinfo='none'
#             ))
#             if j <= 0:
#                 sign = ''
#             else:
#                 sign = '+'
#             fig.add_trace(go.Scatter3d(
#                 x=[-26.5, 26.5],
#                 y=[j,j],
#                 z=[0, 0],
#                 mode='text',
#                 marker=dict(size=0, color=linecol),
#                 text=['-', '-'],
#                 # textposition='top center',
#                 showlegend=False,
#                 hoverinfo='text',
#                 hovertext=sign + str(j)
#             ))
#         # fig.add_trace(go.Scatter3d(
#         #     x=[0, 0],
#         #     y=[-8, -8],
#         #     z=[1, 1],
#         #     mode='markers',
#         #     marker=dict(size=10, color='#4E3A2A'),
#         #     hoverinfo='text',
#         #     hovertext='QB'


#         # ))
    
#         fig.add_trace(go.Scatter3d(
#             x=[-field_width/2, field_width/2],
#                 y=[0, 0],
#                 z=[0, 0],
#                 mode='lines',
#                 line=dict(color='gold', width=4, dash='solid'),
#                 showlegend=False,
#                 hoverinfo='text',
#                 hovertext='Line of Scrimmage'
#         ))



#         return fig

#     df2 = df


#     # df2 = df2.head(50)
#     # dfg = dfg.head(50)
#     df2['z'] = 0
#     # dfg['z'] = 0
#     x_values = []
#     y_values = []
#     z_values = []
#     yac_values = []
#     # Loop through each row in the 'location' column
#     # for loc_list in df2['location']:
#     #     for coord in loc_list:
#     #         x = loc_list[0]
#     #         y=loc_list[1]
#     #         x_values.append(x)
#     #         y_values.append(y)
#     #         z_values.append(0)
#     for index, row in df2.iterrows():
        
#         if row['pass_location'] == 'left':
#             x_values.append(randint(-26,-14))
#         elif row['pass_location'] == 'middle':
#             x_values.append(randint(-8,8))
#         else: 
#             x_values.append(randint(14,26))
#         # Append the value from column 'x' to the list
#         y_values.append(row['air_yards'])
#         z_values.append(0)
#         yac_values.append(row['yards_after_catch'])



#     x_values2 = []
#     y_values2 = []
#     z_values2 = []
#     random = st.checkbox('Random QB Locations')
#     for index, row in df2.iterrows():
#         # Append the value from column 'x' to the list
#         if random:
#             if abs(row['air_yards']) < 5:
#                 x_values2.append(randint(-5,5))
#             else:
#                 x_values2.append(randint(-7,7))

#             y_values2.append(randint(-8,-5))
#             z_values2.append(0)
#         else:
#             x_values2.append(0)
#             y_values2.append(-8)
#             z_values2.append(0)

#     # else:
#     #     for index, row in df2.iterrows():
#     #         # Append the value from column 'x' to the list
            
#     #         x_values2.append(x_coordinate)

#     #         y_values2.append(y_coordinate)
#     #         z_values2.append(2.5)
#     # # Loop through each row in the 'location' column

#     colortype = st.selectbox('Color Scheme',['Completion/Incompletion','Week','Team Colors'])
#     fieldtype = st.selectbox('Field Type',['NextGen','Grass'])
#     if fieldtype == 'Grass':
#         fieldcol = 'green'
#         linecol = 'white'
#         qbcol = '#4E3A2A'
#     else:
#         fieldcol = '#2C2C2C'
#         linecol = 'grey'
#         qbcol = 'gold'

#     import numpy as np
#     import plotly.graph_objects as go
#     import streamlit as st
#     import math
#     def calculate_distance(x1, y1, x2, y2):
#         """Calculate the distance between two points (x1, y1) and (x2, y2)."""
#         return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#     def generate_arc_points(p1, p2, apex, num_points=100):
#         """Generate points on a quadratic Bezier curve (arc) between p1 and p2 with an apex."""
#         t = np.linspace(0, 1, num_points)
#         x = (1 - t)**2 * p1[0] + 2 * (1 - t) * t * apex[0] + t**2 * p2[0]
#         y = (1 - t)**2 * p1[1] + 2 * (1 - t) * t * apex[1] + t**2 * p2[1]
#         z = (1 - t)**2 * p1[2] + 2 * (1 - t) * t * apex[2] + t**2 * p2[2]
#         return x, y, z

#     # Example lists of x and y coordinates
#     x_coords = x_values
#     y_coords = y_values
#     z_value = 0  # Fixed z value
#     x_coords2 = x_values2
#     y_coords2 = y_values2

#     # Create figure
#     fig = go.Figure()
#     # fig = draw_football_field()

#     # Loop through pairs of points to create arcs
#     colors = df['pass_type'].apply(
#             lambda pt: 'blue' if pt == 'TOUCHDOWN' else (
#                 '#39FF14' if pt == 'COMPLETE' else (
#                     'red' if pt == 'INTERCEPTION' else 'white'
#                 )
#             )
#         ).tolist() 
#     color_dict = {
#         "ARI": ["#97233F", "#000000"],  # Arizona Cardinals
#         "ATL": ["#A71930", "#000000", "#A5ACAF"],  # Atlanta Falcons
#         "BAL": ["#241773", "#000000", "#9E7C0C"],  # Baltimore Ravens
#         "BUF": ["#00338D", "#C60C30"],  # Buffalo Bills
#         "CAR": ["#0085CA", "#101820", "#A5ACAF", "#BFC0BF"],  # Carolina Panthers
#         "CHI": ["#0B162A", "#C83803", "#DD4814", "#FFFFFF"],  # Chicago Bears
#         "CIN": ["#FB4F14", "#000000", "#FFFFFF"],  # Cincinnati Bengals
#         "CLE": ["#311D00", "#FF3C00", "#FFFFFF"],  # Cleveland Browns
#         "DAL": ["#041E42", "#869397", "#FFFFFF"],  # Dallas Cowboys
#         "DEN": ["#FB4F14", "#002244", "#FFFFFF"],  # Denver Broncos
#         "DET": ["#0076B6", "#B0B7BC", "#FFFFFF"],  # Detroit Lions
#         "GB": ["#203731", "#FFB81C"],  # Green Bay Packers
#         "HOU": ["#03202F", "#A71930", "#FFFFFF"],  # Houston Texans
#         "IND": ["#002C5F", "#A5ACAF", "#FFFFFF"],  # Indianapolis Colts
#         "JAC": ["#101820", "#006778", "#D7A22A", "#9F792C", "#FFFFFF"],  # Jacksonville Jaguars
#         "KC": ["#E31837", "#FFB81C"],  # Kansas City Chiefs
#         "LV": ["#000000", "#A5ACAF", "#FFFFFF"],  # Las Vegas Raiders
#         "LAC": ["#0072CE", "#FFB81C", "#002244", "#FFFFFF"],  # Los Angeles Chargers
#         "LAR": ["#002244", "#FFFFFF", "#B3995D"],  # Los Angeles Rams
#         "MIA": ["#008E97", "#F58220", "#FFFFFF", "#005778"],  # Miami Dolphins
#         "MIN": ["#4F2683", "#FFC62F", "#FFFFFF"],  # Minnesota Vikings
#         "NE": ["#002244", "#C60C30", "#B0B7BC", "#FFFFFF"],  # New England Patriots
#         "NO": ["#D3BC8D", "#000000"],  # New Orleans Saints
#         "NYJ": ["#203731", "#FFFFFF"],  # New York Jets
#         "PHI": ["#004C54", "#A5ACAF", "#FFFFFF"],  # Philadelphia Eagles
#         "PIT": ["#FFB81C", "#101820"],  # Pittsburgh Steelers
#         "SF": ["#AA0000", "#B3995D", "#FFFFFF"],  # San Francisco 49ers
#         "SEA": ["#002244", "#69BE28", "#A5ACAF", "#FFFFFF"],  # Seattle Seahawks
#         "TB": ["#D50A0A", "#34302B", "#FF7900", "#FFFFFF"],  # Tampa Bay Buccaneers
#         "TEN": ["#0C2340", "#4B92DB", "#FFFFFF"],  # Tennessee Titans
#         "WAS": ["#773141", "#FFB612", "#FFFFFF"]  # Washington Commanders
#     }

#     def get_color2(pass_type, colors):
#         if pass_type == 'TOUCHDOWN':
#             return colors[0]  # First color
#         elif pass_type in ['INTERCEPTION', 'INCOMPLETE']:
#             return colors[1]  # Second color
#         else:
#             return colors[0]  # Default to first colo   
#     import random

#     # Function to generate a random color in hex format
#     def random_color():
#         return "#{:06x}".format(random.randint(0, 0xFFFFFF))
#     unique_weeks = df2['week'].unique()
#     week_to_color = {week: random_color() for week in unique_weeks}
#     def get_color(row):
#         week_color = week_to_color[week]
#         return week_color 
#     passes = df2['desc'].tolist()
#     ys = df2['air_yards'].tolist()
#     yacs = df2['yards_after_catch'].tolist()
#     weeks = df2['week'].tolist()
#     teams = df2['defteam'].tolist()
#     hovertext = [
# f'{pt}<br>{round(y_value, 2)} Air Yards<br>Week: {week}<br>Opponent: {team}'
# for pt, y_value, week, team in zip(passes, ys, weeks, teams)
# ]
#     hovertext2 = [
#     f'{pt}<br>{round(y_value, 2)} YAC<br>Week: {week}<br>Opponent: {team}'
#     for pt, y_value, week, team in zip(passes, yacs, weeks, teams)
#     ]
#     for i in range(len(df2)):
#         if df2['pass_type'].iloc[i] == 'TOUCHDOWN':
#             col = 'blue'
#         elif df2['pass_type'].iloc[i] == 'INTERCEPTION':
#             col = 'red'
#         elif df2['pass_type'].iloc[i] == 'INCOMPLETE':
#             col = 'white'
#         else: 
#             col = '#39FF14'
#         week = df2['week'].iloc[i]
#         week = df2['week'].iloc[i]
#         col3 = get_color(week)
#         col2 = get_color2(df2['pass_type'].iloc[i], color_dict[df2['posteam'].iloc[i]])
#         x1 = x_coords[i]
#         y1 = y_coords[i]
#         x2 = x_coords2[i]
#         y2 = y_coords2[i]
#         z_value2 = 0
#         # Define the start and end points
#         p2 = np.array([x1, y1, z_value])
#         p1 = np.array([x2, y2, z_value2])
        
#         # Apex will be above the line connecting p1 and p2
#         distance = calculate_distance(x1, y1, x2, y2)
#         if distance > 50:
#             h = randint(28,33)
#         elif distance > 40:
#             h = randint(24,27)
#         elif distance > 30:
#             h = randint(21,22)
#         elif distance > 20:
#             h = randint(14, 15)
#         elif distance > 10:
#             h = 12
#         else: 
#             h = 11.5
#         if distance < 10:
#             h = distance
#         apex = np.array([0.5 * (x1 + x2), 0.5 * (y1 + y2), h])  # Adjust apex height as needed
        
#         # Generate arc points
#         x, y, z = generate_arc_points(p1, p2, apex)
        
#         # Add arc trace
#         if colortype == 'Completion/Incompletion':
#             realcol = col
#         elif colortype == 'Team Colors':
#             realcol = col2
#         else:
#             realcol = col3
#         fig.add_trace(go.Scatter3d(
#             x=x, y=y, z=z,
#             mode='lines',
#             line=dict(width=10,color=realcol),
#             name=f'Arc {i + 1}',
#             opacity = 0.5,
#             hoverinfo='text',
#             hovertext=hovertext[i]  # Provide hovertext as a list
#         ))
        
#         # Add start and end points
#         fig.add_trace(go.Scatter3d(
#             x=[p2[0], p2[0]],
#             y=[p2[1], p2[1]],
#             z=[p2[2], p2[2]],
#             mode='markers',
#             marker=dict(size=8, symbol='circle-open',color=col),
#             name=f'Endpoints {i + 1}',
#             hoverinfo='text',
#             hovertext=hovertext[i]  # Provide hovertext as a list
#         ))
#         fig.add_trace(go.Scatter3d(
#             x=[p2[0], p2[0]],
#             y=[p2[1], p2[1]],
#             z=[p2[2], p2[2]],
#             mode='markers',
#             marker=dict(size=5, symbol='circle',color=col),
#             name=f'Endpoints {i + 1}',
#             hoverinfo='text',
#             hovertext=hovertext[i]  # Provide hovertext as a list
#         ))
#         if yac:
#             # Extract the necessary values for the current trace
#             x_values2 = [x_values[i], x_values[i]]  # x remains the same
#             y_values2 = [ys[i], ys[i]+yac_values[i]]      # y changes from air to yac2
#             z_values2 = [0, 0]                      # Define start and end z values
        
#             # Add the trace to the figure
#             fig.add_trace(go.Scatter3d(
#                 x=x_values2,
#                 y=y_values2,
#                 z=z_values2,
#                 mode='lines',
#                 line=dict(width=10, color=realcol,dash='dash'),
#                 name=f'Arc {i + 1}',
#                 opacity=1,
#                 hoverinfo='text',
#                 hovertext=hovertext2[i]  # Provide hovertext as a list
#             ))

#     # Update layout
#     fig.update_layout(
#         title='3D Arcs Plot',
#         scene=dict(
#             xaxis_title='X',
#             yaxis_title='Y',
#             zaxis_title='Z'
#         )
#     )
#     fig = draw_football_field(length,l1,l2)
#     fig.update_layout(
#         margin=dict(l=20, r=20, t=20, b=20),
#             scene_aspectmode="data",
#             height=800,
#             scene_camera=dict(
#                 eye=dict(x=1.3, y=0, z=0.7)
#             ),
#         scene=dict(
#             xaxis=dict(
#                 title='',
#                 range=(-53.3333/2, 53.3333/2),
#                 showticklabels=False,
#                 showgrid=False,

#     # Set the range for the x-axis
#             ),
#             yaxis=dict(
#                 title='',
#                 range=[-15,length] ,
#                 showticklabels=False,
#                 showgrid=False,
#     # Set the range for the y-axis
#             ),
#             zaxis=dict(
#                 title='',
#                 range=[0, 18],
#                 showbackground=True,
#                     backgroundcolor=fieldcol,
#                     showticklabels=False,
#                     showgrid=False,
#     # Set the range for the z-axis
#             )
#         ),
#             legend=dict(
#                 yanchor='bottom',
#                 y=0.05,
#                 x=0.2,
#                 xanchor='left',
#                 orientation='h',
#                 font=dict(size=15, color='black'),
#                 bgcolor='white',
#                 title='',
#                 itemsizing='constant'
#             ),
#             legend_traceorder="reversed",
#             showlegend=False
#         )


#     # Show plot
#     # st.write(df2)

#     # st.plotly_chart(fig,use_container_width=True)




#     # # Show the plot
#     weekstr = ''
#     for week in selected_week:
#         weekstr += str(week) + ', '
#     weekstr = weekstr[:-2]
#     if len(selected_week) > 1:
#         typeweek = 'Weeks:'
#     else:
#         typeweek = 'Week:'
#     st.subheader(f'{qb_name} Passing Chart')
#     # id = int(ids['espn_id'])
#     # if id:
#     #     display_player_image(id,500,f'{qb_name}')
#     st.subheader(f'Season: {selected_season}')
#     st.subheader(f'{typeweek} {weekstr}')

#     st.plotly_chart(fig,use_container_width=True)
        


                                
#     # Create a list of metrics
#     metrics = [
#         'avg_time_to_throw',
#         'avg_completed_air_yards',
#         'avg_intended_air_yards',
#         'avg_air_yards_differential',
#         'aggressiveness',
#         'max_completed_air_distance',
#         'avg_air_yards_to_sticks',
#         'attempts',
#         'pass_yards',
#         'pass_touchdowns',
#         'interceptions',
#         'passer_rating',
#         'completions',
#         'completion_percentage',
#         'expected_completion_percentage',
#         'completion_percentage_above_expectation',
#         'avg_air_distance',
#         'max_air_distance'
#     ]

#     # Dropdown for selecting metric

#     # Show plot in Streamlit
#     # Create the histogram plot
#     fig, ax = plt.subplots()
#     sns.histplot(df['air_yards'], kde=False, ax=ax)

#     # Add labels and title if needed
#     ax.set_xlabel('Air Yards')
#     ax.set_ylabel('Frequency')
#     ax.set_title('Distribution of Air Yards')
#     col1, col2 = st.columns(2)
#     # Show the plot in Streamlit
#     with col1:
#         st.plotly_chart(fig)

#     plt.style.use('dark_background')

#     # Set up our subplots
#     fig, (ax1, ax2) =plt.subplots(1,2)


#     qb = df

#     # What we've added here is shading for the densities, but leaving the lowest density area unshaded.
#     # I've also added the *n_level* parameter, which allows us to choose how many levels we want to have in our contour. The higher the number here, the smoother the plot will look.
#     sns.kdeplot(x=x_values, y=y_values, ax=ax1, cmap='gist_heat', shade=True, shade_lowest=False, n_levels=10)

#     #Set title, remove ticks and labels
#     ax1.set_xlabel('')
#     ax1.set_xticks([])

#     ax1.set_yticks([])

#     ax1.set_ylabel('')

#     #Remove any part of the plot that is out of bounds
#     ax1.set_xlim(-53.3333/2, 53.3333/2)

#     ax1.set_ylim(-15,60)
#     #This makes our scales (x and y) equal (1 pixel in the x direction is the same 'distance' in coordinates as 1 pixel in the y direction)




#     #Plot all of the field markings (line of scrimmage, hash marks, etc.)

#     for j in range(-15,60-1,1):
#         ax1.annotate('--', (-3.1,j-0.5),
#                      ha='center',fontsize =10)
#         ax1.annotate('--', (3.1,j-0.5),
#                      ha='center',fontsize =10)
        
#     for i in range(-10,60,5):
#         ax1.axhline(i,c='w',ls='-',alpha=0.7, lw=1.5)
        
#     for i in range(-10,60,10):
#         ax1.axhline(i,c='w',ls='-',alpha=1, lw=1.5)
        
#     for i in range(10,60-1,10):
#         ax1.annotate(str(i), (-12.88,i-1.15),
#                 ha='center',fontsize =15,
#                     rotation=270)
        
#         ax1.annotate(str(i), (12.88,i-0.65),
#                 ha='center',fontsize =15,
#                     rotation=90)
#     sns.scatterplot(x=x_values, y=y_values, ax=ax2)

#     ax2.set_xlabel('')
#     ax2.set_ylabel('')
#     ax2.set_xticks([])

#     ax2.set_yticks([])

#     ax2.set_xlim(-53.3333/2, 53.3333/2)

#     ax2.set_ylim(-15,60)

#     for j in range(-15,60,1):
#         ax2.annotate('--', (-3.1,j-0.5),
#                      ha='center',fontsize =10)
#         ax2.annotate('--', (3.1,j-0.5),
#                      ha='center',fontsize =10)
        
#     for i in range(-10,60,5):
#         ax2.axhline(i,c='w',ls='-',alpha=0.7, lw=1.5)
        
#     for i in range(-10,60,10):
#         ax2.axhline(i,c='w',ls='-',alpha=1, lw=1.5)
        
#     for i in range(10,60-1,10):
#         ax2.annotate(str(i), (-12.88,i-1.15),
#                 ha='center',fontsize =15,
#                     rotation=270)
        
#         ax2.annotate(str(i), (12.88,i-0.65),
#                 ha='center',fontsize =15,
#                     rotation=90)

#     with col2:
#         st.pyplot(fig)
#     # with coli2:
#     #     selected_metric = st.selectbox('Select Metric', metrics)

#     # # Plotly bar graph
#     #     fig2 = px.bar(
#     #     nfl2,
#     #     x='week',
#     #     y=selected_metric,
#     #     title=f'Weekly Statistics for {selected_metric.replace("_", " ").title()}',
#     #     labels={'week': 'Week', selected_metric: selected_metric.replace("_", " ").title()},
#     #     template='plotly_dark'
#     #     )

#     #     st.plotly_chart(fig2)



from statsbombpy import sb
import plotly.graph_objects as go
import numpy as np
import streamlit as st
import numpy as np
import pandas as pd
import json
import streamlit as st
import unicodedata
from matplotlib import pyplot as plt
from FCPython import createPitch
import requests
from random import randint
# Create pitch plot
import math
import plotly.express as px

st.set_page_config(page_title="Soccer 3D Visualizer",page_icon='⚽',layout='wide')
st.markdown("""
    <style>
    .big-font {
        font-size: 100px !important;
        text-align: center;
    }
    </style>
    <p class="big-font">Soccer 3D Visualizer</p>
    """, unsafe_allow_html=True)

st.sidebar.write('View multiple 3D maps such as shot maps, passing maps, receiving maps, pressure maps. Data from Statsbomb API. Inspired by the work of Andrii Gozhulovskyi')

def create_pitch_3d():
    # Create figure
    fig = go.Figure()

    # Define scaling factor
    scale_factor = 1

    # Scaled pitch dimensions
    pitch_length = 120 * scale_factor
    pitch_width = 80 * scale_factor

    # Plot pitch outline & centre line
    fig.add_trace(go.Scatter3d(x=[0, 0, pitch_length, pitch_length, 0, pitch_length / 2, pitch_length / 2], 
                               y=[0, pitch_width, pitch_width, 0, 0, 0, pitch_width],
                               z=[0]*7,
                               mode='lines',
                               line=dict(color='white', width=4 * scale_factor), hoverinfo='none'))
    
    # Left Penalty Area
    fig.add_trace(go.Scatter3d(x=[16.5 * scale_factor, 16.5 * scale_factor, 0, 16.5 * scale_factor], 
                               y=[60 * scale_factor, 20 * scale_factor, 20 * scale_factor, 20 * scale_factor],
                               z=[0, 0, 0, 0],
                               mode='lines',
                               line=dict(color='white', width=4 * scale_factor), hoverinfo='none'))
    fig.add_trace(go.Scatter3d(x=[16.5 * scale_factor, 0], 
                               y=[60 * scale_factor, 60 * scale_factor],
                               z=[0, 0],
                               mode='lines',
                               line=dict(color='white', width=4 * scale_factor), hoverinfo='none'))
    
    # Right Penalty Area
    fig.add_trace(go.Scatter3d(x=[pitch_length, (120 - 16.5) * scale_factor, (120 - 16.5) * scale_factor, pitch_length], 
                               y=[60 * scale_factor, 60 * scale_factor, 20 * scale_factor, 20 * scale_factor],
                               z=[0, 0, 0, 0],
                               mode='lines',
                               line=dict(color='white', width=4 * scale_factor), hoverinfo='none'))
    
    # Left 6-yard Box
    fig.add_trace(go.Scatter3d(x=[0, 5.5 * scale_factor, 5.5 * scale_factor, 0.5 * scale_factor, 0], 
                               y=[49 * scale_factor, 49 * scale_factor, 31 * scale_factor, 31 * scale_factor, 49 * scale_factor],
                               z=[0, 0, 0, 0, 0],
                               mode='lines',
                               line=dict(color='white', width=4 * scale_factor), hoverinfo='none'))
    
    # Right 6-yard Box
    fig.add_trace(go.Scatter3d(x=[pitch_length, (120 - 5.5) * scale_factor, (120 - 5.5) * scale_factor, pitch_length], 
                               y=[49 * scale_factor, 49 * scale_factor, 31 * scale_factor, 31 * scale_factor],
                               z=[0, 0, 0, 0],
                               mode='lines',
                               line=dict(color='white', width=4 * scale_factor), hoverinfo='none'))
    
    # Draw Circles
    def add_circle(x_center, y_center, z_center, radius, name):
        theta = np.linspace(0, 2 * np.pi, 100)
        x = x_center + radius * np.cos(theta)
        y = y_center + radius * np.sin(theta)
        z = z_center * np.ones_like(x)
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', name=name, line=dict(color='white', width=4 * scale_factor), hoverinfo='none'))

    add_circle(pitch_length / 2, pitch_width / 2, 0, 9.15 * scale_factor, 'Centre Circle')
    add_circle(pitch_length / 2, pitch_width / 2, 0, 0.8 * scale_factor, 'Centre Spot')
    add_circle(11 * scale_factor, (pitch_width / 2), 0, 0.8 * scale_factor, 'Left Penalty Spot')
    add_circle((120 - 11) * scale_factor, (pitch_width / 2), 0, 0.8 * scale_factor, 'Right Penalty Spot')

    # Draw Arcs
    def add_arc(x_center, y_center, z_center, radius, theta1, theta2, name):
        theta = np.linspace(np.deg2rad(theta1), np.deg2rad(theta2), 100)
        x = x_center + radius * np.cos(theta)  # Flip around the Y-axis
        y = y_center + radius * np.sin(theta)
        z = z_center * np.ones_like(x)
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', name=name, line=dict(color='white', width=4 * scale_factor)))
    def add_arc2(x_center, y_center, z_center, radius, theta1, theta2, name):
        theta = np.linspace(np.deg2rad(theta1), np.deg2rad(theta2), 100)
        x = x_center - radius * np.cos(theta)  # Flip around the Y-axis
        y = y_center + radius * np.sin(theta)
        z = z_center * np.ones_like(x)
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', name=name, line=dict(color='white', width=4 * scale_factor)))
    draw_goals(fig,'home')
    draw_goals(fig,'away')
    


    
    



        # Example arcs (you can uncomment and adjust as needed)
    add_arc2(11 * scale_factor, (pitch_width / 2), 0, 18.3 / 2 * scale_factor, 234, 126, 'Left Arc')
    add_arc((120 - 11) * scale_factor, (pitch_width / 2), 0, 18.3 / 2 * scale_factor, 128, 232, 'Right Arc')
    def add_arc3(x_center, y_center, z_center, radius, angle_start, angle_end, name):
        theta = np.linspace(np.deg2rad(angle_start), np.deg2rad(angle_end), 100)
        x = x_center + radius * np.cos(theta)
        y = y_center + radius * np.sin(theta)
        z = z_center * np.ones_like(x)
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', name=name, line=dict(color='white', width=4 * scale_factor), hoverinfo='none'))

    arc_radius = 4 * scale_factor
    # Bottom-left corner
    add_arc3(arc_radius, arc_radius, 0, arc_radius, 180, 270, 'Bottom-left Arc')
    # Bottom-right corner
    add_arc3(pitch_length - arc_radius, arc_radius, 0, arc_radius, 270, 360, 'Bottom-right Arc')
    # Top-left corner
    add_arc3(arc_radius, pitch_width - arc_radius, 0, arc_radius, 90, 180, 'Top-left Arc')
    # Top-right corner
    add_arc3(pitch_length - arc_radius, pitch_width - arc_radius, 0, arc_radius, 0, 90, 'Top-right Arc')

        # Set axis
    fig.update_layout(scene=dict(
        xaxis=dict(
            range=[-5, pitch_length+5],
            title='',
            showgrid=False,        # Turn off grid
            showline=False,        # Turn off axis line
            showticklabels=False,  # Turn off tick labels
            zeroline=False,        # Turn off the zero line
        ),
        yaxis=dict(
            range=[-5, pitch_width+5],
            title='',
            showgrid=False,        # Turn off grid
            showline=False,        # Turn off axis line
            showticklabels=False,  # Turn off tick labels
            zeroline=False,        # Turn off the zero line
        ),
        zaxis=dict(
            # range=[0, 1],
            title='',
            showgrid=False,        # Turn off grid
            showline=False,        # Turn off axis line
            showticklabels=False,  # Turn off tick labels
            zeroline=False,        # Turn off the zero line
            showbackground=True,   # Optionally keep the background
            backgroundcolor='green'
        ),
        # aspectmode='data',
        # aspectratio=dict(x=2, y=1.4, z=0.2),  # Adjust aspect ratio if needed
    ), showlegend=False,
     margin=dict(l=20, r=20, t=20, b=20),
            scene_aspectmode="data",
            height=800,
            scene_camera=dict(
                eye=dict(x=0, y=3, z=0.7)
            ),)
    
    return fig

def get_event_dict(df, chosen_timestamp):
    timestamp_events = df[df['timestring']==chosen_timestamp]
    timestamp_events = timestamp_events[timestamp_events['visible_area'].notna()]

    timestamp_events['event_tag'] = timestamp_events['player'] + ': ' + timestamp_events['type']
    event_dict = dict(zip(timestamp_events['event_tag'], timestamp_events['id']))
    event_dict = {k: v for k, v in event_dict.items() if not pd.isna(k)}
    return event_dict
from scipy.spatial import Voronoi, voronoi_plot_2d

def compute_voronoi(player_locations):
    # Create Voronoi diagram
    vor = Voronoi(player_locations)
    
    # Collect vertices for each region
    regions = []
    for region in vor.regions:
        if len(region) > 0 and -1 not in region:  # Exclude empty regions and those with infinity
            regions.append(vor.vertices[region])
    return regions

def create_3d_plot(df, event_dict, chosen_timestamp, displayed_event, voronoi,fig):
    home_color = 'red'
    away_color = 'blue'

    # Filter data for the selected timestamp and event
    frame = df[(df['timestring'] == chosen_timestamp) & (df['id'] == event_dict[displayed_event])]
    visible_area = np.array(frame.iloc[0].visible_area).reshape(-1, 2)

    # # Create 3D figure

    # Collect player locations for Voronoi computation
    player_locations = []
    for _, row in frame.iterrows():
        player_locations.append(row['player_location'])

    player_locations = np.array(player_locations)

    # Compute Voronoi polygons if required
    if voronoi:
        fig.add_trace(go.Mesh3d(
        x=visible_area[:, 0],
        y=visible_area[:, 1],
        z=[0] * len(visible_area),  # Set z-coordinate for the polygon
        color='darkgray',  # You can change this color
        opacity=0.5,
        name='Visible Area',
        hoverinfo='none'
    ))

    
    for _, row in frame.iterrows():
        if row['team'] == team_1:
            color = home_color if row['teammate'] else away_color
        elif row['team'] == team_2:
            color = away_color if row['teammate'] else home_color
        marker = 'diamond' if row['keeper'] else 'cross' if row['actor'] else 'circle'
        size = 15 if row['keeper'] else 15 if row['actor'] else 7
        hover = 'Goalkeeper' if row['keeper'] else 'Other Players' if not row['actor'] else row['player']
        fig.add_trace(go.Scatter3d(
            x=[row['player_location'][0]],
            y=[row['player_location'][1]],
            z=[0],  # Set z to 0 for ground level
            mode='markers',
            marker=dict(color=color, size=size, symbol=marker),
            name=f"{row['player']} ({row['team']})",
            hoverinfo='text',
            hovertext= hover
        ))

    # Annotate the event
    row = df[df['id'] == event_dict[displayed_event]].iloc[0]
    

    # Add arrows for Carries and Lines for Passes/Shots
    if row['type'] == 'Carry':
        color = home_color if row['teammate'] else away_color
        fig.add_trace(go.Scatter3d(
            x=[row["location"][0], row['carry_end_location'][0]],
            y=[row["location"][1], row['carry_end_location'][1]],
            z=[0, 0],
            mode='lines',
            line=dict(color=color, width=5,dash='dash'),
            name='Carry',
            hoverinfo='none'
        ))
    elif row['type'] == 'Pass':
        color = home_color if row['teammate'] else away_color
        end_location = row[f'{row["type"].lower()}_end_location']
        if row['pass_height'] == 'Ground Pass':
            fig.add_trace(go.Scatter3d(
                x=[row["location"][0], end_location[0]],
                y=[row["location"][1], end_location[1]],
                z=[0, 0],
                mode='lines',
                line=dict(color=color, width=5),
                name=row["type"],
                hoverinfo='text',
                hovertext=row['type']
            ))
        else:
            p1 = np.array([row["location"][0], row["location"][1], 0])
            p2 = np.array([end_location[0], end_location[1], 0])
            
            # Apex will be above the line connecting p1 and p2
            distance = calculate_distance(row["location"][0], row["location"][1], end_location[0], end_location[1])
            if distance > 50:
                h = 4*(randint(23,24)-20)
            elif distance > 40:
                h = 4*(randint(20,21)-20)
            elif distance > 30:
                h = 4*(randint(16,17)-15)
            elif distance > 20:
                h = 4*(randint(10, 11)-10)
            elif distance > 10:
                h = 4*(7-6)
            else: 
                h = 4*(0.5)
            apex = np.array([0.5 * (row["location"][0] + end_location[0]), 0.5 * (row["location"][1] + end_location[1]), h])  # Adjust apex height as needed
            
            # Generate arc points
            x, y, z = generate_arc_points(p1, p2, apex)
            
            # Add arc trace
            fig.add_trace(go.Scatter3d(
                x=x, y=y, z=z,
                mode='lines',
                line=dict(width=5,color=color),
                name=f'Arc',
                hoverinfo='none',
            ))
    elif row['type'] == 'Shot':
        z2 = row['shot_end_location'][2] if len(row['shot_end_location']) > 2 else 0
        if z2 > 0:  # Only create curves for shots where z2 is greater than 0
            x_curve, y_curve, z_curve = generate_smooth_curve(row['location'][0], row['shot_end_location'][0], 80-row['location'][1], 80-row['shot_end_location'][1], z2)
            
            fig.add_trace(go.Scatter3d(
                x=x_curve,
                y=y_curve,
                z=z_curve,
                mode='lines',
                line=dict(color=color, width=5),  # Change color if needed
                name='Shot Trajectory',
                hoverinfo='none',
            ))
        else:
            fig.add_trace(go.Scatter3d(
            x=[row['location'][0], row['shot_end_location'][0]],
            y=[80-row['location'][1], 80-row['shot_end_location'][1]],
            z=[0, 0],  # Line stays on the ground
            mode='lines',
            line=dict(color=color, width=5),
            name='Shot Path'
        ))



    return fig
def generate_smooth_curve(x_start, x_end, y_start, y_end, z_end):
        t = np.linspace(0, 1, num=100)  # Parameter t from 0 to 1
        x_curve = (1 - t) * x_start + t * x_end
        y_curve = (1 - t) * y_start + t * y_end
        z_curve = z_end * t * (2 - t) # Parabolic curve concave down starting at z = 0
        return x_curve, y_curve, z_curve

def shot_freeze_frame_3d(fig,shot_df, tag, keeper_cone=True):
    
    shot = shot_df[shot_df['tag'] == tag].iloc[0]

    home_color = 'red'
    away_color = 'blue'

    # Create 3D figure
    

    # Add players to the plot
    for player in shot['shot_freeze_frame']:
        color = home_color if player['teammate'] == True else away_color
        symbol = 'diamond' if player['position']['name'] == 'Goalkeeper' else 'circle'
        size = 15 if player['position']['name'] == 'Goalkeeper' else 7
        fig.add_trace(go.Scatter3d(
            x=[player['location'][0]],
            y=[player['location'][1]],
            z=[0],  # Set z-coordinate for ground level
            mode='markers',
            marker=dict(color=color, size=size, symbol=symbol, line=dict(color='black', width=1)),
            hoverinfo='text',
            hovertext=f"{player['player']['name']}"
        ))

    # If keeper_cone is enabled, draw the goalkeeper's cone
    

        # Add annotation for the goalkeeper
        # for player in shot['shot_freeze_frame']:
        #     if player['position']['name'] == 'Goalkeeper':
        #         fig.add_annotation(
        #             x=player['location'][0],
        #             y=player['location'][1],
        #             z=[0.1],  # Slightly above ground
        #             text='G',
        #             showarrow=False,
        #             font=dict(size=12, color='black')
        #         )
        #         break

    # Annotate the player taking the shot
    # fig.add_annotation(
    #     x=shot['location'][0],
    #     y=shot['location'][1],
    #     z=0,  # Ground level
    #     text=shot['player'],
    #     showarrow=False,
    #     font=dict(size=9, color='white')
    # )

    # Add the shot location
    color = home_color if shot['team'] == team_1 else away_color
    fig.add_trace(go.Scatter3d(
        x=[shot['location'][0]],
        y=[80-shot['location'][1]],
        z=[0],
        mode='markers',
        marker=dict(color=color, size=15, symbol='cross', line=dict(color='black', width=2)),
        hoverinfo='text',
        hovertext=f"{shot['player']}"
    ))

    # Add the shot line
    z2 = shot['shot_end_location'][2] if len(shot['shot_end_location']) > 2 else 0
    
    if z2 > 0:  # Only create curves for shots where z2 is greater than 0
        x_curve, y_curve, z_curve = generate_smooth_curve(shot['location'][0], shot['shot_end_location'][0], 80-shot['location'][1], 80-shot['shot_end_location'][1], z2)
        
        fig.add_trace(go.Scatter3d(
            x=x_curve,
            y=y_curve,
            z=z_curve,
            mode='lines',
            line=dict(color=color, width=5),  # Change color if needed
            name='Shot Trajectory',
            hoverinfo='none',
        ))
    else:
        fig.add_trace(go.Scatter3d(
        x=[shot['location'][0], shot['shot_end_location'][0]],
        y=[80-shot['location'][1], 80-shot['shot_end_location'][1]],
        z=[0, 0],  # Line stays on the ground
        mode='lines',
        line=dict(color=color, width=5),
        name='Shot Path'
    ))


    # Handle shot outcomes
    

    # Set layout

    return fig



def draw_goals(fig,loc):
    if loc == 'home':
        x1 = 0
        x2 = -5
    else:
        x1 = 120
        x2 = 125
    fig.add_trace(go.Scatter3d(
    x=[x1, x2],
    y=[45, 45],
    z=[0, 0],
    mode='lines',
    line=dict(color='white', width=5),
    hoverinfo='none',
    ))

    fig.add_trace(go.Scatter3d(
        x=[x1, x2],
        y=[35, 35],
        z=[0, 0],
        mode='lines',
        line=dict(color='white', width=5),
        hoverinfo='none',
    ))

    fig.add_trace(go.Scatter3d(
        x=[x2, x2],
        y=[35, 45],
        z=[0, 0],
        mode='lines',
        line=dict(color='white', width=5),
        hoverinfo='none',
    ))

    fig.add_trace(go.Scatter3d(
        x=[x1, x1],
        y=[35, 45],
        z=[4, 4],
        mode='lines',
        line=dict(color='white', width=5),
        hoverinfo='none',
    ))

    fig.add_trace(go.Scatter3d(
        x=[x1, x1],
        y=[35, 35],
        z=[0, 4],
        mode='lines',
        line=dict(color='white', width=5),
        hoverinfo='none',
    ))

    fig.add_trace(go.Scatter3d(
        x=[x1, x1],
        y=[45, 45],
        z=[0, 4],
        mode='lines',
        line=dict(color='white', width=5),
        hoverinfo='none',
    ))

    # Adding the net grid
    # Horizontal lines for the net on the top
    for i in range(0, 16):
        z_value = i / 4
        fig.add_trace(go.Scatter3d(
            x=[x2, x1],
            y=[45, 45],
            z=[z_value, z_value],
            mode='lines',
            line=dict(color='white', width=2),
            hoverinfo='none',
        ))

    # Vertical lines for the net on the top
    if loc == 'home':
        for i in range(0, 20):
            x_value = x2 + i/4
            fig.add_trace(go.Scatter3d(
                x=[x_value, x_value],
                y=[45, 45],
                z=[0, 4],
                mode='lines',
                line=dict(color='white', width=2),
                hoverinfo='none',
            ))
    else:
        for i in range(0, 20):
            x_value = x2 - i/4
            fig.add_trace(go.Scatter3d(
                x=[x_value, x_value],
                y=[45, 45],
                z=[0, 4],
                mode='lines',
                line=dict(color='white', width=2),
                hoverinfo='none',
            ))
        # Horizontal lines for the net on the top
    for i in range(0, 16):
        z_value = i / 4
        fig.add_trace(go.Scatter3d(
            x=[x2, x1],
            y=[35, 35],
            z=[z_value, z_value],
            mode='lines',
            line=dict(color='white', width=2),
            hoverinfo='none',
        ))

    # Vertical lines for the net on the top
    
    for i in range(0, 20):
        if loc == 'home':
            x_value = x2 + i/4
            fig.add_trace(go.Scatter3d(
                x=[x_value, x_value],
                y=[35, 35],
                z=[0, 4],
                mode='lines',
                line=dict(color='white', width=2),
                hoverinfo='none',
            ))
        else:
            x_value = x2 - i/4
            fig.add_trace(go.Scatter3d(
                x=[x_value, x_value],
                y=[35, 35],
                z=[0, 4],
                mode='lines',
                line=dict(color='white', width=2),
                hoverinfo='none',
            ))

    # Horizontal lines for the net on the back
    for i in range(0, 16):
        z_value = i / 4
        fig.add_trace(go.Scatter3d(
            x=[x2, x2],
            y=[35, 45],
            z=[z_value, z_value],
            mode='lines',
            line=dict(color='white', width=2),
            hoverinfo='none',
        ))

    # Vertical lines for the net on the back
    for i in range(0, 40):
        y_value = 35 + i/4
        fig.add_trace(go.Scatter3d(
            x=[x2, x2],
            y=[y_value, y_value],
            z=[0, 4],
            mode='lines',
            line=dict(color='white', width=2),
            hoverinfo='none',
        ))
    
    y_min, y_max = 35, 45
    z_value = 4
    step = 1/4  # Step size for spacing between lines

    # Initialize the figure

    # Horizontal lines with floating-point step
    y = y_min
    while y <= y_max:
        fig.add_trace(go.Scatter3d(
            x=[x1, x2],  # Adjust x-range as needed
            y=[y, y],
            z=[z_value, z_value],
            mode='lines',
            line=dict(color='white', width=2),
            hoverinfo='none',
        ))
        y += step

    # Vertical lines (using integers for simplicity here)
    for x in range(x2, x1):  # Adjust x-range as needed
        fig.add_trace(go.Scatter3d(
            x=[x, x],
            y=[y_min, y_max],
            z=[z_value, z_value],
            mode='lines',
            line=dict(color='white', width=2),
            hoverinfo='none',
        ))
def calculate_distance(x1, y1, x2, y2):
    """Calculate the distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def generate_arc_points(p1, p2, apex, num_points=100):
    """Generate points on a quadratic Bezier curve (arc) between p1 and p2 with an apex."""
    t = np.linspace(0, 1, num_points)
    x = (1 - t)**2 * p1[0] + 2 * (1 - t) * t * apex[0] + t**2 * p2[0]
    y = (1 - t)**2 * p1[1] + 2 * (1 - t) * t * apex[1] + t**2 * p2[1]
    z = (1 - t)**2 * p1[2] + 2 * (1 - t) * t * apex[2] + t**2 * p2[2]
    return x, y, z
def create_timestring(row):
    second_component = str(row['second']) if row['second'] > 9 else '0'+str(row['second'])
    minute_component = str(row['minute']) if row['minute'] > 9 else '0'+str(row['minute'])
    return minute_component + ':' + second_component
pitch_width = 120
pitch_height = 80
fig, ax = createPitch(pitch_width, pitch_height, 'yards', 'gray')
comps = sb.competitions()
compets = []
for index, row in comps.iterrows():
    compets.append(row['competition_name'] + ' - ' + row['season_name'] + ' - ' + str(row['competition_id'])+ ' - ' + str(row['season_id']))
competition = st.sidebar.selectbox('Select a competition',compets)
parts = competition.split(' - ')
comp = parts[0]
compid = parts[-2]
seasonid = parts[-1]
matches = sb.matches(competition_id=compid,season_id=seasonid)
matchs = []
# st.write(matches)
for index, row in matches.iterrows():
    game = row['home_team'] + ' vs ' + row['away_team']
    matchs.append(game + ' - ' + row['competition_stage'] + ' - ' + str(row['match_id']))
matchesselect = st.sidebar.selectbox('Select a game',matchs)
matchparts = matchesselect.split(' - ')
gameid = matchparts[-1]
stage = matchparts[-2]
game2 = matchparts[0]
# gameid = 3775635
url = f'https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/{gameid}.json'
trythreesixty = st.sidebar.checkbox('Check for 360 Data')
if trythreesixty:
    try:
        frame_df = sb.frames(match_id=gameid, fmt='dataframe')
        frame_df = frame_df.rename(columns={'location': 'player_location'})
        event_df = sb.events(match_id=gameid)
        event_df['timestring'] = event_df.apply(create_timestring, axis=1)

        dfframe = pd.merge(frame_df, event_df, on='id', how='right')
        dfframe = dfframe.sort_values('timestring')
        threesixtydata = True
        st.success('360 Data Available')
    except requests.exceptions.HTTPError as e:
        threesixtydata = False
        dfframe = pd.DataFrame()
        # Handle the 404 error
        if e.response.status_code == 404:
            st.warning(f"No 360 Data Available")
        else:
            st.error(f"An error occurred: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    game = response.json()
    
    # Print the JSON data
    # print(json_data)
else:
    # Print an error message if the request failed
    st.error(f"Failed to retrieve data. Status code: {response.status_code}")
df = pd.json_normalize(game, sep='_')
location = df['location'].tolist()
x1 = np.array([el[0] if isinstance(el, (list, tuple)) else el for el in location])
y1 = pitch_height - np.array([el[0] if isinstance(el, (list, tuple)) else el for el in location])

df['x_start'] = x1
df['y_start'] = y1

# Replace non-unicode characters in players names
# df['player_name'] = df['player_name'].astype(str)
# df['player_name'] = df['player_name'].apply\
#     (lambda val: unicodedata.normalize('NFC', val).encode('ascii', 'ignore').decode('utf-8'))
# df['player_name'] = df['player_name'].replace('nan', np.nan)
# Get teams and players names
team_1 = df['team_name'].unique()[0]
team_2 = df['team_name'].unique()[1]
mask_1 = df.loc[df['team_name'] == team_1]
mask_2 = df.loc[df['team_name'] == team_2]
player_names_1 = mask_1['player_name'].dropna().unique()
player_names_2 = mask_2['player_name'].dropna().unique()


# List of activities for drop-down menus
activities = ['Pass', 'Ball Receipt', 'Carry', 'Pressure', 'Shot']


# Drop-down menus 'Select Team, Player and Activity'
if trythreesixty:
    if threesixtydata == True:
        threesixty = st.sidebar.checkbox('360 Data')
        if threesixty:
            fig = create_pitch_3d()
            mode = st.sidebar.selectbox("Choose mode:", ['Timestamp Slider', 'Shot Freeze Frame'])
            if mode == 'Timestamp Slider':
                chosen_timestamp = st.select_slider("Select timestamp", options=dfframe[(dfframe['visible_area'].notna())]['timestring'].unique())
                event_dict = get_event_dict(df=dfframe, chosen_timestamp=chosen_timestamp)

                displayed_event = st.selectbox("Select event", options=event_dict.keys())
                voronoi = st.checkbox("Highlight visible area",help='Not all parts of the field are visible in each frame so some players may not appear')
                create_3d_plot(fig=fig,df=dfframe,chosen_timestamp=chosen_timestamp, displayed_event=displayed_event, voronoi=voronoi,event_dict=event_dict)
            else:
                tab1, tab2 = st.tabs(["📈 Charts", "📄 Shot Info"])
                shot_info = event_df[event_df['shot_outcome'].notna()][['player', 'timestring', 'shot_outcome', 'shot_statsbomb_xg', 'shot_technique', 'shot_body_part']]
                shot_info.index = range(1, len(shot_info)+1)

                with tab1:
                    shot_cols = ['player', 'team', 'timestring', 'shot_outcome', 'shot_freeze_frame', 'location', 'shot_end_location']
                    shot_df = event_df[event_df['shot_outcome'].notna()][shot_cols]
                    shot_df['tag'] = shot_df['player'] + ' - ' + shot_df['timestring'] + ' ( ' + shot_df['shot_outcome'] + ' )'

                    tag = st.selectbox("Choose shot",options=shot_df['tag'].to_list())

                    shot_freeze_frame_3d(fig,shot_df, tag, keeper_cone=False)

                with tab2:
                    shot_info.columns = ["Player", "Timestamp", "Shot Outcome", "xG", "Technique", "Body Part"]
                    st.dataframe(shot_info)
            st.plotly_chart(fig,use_container_width=True)

else:
    menu_team = st.sidebar.selectbox('Select Team', (team_1, team_2))
    if menu_team == team_1:
        menu_player = st.sidebar.multiselect('Select Player', player_names_1)
    else:
        menu_player = st.sidebar.multiselect('Select Player', player_names_2)


        # Show figure


    # Call the function to create the pitch
    fig = create_pitch_3d()

    def pass_map_3d(fig):
        # Filter the dataframe for passes by the selected player
        df_pass = df.loc[(df['player_name'].isin(menu_player)) & (df['type_name'] == 'Pass')]
        df_high = df_pass[df_pass['pass_height_name'] == 'High Pass']
        df_pass = df_pass[df_pass['pass_height_name'] == 'Ground Pass']

        location = df_pass['location'].tolist()
        pass_end_location = df_pass['pass_end_location'].tolist()
        passer = df_pass['player_name'].tolist()
        recepient = df_pass['pass_recipient_name'].tolist()
        passheightname = df_pass['pass_height_name'].tolist()
        periods = df_pass['period'].tolist()
        minutes = df_pass['minute'].tolist()
        seconds = df_pass['second'].tolist()

        # Determine the color based on the team
        color = 'blue' if menu_team == team_1 else 'red'
        
        # Extract x and y coordinates
        x1 = np.array([el[0] for el in location])
        y1 = pitch_height - np.array([el[1] for el in location])
        x2 = np.array([el[0] for el in pass_end_location])
        y2 = pitch_height - np.array([el[1] for el in pass_end_location])
        # x1=x1*0.8
        # x2=x2*0.8
        # y1=y1*0.8
        # y2=y2*0.8

        if menu_team != team_1:
            x1 = pitch_width - x1
            y1 = y1
            x2 = pitch_width - x2
            y2 = y2
        
        u = x2 - x1
        v = y2 - y1
        
        # Create figure
        # if menu_team != team_1:

        #     y1 = y1+10
        #     y2 = y2+10
        #     x1=x1+10
        #     x2=x2+10
        # else:
        #     x1=x1+10
        #     x2=x2+10
        #     y1=y1+10
        #     y2=y2+10
        # Plot the passes as arrows
        for i in range(len(x1)):
            player = passer[i]
            reciever = recepient[i]
            passheight = passheightname[i].lower()
            fig.add_trace(go.Scatter3d(
                x=[x1[i], x2[i]],
                y=[y1[i], y2[i]],
                z=[0, 0],  # Assuming passes occur at the same z-coordinate
                mode='lines',
                line=dict(color=color, width=5),
                marker=dict(size=3),
                hoverinfo='text',
                hovertext=f'{player} {passheight} to {reciever} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
            ))
            # fig.add_trace(go.Scatter3d(
            #     x=[x1[i]],
            #     y=[y1[i]],
            #     z=[0],  # Assuming passes occur at the same z-coordinate
            #     mode='markers',
            #     marker=dict(color=color,size=3,symbol='circle')
            # ))
            fig.add_trace(go.Scatter3d(
                x=[x2[i]],
                y=[y2[i]],
                z=[0],  # Assuming passes occur at the same z-coordinate
                mode='markers',
                marker=dict(color=color,size=5,symbol='circle',
                ),
                hoverinfo='text',
                hovertext=f'{player} {passheight} to {reciever} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
            ))
        location = df_high['location'].tolist()
        pass_end_location = df_high['pass_end_location'].tolist()
        passer = df_high['player_name'].tolist()
        recepient = df_high['pass_recipient_name'].tolist()
        passheightname = df_high['pass_height_name'].tolist()
        x_coords = np.array([el[0] for el in location])
        y_coords = pitch_height - np.array([el[1] for el in location])
        x_coords2 = np.array([el[0] for el in pass_end_location])
        y_coords2 = pitch_height - np.array([el[1] for el in pass_end_location])
        if menu_team != team_1:
            x_coords = pitch_width - x_coords
            y_coords = y_coords
            x_coords2 = pitch_width - x_coords2
            y_coords2 = y_coords2
            

        z_value = 0  # Fixed z value

        for i in range(len(x_coords) - 1):
            x1 = x_coords[i]
            y1 = y_coords[i]
            x2 = x_coords2[i]
            y2 = y_coords2[i]
            player = passer[i]
            reciever = recepient[i]
            passheight = passheightname[i].lower()

            
            # Define the start and end points
            p1 = np.array([x1, y1, z_value])
            p2 = np.array([x2, y2, z_value])
            
            # Apex will be above the line connecting p1 and p2
            distance = calculate_distance(x1, y1, x2, y2)
            if distance > 50:
                h = 4*(randint(23,24)-20)
            elif distance > 40:
                h = 4*(randint(20,21)-20)
            elif distance > 30:
                h = 4*(randint(16,17)-15)
            elif distance > 20:
                h = 4*(randint(10, 11)-10)
            elif distance > 10:
                h = 4*(7-6)
            else: 
                h = 4*(0.5)
            apex = np.array([0.5 * (x1 + x2), 0.5 * (y1 + y2), h])  # Adjust apex height as needed
            
            # Generate arc points
            x, y, z = generate_arc_points(p1, p2, apex)
            
            # Add arc trace
            fig.add_trace(go.Scatter3d(
                x=x, y=y, z=z,
                mode='lines',
                line=dict(width=5,color=color),
                name=f'Arc {i + 1}',
                hoverinfo='text',
                hovertext=f'{player} {passheight} to {reciever} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
            ))
            fig.add_trace(go.Scatter3d(
                x=[x_coords2[i]],
                y=[y_coords2[i]],
                z=[0],  # Assuming passes occur at the same z-coordinate
                mode='markers',
                marker=dict(color=color,size=5,symbol='circle',
                ),
                hoverinfo='text',
                hovertext=f'{player} {passheight} to {reciever} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
            ))
    def ball_receipt_map_3d(fig):
        # Filter the dataframe for ball receipts by the selected player
        df_ball_rec = df.loc[(df['player_name'].isin(menu_player)) & (df['type_name'] == 'Ball Receipt*')]
        location = df_ball_rec['location'].tolist()
        periods = df_ball_rec['period'].tolist()
        minutes = df_ball_rec['minute'].tolist()
        seconds = df_ball_rec['second'].tolist()
        # Determine the color based on the team
        color = 'blue' if menu_team == team_1 else 'red'
        
        # Extract x and y coordinates
        x = np.array([el[0] for el in location])
        y = pitch_height - np.array([el[1] for el in location])
        
        # Adjust coordinates based on team
        if menu_team != team_1:
            x = pitch_width - x
            y = y

        # Add the ball receipts as markers in 3D
        fig.add_trace(go.Scatter3d(
            x=x,
            y=y,
            z=np.zeros_like(x),  # Assuming all receipts are at the same z-coordinate
            mode='markers',
            marker=dict(color=color, size=7, symbol='circle', opacity=0.5),
            name='Ball Receipts',
            hoverinfo='text',
            hovertext = [f'Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}' for i in range(len(x))]

        ))

    def carry_map_3d(fig):
        # Filter the dataframe for carries by the selected player
        df_carry = df.loc[(df['player_name'].isin(menu_player)) & (df['type_name'] == 'Carry')]
        location = df_carry['location'].tolist()
        carry_end_location = df_carry['carry_end_location'].tolist()
        periods = df_carry['period'].tolist()
        minutes = df_carry['minute'].tolist()
        seconds = df_carry['second'].tolist()
        # Determine the color based on the team
        color = 'blue' if menu_team == team_1 else 'red'
        
        # Extract coordinates
        x1 = np.array([el[0] for el in location])
        y1 = pitch_height - np.array([el[1] for el in location])
        x2 = np.array([el[0] for el in carry_end_location])
        y2 = pitch_height - np.array([el[1] for el in carry_end_location])
        
        # Adjust coordinates based on team
        if menu_team != team_1:
            x1 = pitch_width - x1
            y1 = y1
            x2 = pitch_width - x2
            y2 = y2
        
        # Calculate u and v components for arrows
        u = x2 - x1
        v = y2 - y1
        
        # Add carries as lines (arrows) in 3D
        for i in range(len(x1)):
            fig.add_trace(go.Scatter3d(
                x=[x1[i], x2[i]],
                y=[y1[i], y2[i]],
                z=[0, 0],  # Assuming carries occur at the same z-coordinate
                mode='lines',
                line=dict(color=color, width=5,dash='dash'),
                marker=dict(size=5, symbol='circle', color=color),
                name='Carries',
                hoverinfo='text',
                hovertext = [f'Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}']
            ))
            fig.add_trace(go.Scatter3d(
                x=[x2[i]],
                y=[y2[i]],
                z=[0, 0],  # Assuming shots occur at the same z-coordinate
                mode='markers',
                # line=dict(color=color, width=3),
                marker=dict(size=5, symbol='circle', color=color),
                name='Shots',
                hoverinfo='text',
                hovertext = [f'Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}']
            ))

    def pressure_map_3d(fig):
        # Filter the dataframe for pressure by the selected player
        df_pressure = df.loc[(df['player_name'].isin(menu_player)) & (df['type_name'] == 'Pressure')]
        location = df_pressure['location'].tolist()
        periods = df_pressure['period'].tolist()
        minutes = df_pressure['minute'].tolist()
        seconds = df_pressure['second'].tolist()

        # Determine the color based on the team
        color = 'blue' if menu_team == team_1 else 'red'
        
        # Extract x and y coordinates
        x = np.array([el[0] for el in location])
        y = pitch_height - np.array([el[1] for el in location])
        
        # Adjust coordinates based on team
        if menu_team != team_1:
            x = pitch_width - x
            y = y

        # Add pressure points as markers in 3D
        fig.add_trace(go.Scatter3d(
            x=x,
            y=y,
            z=np.zeros_like(x),  # Assuming all pressure points are at the same z-coordinate
            mode='markers',
            marker=dict(color=color, size=12, symbol='circle', opacity=0.5),
            name='Pressure Points',
            hoverinfo='text',
            hovertext = [f'Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}' for i in range(len(x))]
        ))

    def shot_map_3d(fig):
        # Filter the dataframe for shots by the selected player
        df_shot = df.loc[(df['player_name'].isin(menu_player)) & (df['type_name'] == 'Shot')]
        location = df_shot['location'].tolist()
        shotend = df_shot['shot_end_location'].tolist()
        outcome = df_shot['shot_outcome_name'].tolist()
        periods = df_shot['period'].tolist()
        minutes = df_shot['minute'].tolist()
        seconds = df_shot['second'].tolist()

        # Determine the color based on the team
        color = 'blue' if menu_team == team_1 else 'red'
        
        # Extract coordinates
        x1 = np.array([el[0] for el in location])
        y1 = pitch_height - np.array([el[1] for el in location])
        
        x2 = np.array([el[0] for el in shotend])
        y2 = pitch_height - np.array([el[1] for el in shotend])
        z2 = np.array([el[2] if len(el) > 2 else 0 for el in shotend])

        # Define target positions for the shots
        if menu_team == team_1:
            x2 = x2
            y2 = y2
            # x2 = np.full((len(x1)), 120)  # Target x-coordinate
            # y2 = np.full((len(y1)), 40)   # Target y-coordinate
        else:
            x1 = pitch_width-x1
            x2 = pitch_width-x2
            # y2 = pitch_height-y2
            # x2 = np.full((len(x1)), 0)    # Target x-coordinate
            # y2 = np.full((len(y1)), 40)   # Target y-coordinate

        # Calculate direction vectors
        u = x2 - x1
        v = y2 - y1
        # y1 = y1+5
        # y2 = y2+5

        # Add shots as lines (arrows) in 3D
        def generate_smooth_curve(x_start, x_end, y_start, y_end, z_end):
            t = np.linspace(0, 1, num=100)  # Parameter t from 0 to 1
            x_curve = (1 - t) * x_start + t * x_end
            y_curve = (1 - t) * y_start + t * y_end
            z_curve = z_end * t ** 2  # Parabolic curve rising to z_end
            return x_curve, y_curve, z_curve
        def generate_smooth_curve(x_start, x_end, y_start, y_end, z_end):
            t = np.linspace(0, 1, num=100)  # Parameter t from 0 to 1
            x_curve = (1 - t) * x_start + t * x_end
            y_curve = (1 - t) * y_start + t * y_end
            z_curve = z_end * t * (2 - t) # Parabolic curve concave down starting at z = 0
            return x_curve, y_curve, z_curve

        # Plot each shot
        for i in range(len(x1)):
            shotoutcome = outcome[i]
            if menu_team == team_2:
                if z2[i] > 0:  # Only create curves for shots where z2 is greater than 0
                    x_curve, y_curve, z_curve = generate_smooth_curve(x1[i], x2[i], 80-y1[i], 80-y2[i], z2[i])
                    
                    fig.add_trace(go.Scatter3d(
                        x=x_curve,
                        y=y_curve,
                        z=z_curve,
                        mode='lines',
                        line=dict(color=color, width=5),  # Change color if needed
                        name='Shot Trajectory',
                        hoverinfo='text',
                        hovertext=f'{shotoutcome} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
                    ))

                    # Plot the start and end points as markers
                    fig.add_trace(go.Scatter3d(
                        x=[x2[i], x2[i]],
                        y=[80-y2[i], 80-y2[i]],
                        z=[z2[i], z2[i]],
                        mode='markers',
                        marker=dict(size=5, symbol='circle', color=color),  # Change color if needed
                        name='Shot Points',
                        hoverinfo='text',
                        hovertext=f'{shotoutcome} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
                    ))
                else:
                    fig.add_trace(go.Scatter3d(
                    x=[x1[i], x2[i]],
                    y=[80-y1[i], 80-y2[i]],
                    z=[0, z2[i]],  # Assuming shots occur at the same z-coordinate
                    mode='lines',
                    line=dict(color=color, width=5),
                    marker=dict(size=5, symbol='circle', color=color),
                    name='Shots',
                    hoverinfo='text',
                    hovertext=f'{shotoutcome} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
                ))
                    fig.add_trace(go.Scatter3d(
                        x=[x2[i]],
                        y=[80-y2[i]],
                        z=[z2[i], z2[i]],  # Assuming shots occur at the same z-coordinate
                        mode='markers',
                        # line=dict(color=color, width=3),
                        marker=dict(size=5, symbol='circle', color=color),
                        name='Shots',
                        hoverinfo='text',
                        hovertext=f'{shotoutcome} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
                    ))
            else:
                if z2[i] > 0:  # Only create curves for shots where z2 is greater than 0
                    x_curve, y_curve, z_curve = generate_smooth_curve(x1[i], x2[i], y1[i], y2[i], z2[i])
                    
                    fig.add_trace(go.Scatter3d(
                        x=x_curve,
                        y=y_curve,
                        z=z_curve,
                        mode='lines',
                        line=dict(color=color, width=5),  # Change color if needed
                        name='Shot Trajectory',
                        hoverinfo='text',
                        hovertext=f'{shotoutcome} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
                    ))

                    # Plot the start and end points as markers
                    fig.add_trace(go.Scatter3d(
                        x=[x2[i], x2[i]],
                        y=[y2[i], y2[i]],
                        z=[z2[i], z2[i]],
                        mode='markers',
                        marker=dict(size=5, symbol='circle', color=color),  # Change color if needed
                        name='Shot Points',
                        hoverinfo='text',
                        hovertext=f'{shotoutcome} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
                    ))
                else:
                    fig.add_trace(go.Scatter3d(
                    x=[x1[i], x2[i]],
                    y=[y1[i], y2[i]],
                    z=[0, z2[i]],  # Assuming shots occur at the same z-coordinate
                    mode='lines',
                    line=dict(color=color, width=5),
                    marker=dict(size=5, symbol='circle', color=color),
                    name='Shots',
                    hoverinfo='text',
                    hovertext=f'{shotoutcome} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
                ))
                    fig.add_trace(go.Scatter3d(
                        x=[x2[i]],
                        y=[y2[i]],
                        z=[z2[i], z2[i]],  # Assuming shots occur at the same z-coordinate
                        mode='markers',
                        # line=dict(color=color, width=3),
                        marker=dict(size=5, symbol='circle', color=color),
                        name='Shots',
                        hoverinfo='text',
                        hovertext=f'{shotoutcome} Half: {periods[i]} Time: {minutes[i]}:{seconds[i]:02}'
                    ))



    typeplot = st.sidebar.selectbox('Select a plot',['Pass Map','Receipt Map','Pressure Map','Carry Map','Shot Map'])
    if typeplot == 'Pass Map':
        pass_map_3d(fig)
        df_pass = df.loc[(df['player_name'].isin(menu_player)) & (df['type_name'] == 'Pass')]

        frequency = df_pass['pass_recipient_name'].value_counts().reset_index()
        frequency.columns = ['pass_recipient_name', 'frequency']

        # Step 2: Plot the results using Plotly
        fig2 = px.pie(frequency, names='pass_recipient_name', values='frequency',
                title='Distribution of Passes to Each Recipient',
                labels={'pass_recipient_name': 'Recipient', 'frequency': 'Frequency'},
                color='frequency',  # Optional: Add color to slices based on frequency
                    # Optional: Customize color scale
                )
    # Step 1: Create bins for 'pass_length'
        # Define your bin edges and labels
        bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 100]
        labels = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60', '60-65', '65-70', '70-75', '75-80', '80-85', '85-90', '90-100']

        # Create bins for 'pass_length'
        df_pass['pass_length_bin'] = pd.cut(df_pass['pass_length'], bins=bins, labels=labels, right=True)

        # Aggregate the frequency of each bin
        frequency2 = df_pass['pass_length_bin'].value_counts().reset_index()
        frequency2.columns = ['pass_length_bin', 'frequency']
        frequency2 = frequency2.sort_values(by='pass_length_bin')  # Ensure bins are sorted correctly

        # Plot the results using Plotly
        fig3 = px.bar(frequency2, x='pass_length_bin', y='frequency',
                    title='Frequency of Pass Lengths',
                    labels={'pass_length_bin': 'Pass Length (Yards)', 'frequency': 'Frequency'},
                    color='frequency',  # Optional: Add color to bars based on frequency
                    color_continuous_scale='Blues'  # Optional: Customize color scale
                    )
        
    elif typeplot == 'Receipt Map':
        ball_receipt_map_3d(fig)
    elif typeplot == 'Carry Map':
        carry_map_3d(fig)
    elif typeplot == 'Pressure Map': 
        pressure_map_3d(fig)
    else:
        df_shot = df.loc[(df['player_name'] == menu_player) & (df['type_name'] == 'Shot')]

        frequency = df_shot['shot_outcome_name'].value_counts().reset_index()
        frequency.columns = ['shot_outcome_name', 'frequency']

        # Step 2: Plot the results using Plotly
        fig2 = px.pie(frequency, names='shot_outcome_name', values='frequency',
                title='Shot Outcomes',
                labels={'shot_outcome_name': 'Shot Outcome', 'frequency': 'Frequency'},
                color='frequency',  # Optional: Add color to slices based on frequency
                    # Optional: Customize color scale
                )
        frequency2 = df_shot['play_pattern_name'].value_counts().reset_index()
        frequency2.columns = ['play_pattern_name', 'frequency']

        # Plot the results using Plotly as a bar chart
        fig3 = px.bar(frequency2, x='play_pattern_name', y='frequency',
                    title='Frequency of Play Patterns',
                    labels={'play_pattern_name': 'Play Pattern', 'frequency': 'Frequency'},
                    color='frequency',  # Optional: Add color to bars based on frequency
                    color_continuous_scale='Blues'  # Optional: Customize color scale
                    )
        shot_map_3d(fig)
    # from random import randint
    # # df2 = df[df['type_name'] == 'Pass']
    # # df2 = df2[df2['pass_height_name'] == 'High Pass']
    # df_pass = df.loc[(df['player_name'] == menu_player) & (df['type_name'] == 'Pass')]
    # location = df_pass['location'].tolist()
    # pass_end_location = df_pass['pass_end_location'].tolist()

    # # Determine the color based on the team
    # color = 'blue' if menu_team == team_1 else 'red'

    # # Extract x and y coordinates
    # x_coords = np.array([el[0] for el in location])
    # y_coords = pitch_height - np.array([el[1] for el in location])
    # x_coords2 = np.array([el[0] for el in pass_end_location])
    # y_coords2 = pitch_height - np.array([el[1] for el in pass_end_location])
    # z_value = 0  # Fixed z value

    # for i in range(len(x_coords) - 1):
    #     x1 = x_coords[i]
    #     y1 = y_coords[i]
    #     x2 = x_coords2[i]
    #     y2 = y_coords2[i]
        
    #     # Define the start and end points
    #     p1 = np.array([x1, y1, z_value])
    #     p2 = np.array([x2, y2, z_value])
        
    #     # Apex will be above the line connecting p1 and p2
    #     distance = calculate_distance(x1, y1, x2, y2)
    #     if distance > 50:
    #         h = 2*(randint(23,24)-20)
    #     elif distance > 40:
    #         h = 2*(randint(20,21)-20)
    #     elif distance > 30:
    #         h = 2*(randint(16,17)-15)
    #     elif distance > 20:
    #         h = 2*(randint(10, 11)-10)
    #     elif distance > 10:
    #         h = 2*(7-6)
    #     else: 
    #         h = 2*(0.5)
    #     apex = np.array([0.5 * (x1 + x2), 0.5 * (y1 + y2), h])  # Adjust apex height as needed
        
    #     # Generate arc points
    #     x, y, z = generate_arc_points(p1, p2, apex)
        
    #     # Add arc trace
    #     fig.add_trace(go.Scatter3d(
    #         x=x, y=y, z=z,
    #         mode='lines',
    #         line=dict(width=5,color=color),
    #         name=f'Arc {i + 1}',
    #         hoverinfo='text',
    #         hovertext=distance
    #     ))
    fig.add_trace(go.Scatter3d(
        x=[120,120],  # Centered in x
        y=[0,0],  # Centered in y
        z=[6],  # Text floating above at z=6
        mode='text',
        text=[f'{team_2}'],
        textposition='top center',  # Adjust text position if needed
        marker=dict(size=0),  # Hide marker
        textfont=dict(size=15, color='white')  # Customize font size and color
        , hoverinfo='none'
    ))
    fig.add_trace(go.Scatter3d(
        x=[0,0],  # Centered in x
        y=[0,0],  # Centered in y
        z=[6],  # Text floating above at z=6
        mode='text',
        text=[f'{team_1}'],
        textposition='top center',  # Adjust text position if needed
        marker=dict(size=0),  # Hide marker
        textfont=dict(size=15, color='white') 
        , hoverinfo='none' # Customize font size and color
    ))
    # from streamlit_plotly_events import plotly_events
    # selected_points = plotly_events(fig,click_event=True)
    # if selected_points:
    #     for point in selected_points:
    #         # Extract point details
    #         x_val = point.get('x', 'N/A')
    #         y_val = point.get('y', 'N/A')
    #         z_val = point.get('z', 'N/A')
    #         curve_number = point.get('curveNumber', 'N/A')
    #         point_number = point.get('pointNumber', 'N/A')
    #         st.write(x_val)
    #         st.write(y_val)
    #         df2 = df[(df['x_start'] == x_val)]
    #         st.write(df2)
    st.subheader(f'{menu_player} {typeplot} - {game2} - {comp} {stage} ')
# def display_player_image(player_id, width2, caption2):
#     # Define the list of possible image sizes to try
#     image_sizes = ['24_120', '23_120', '22_120', '21_120', '20_120','19_120','18_120','17_120','16_120','15_120','14_120']  # Add more sizes if needed

#     for size in image_sizes:
#         # Construct the URL for the player image using the player ID and current size
#         image_url = f"https://cdn.sofifa.net/players/{player_id}/{size}.png"
        
#         # Check if the image URL returns a successful response
#         response = requests.head(image_url)
        
#         if response.status_code == 200:
#             # If the image is available, display it
#             st.markdown(
#                 f'<div style="display: flex; flex-direction: column; align-items: center;">'
#                 f'<img src="{image_url}" style="width: {width2}px;">'
#                 f'<p style="text-align: center; font-size: 30px;">{caption2}</p>'  # Adjust font-size as needed
#                 f'</div>',
#                 unsafe_allow_html=True
#             )
#             break  # Exit the loop once a valid image is found

#     else:
#         # If none of the URLs worked, display a placeholder or an error message
#         st.write("Image not found.")
        
# if 'Women' in competition:
#     imgs = pd.read_csv('/Users/ryan/Desktop/FantasyPython/female_players.csv')
# else:
#     imgs = pd.read_csv('/Users/ryan/Desktop/FantasyPython/male_players.csv')
# # nameparts = menu_player.split(' ')
# # def split_name(name):
# #     parts = name.split(' ', 1)  # Split on the first space
# #     return parts[0], parts[1] if len(parts) > 1 else ''

# # # Apply the function and create new columns
# # imgs[['FirstName', 'LastName']] = imgs['Name'].apply(lambda name: pd.Series(split_name(name)))
# # imgs = imgs[imgs['FirstName'] == nameparts[0]]
# # filtered_imgs = pd.DataFrame()  # Initialize an empty DataFrame

# # for name in nameparts:
# #     filtered_imgs = pd.concat([filtered_imgs, imgs[imgs['LastName'] == name]])
# # if not filtered_imgs.empty:
# #     # Extract the link from the first row of the DataFrame
# #     link = filtered_imgs['Links'].iloc[0]
    
# #     # Split the link to extract the player ID
# #     linkparts = link.split('/')
    
# #     # Ensure the player ID is in the expected position
# #     if len(linkparts) >= 2:
# #         player_id = linkparts[-2]
# #     else:
# #         player_id = None
# imgs = imgs[imgs['long_name'] == menu_player]
# if not imgs.empty:
#     id = imgs['player_id'].iloc[0]
#     if len(str(id)) == 5:
#         id = '0' + str(id)
#     if len(str(id)) == 4:
#         id = '00' + str(id)
#     def format_id(id_number):
#         # Convert the ID to a string
#         id_str = str(id_number)
#         # Ensure the ID is at least 6 digits long for proper formatting
#         if len(id_str) >= 6:
#             # Insert the slash after the first 3 digits
#             formatted_id = id_str[:3] + '/' + id_str[3:]
#         else:
#             # Handle cases where ID might be less than 6 digits
#             formatted_id = id_str
#         return formatted_id
#     formatted_id = format_id(id)    # Call the function to display the player image
#     display_player_image(formatted_id, 300, '')

    st.plotly_chart(fig,use_container_width=True)
    col1,col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig2)
    with col2:
        st.plotly_chart(fig3)

