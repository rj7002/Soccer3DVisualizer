
from statsbombpy import sb
import plotly.graph_objects as go
import numpy as np
import streamlit as st
import numpy as np
import pandas as pd
import json
import streamlit as st
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

st.sidebar.write('View multiple 3D maps such as shot maps, passing maps, receiving maps, pressure maps with data from Statsbomb API. Inspired by the work of Andrii Gozhulovskyi and Aleks Kapich.')

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
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', name=name, line=dict(color='white', width=4 * scale_factor),hoverinfo='none'))
    def add_arc2(x_center, y_center, z_center, radius, theta1, theta2, name):
        theta = np.linspace(np.deg2rad(theta1), np.deg2rad(theta2), 100)
        x = x_center - radius * np.cos(theta)  # Flip around the Y-axis
        y = y_center + radius * np.sin(theta)
        z = z_center * np.ones_like(x)
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', name=name, line=dict(color='white', width=4 * scale_factor),hoverinfo='none'))
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
        size = 7 if row['keeper'] else 7 if row['actor'] else 7
        hover = (
            'Teammate' if row['teammate'] else
            'Goalkeeper' if row['keeper'] else
            'Other Players' if not row['actor'] else
            row['player']
        )
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
        fig.add_trace(go.Scatter3d(
        x=[row['location'][0]],
        y=[80-row['location'][1]],
        z=[0],
        mode='markers',
        marker=dict(color=color, size=7, symbol='cross', line=dict(color='black', width=2)),
        hoverinfo='text',
        hovertext=f"{row['player']}"
    ))
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
            name='Shot Path',
            hoverinfo='none'
        ))



    return fig
# def generate_smooth_curve(x_start, x_end, y_start, y_end, z_end):
#         t = np.linspace(0, 1, num=100)  # Parameter t from 0 to 1
#         x_curve = (1 - t) * x_start + t * x_end
#         y_curve = (1 - t) * y_start + t * y_end
#         z_curve = z_end * t * (2 - t) # Parabolic curve concave down starting at z = 0
#         return x_curve, y_curve, z_curve

def generate_smooth_curve(x_start, x_end, y_start, y_end, z_end):
    t = np.linspace(0, 1, num=100)  # Parameter t from 0 to 1
    x_curve = (1 - t) * x_start + t * x_end
    y_curve = (1 - t) * y_start + t * y_end
    
    # Determine the distance from 35 and 45
    distance_to_35 = abs(y_end - 35)
    distance_to_45 = abs(y_end - 45)
    
    # Calculate curve strength based on proximity to 35 or 45
    if distance_to_35 < distance_to_45:
        # Closer to 35: start with a base strength and increase it
        curve_strength = 0.5 + (1 - (distance_to_35 / 10)) * 0.05  # Adjust based on the distance
        y_curve -= curve_strength * np.sin(np.pi * t)  # Bend left
    else:
        # Closer to 45: start with a base strength and increase it
        curve_strength = 0.5 + (1 - (distance_to_45 / 10)) * 0.05  # Adjust based on the distance
        y_curve += curve_strength * np.sin(np.pi * t)  # Bend right
    
    z_curve = z_end * t * (2 - t)  # Parabolic curve concave down starting at z = 0
    return x_curve, y_curve, z_curve

def shot_freeze_frame_3d(fig,shot_df, tag, keeper_cone=True):
    
    shot = shot_df[shot_df['tag'] == tag].iloc[0]

    home_color = 'red'
    away_color = 'blue'

    # Create 3D figure
    if shot['team'] != team_1:
    # Add players to the plot
        for player in shot['shot_freeze_frame']:
            color = home_color if player['teammate'] == True else away_color
            symbol = 'diamond' if player['position']['name'] == 'Goalkeeper' else 'circle'
            size = 7 if player['position']['name'] == 'Goalkeeper' else 7
            fig.add_trace(go.Scatter3d(
                x=[pitch_width-player['location'][0]],
                y=[player['location'][1]],
                z=[0],  # Set z-coordinate for ground level
                mode='markers',
                marker=dict(color=color, size=size, symbol=symbol, line=dict(color='black', width=1)),
                hoverinfo='text',
                hovertext=f"{player['player']['name']}"
            ))

    # Add the shot location
        color = home_color if shot['team'] == team_1 else away_color
        fig.add_trace(go.Scatter3d(
            x=[pitch_width-shot['location'][0]],
            y=[shot['location'][1]],
            z=[0],
            mode='markers',
            marker=dict(color=color, size=7, symbol='cross', line=dict(color='black', width=2)),
            hoverinfo='text',
            hovertext=f"{shot['player']}"
        ))

        # Add the shot line
        z2 = shot['shot_end_location'][2] if len(shot['shot_end_location']) > 2 else 0
        
        if z2 > 0:  # Only create curves for shots where z2 is greater than 0
            x_curve, y_curve, z_curve = generate_smooth_curve(pitch_width-shot['location'][0], pitch_width-shot['shot_end_location'][0], shot['location'][1], shot['shot_end_location'][1], z2)
            
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
            x=[pitch_width-shot['location'][0], pitch_width-shot['shot_end_location'][0]],
            y=[shot['location'][1], shot['shot_end_location'][1]],
            z=[0, 0],  # Line stays on the ground
            mode='lines',
            line=dict(color=color, width=5),
            name='Shot Path',
            hoverinfo='none'
        ))

    else:
        for player in shot['shot_freeze_frame']:
            color = home_color if player['teammate'] == True else away_color
            symbol = 'diamond' if player['position']['name'] == 'Goalkeeper' else 'circle'
            size = 7 if player['position']['name'] == 'Goalkeeper' else 7
            fig.add_trace(go.Scatter3d(
                x=[player['location'][0]],
                y=[80-player['location'][1]],
                z=[0],  # Set z-coordinate for ground level
                mode='markers',
                marker=dict(color=color, size=size, symbol=symbol, line=dict(color='black', width=1)),
                hoverinfo='text',
                hovertext=f"{player['player']['name']}"
            ))

    # Add the shot location
        color = home_color if shot['team'] == team_1 else away_color
        fig.add_trace(go.Scatter3d(
            x=[shot['location'][0]],
            y=[80-shot['location'][1]],
            z=[0],
            mode='markers',
            marker=dict(color=color, size=7, symbol='cross', line=dict(color='black', width=2)),
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
            name='Shot Path',
            hoverinfo='none'
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
def generate_smooth_curve(x_start, x_end, y_start, y_end, z_end):
    t = np.linspace(0, 1, num=100)  # Parameter t from 0 to 1
    x_curve = (1 - t) * x_start + t * x_end
    y_curve = (1 - t) * y_start + t * y_end
    
    # Determine the distance from 35 and 45
    distance_to_35 = abs(y_end - 35)
    distance_to_45 = abs(y_end - 45)
    
    # Calculate curve strength based on proximity to 35 or 45
    if distance_to_35 < distance_to_45:
        # Closer to 35: start with a base strength and increase it
        curve_strength = 0.5 + (1 - (distance_to_35 / 10)) * 0.05  # Adjust based on the distance
        y_curve -= curve_strength * np.sin(np.pi * t)  # Bend left
    else:
        # Closer to 45: start with a base strength and increase it
        curve_strength = 0.5 + (1 - (distance_to_45 / 10)) * 0.05  # Adjust based on the distance
        y_curve += curve_strength * np.sin(np.pi * t)  # Bend right
    
    z_curve = z_end * t * (2 - t)  # Parabolic curve concave down starting at z = 0
    return x_curve, y_curve, z_curve
def create_timestring(row):
    second_component = str(row['second']) if row['second'] > 9 else '0'+str(row['second'])
    minute_component = str(row['minute']) if row['minute'] > 9 else '0'+str(row['minute'])
    return minute_component + ':' + second_component
pitch_width = 120
pitch_height = 80
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
        # def generate_smooth_curve(x_start, x_end, y_start, y_end, z_end):
        #     t = np.linspace(0, 1, num=100)  # Parameter t from 0 to 1
        #     x_curve = (1 - t) * x_start + t * x_end
        #     y_curve = (1 - t) * y_start + t * y_end
        #     z_curve = z_end * t ** 2  # Parabolic curve rising to z_end
        #     return x_curve, y_curve, z_curve
        # def generate_smooth_curve(x_start, x_end, y_start, y_end, z_end):
        #     t = np.linspace(0, 1, num=100)  # Parameter t from 0 to 1
        #     x_curve = (1 - t) * x_start + t * x_end
        #     y_curve = (1 - t) * y_start + t * y_end
        #     z_curve = z_end * t * (2 - t) # Parabolic curve concave down starting at z = 0
        #     return x_curve, y_curve, z_curve
        def generate_smooth_curve(x_start, x_end, y_start, y_end, z_end):
            t = np.linspace(0, 1, num=100)  # Parameter t from 0 to 1
            x_curve = (1 - t) * x_start + t * x_end
            y_curve = (1 - t) * y_start + t * y_end
            
            # Determine the distance from 35 and 45
            distance_to_35 = abs(y_end - 35)
            distance_to_45 = abs(y_end - 45)
            
            # Calculate curve strength based on proximity to 35 or 45
            if distance_to_35 < distance_to_45:
                # Closer to 35: start with a base strength and increase it
                curve_strength = 0.5 + (1 - (distance_to_35 / 10)) * 0.05  # Adjust based on the distance
                y_curve -= curve_strength * np.sin(np.pi * t)  # Bend left
            else:
                # Closer to 45: start with a base strength and increase it
                curve_strength = 0.5 + (1 - (distance_to_45 / 10)) * 0.05  # Adjust based on the distance
                y_curve += curve_strength * np.sin(np.pi * t)  # Bend right
            
            z_curve = z_end * t * (2 - t)  # Parabolic curve concave down starting at z = 0
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
        df_shot = df.loc[(df['player_name'].isin(menu_player)) & (df['type_name'] == 'Shot')]

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
