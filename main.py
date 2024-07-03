import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib
import private

# adding column for each seasons nba champion
def add_champ():
    # path to the data folder with seasons stats
    dir = private.directory()

    # Iterate through the files in the specified directory
    for filename in os.listdir(dir):
        # Construct the full file path
        file_path = os.path.join(dir, filename)
        
        # Check if it is a file (and not a directory)
        if os.path.isfile(file_path):
            # Process the file (e.g., print the filename)
            print(f'Processing file: {filename}')
            # Add your file processing code here
            
    # just for the existing data csv's, can be modulated later
    champion_teams = [
        ('19-20.csv', 'Los Angeles Lakers*'),
        ('20-21.csv', 'Milwaukee Bucks*'),
        ('21-22.csv', 'Golden State Warriors*'),
        ('22-23.csv', 'Denver Nuggets*'),
        ('23-24.csv', 'Boston Celtics*')
    ]
    # will add the champ column with winner and losers

    for filename, champion_team in champion_teams:
        file_path = os.path.join(dir, filename)
        
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
           # Remove the last row
        # df = df.iloc[:-1] commented out to avoid deleting more data (only run once to remove avg row)
    
        # Add the 'champ' column
        df['champ'] = df['Team'].apply(lambda x: 1 if x == champion_team else 0)
        
        # Save the modified DataFrame back to a CSV file
        output_path = os.path.join(dir, 'modified_' + filename)
        df.to_csv(output_path, index=False)
        
        # Print the DataFrame to confirm the changes
        print(f'Processed {filename}:')
        print(df)
        print('\n')
        
def preformLinReg():
    year_csv = ['modified_19-20.csv', 'modified_20-21.csv', 'modified_22-23.csv', 'modified_23-24.csv']
    dir = private.directory()

    data_frames = []
    for file in year_csv:
        file_path = os.path.join(dir, file)
        df = pd.read_csv(file_path)
        data_frames.append(df)
            
    # Concatenate all DataFrames
    full_df = pd.concat(data_frames, ignore_index=True)

    # Define the features (all columns except 'champ' and 'Team') and the target variable ('champ') 
    X = full_df.drop(columns=['champ', 'Team'])
    y = full_df['champ']


    # Split the data into training and testing sets, using a time-based split
    # Assuming the files are ordered from oldest to newest
    split_index = int(len(full_df) * 0.8)
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

    # Fit a linear regression model to the training data
    model = LinearRegression()
    model.fit(X_train, y_train)


    # Extract the coefficients and their corresponding feature names
    coefficients = model.coef_
    features = X.columns

    # Create a DataFrame to display the feature importance
    importance_df = pd.DataFrame({'Feature': features, 'Coefficient': coefficients})

    # Display the coefficients
    print(importance_df)

    # Optional: Calculate the R-squared score to see how well the model fits the data
    r_squared = model.score(X_test, y_test)
    print(f'R-squared score: {r_squared}')
    
    model_filename = 'linear_regression_model.joblib'
    joblib.dump(model, model_filename)
    print(f'Model saved to {model_filename}')
    
