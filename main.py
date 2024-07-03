import os
import pandas as pd
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
        
        
