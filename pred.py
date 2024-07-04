import pandas as pd
import joblib
import private

def test():
    # Load the new season data
    new_season_file = private.test()
    new_season_df = pd.read_csv(new_season_file)

    X_new = new_season_df.drop(columns=['Team'])

    # Load the saved logistic regression model
    model_filename = 'logistic_regression_model.joblib'
    loaded_model = joblib.load(model_filename)

    # Predict the likelihood of each team becoming the champion
    champion_probabilities = loaded_model.predict_proba(X_new)[:, 1]

    # Add the predictions to the DataFrame
    new_season_df['Champ_Probability'] = champion_probabilities


    # Sort the DataFrame by the champion probability in descending order
    new_season_df_sorted = new_season_df.sort_values(by='Champ_Probability', ascending=False)


    # Display the DataFrame with the new probabilities
    print(new_season_df_sorted[['Team', 'Champ_Probability']])

    # Save the results to a new CSV file if needed
    new_season_df.to_csv(index=False)
    print(f'Predictions saved')
    
    
    

