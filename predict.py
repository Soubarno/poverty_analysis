import streamlit as st
import pandas as pd

from web_functions import predict

# Load the Indian census data
df = pd.read_csv('indian_census_2022.csv')


# Assuming X and y are defined
X = df[["Population","Literacy_Index","Poverty_Index","Standard_of_Life","Hunger_Index","Satisfaction_Level","Healthcare","Basic_Needs"]]
y = df['Score'].astype(int)

def app(df, X, y):

    st.title("Prediction Page")

    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Poverty Analysis.
            </p>
        """, unsafe_allow_html=True)
    
    st.subheader("Select State:")

    # Create a dropdown menu for selecting the state
    selected_state = st.selectbox("Select State", df['State'])

    # Autofill the features based on the selected state
    selected_row = df[df['State'] == selected_state].iloc[0]
    Population = float(selected_row["Population"])
    Literacy_Index = float(selected_row["Literacy_Index"])
    Poverty_Index = float(selected_row["Poverty_Index"])
    Standard_of_Life = float(selected_row["Standard_of_Life"])
    Hunger_Index = float(selected_row["Hunger_Index"])
    Satisfaction_Level = float(selected_row["Satisfaction_Level"])
    Healthcare = float(selected_row["Healthcare"])
    Basic_Needs = float(selected_row["Basic_Needs"])
     
    # Scale down Population to fit within the range of 0 to 1
    population_scaled = Population / df["Population"].max()
    literacy_index_scaled = Literacy_Index / df["Literacy_Index"].max()
    poverty_index_scaled = Poverty_Index / df["Poverty_Index"].max()
    standard_of_life_scaled = Standard_of_Life / df["Standard_of_Life"].max()
    hunger_index_scaled = Hunger_Index / df["Hunger_Index"].max()
    satisfaction_level_scaled = Satisfaction_Level / df["Satisfaction_Level"].max()
    healthcare_scaled = Healthcare / df["Healthcare"].max()
    basic_needs_scaled = Basic_Needs / df["Basic_Needs"].max()


     
    # Display progress bars for each feature
    st.subheader("Features:")
    st.markdown("**Population:**")
    st.progress(population_scaled)
    st.write(f" {Population}")
    st.markdown("**Literacy Rate:**")
    st.progress(literacy_index_scaled)
    st.write(f" {Literacy_Index}")
    st.markdown("**Poverty Index:**")
    st.progress(poverty_index_scaled)
    st.write(f" {Poverty_Index}")
    st.markdown("**Standard of Living:**")
    st.progress(standard_of_life_scaled)
    st.write(f" {Standard_of_Life}")
    st.markdown("**Hunger Index:**")
    st.progress(hunger_index_scaled)
    st.write(f" {Hunger_Index}")
    st.markdown("**Governance Satisfaction:**")
    st.progress(satisfaction_level_scaled)
    st.write(f" {Satisfaction_Level}")
    st.markdown("**Healthcare Satisfaction:**")
    st.progress(healthcare_scaled)
    st.write(f" {Healthcare}")
    st.markdown("**Basic Needs:**")
    st.progress(basic_needs_scaled)
    st.write(f" {Basic_Needs}")

    # Create a button to predict
    if st.button("Detect Class"):
        # Get prediction and model score
        features = [Population, Literacy_Index, Poverty_Index, Standard_of_Life, Hunger_Index, Satisfaction_Level, Healthcare, Basic_Needs]
        prediction, score = predict(X, y, features)
        score = score
        

        # Print the output according to the prediction
                
        if (prediction == 2):
            st.error("Extremely poor! On brink of poverty")
            
        elif (prediction == 3):
            st.error("Very Poor! Need financial aids")
          
        elif (prediction == 4):
            st.error("Poor! Need financial aids")
     
        elif (prediction == 5):
            st.warning("Average. Need good governance")
      
        elif (prediction == 6):
            st.warning("Good! Well to do")
    
        elif (prediction == 7):
            st.warning("Very good! Significantly good.")

        elif (prediction == 8):
            st.success("Prosperous State! Doing good.")
    
        elif (prediction == 9):
            st.success("Magnificient! Surplus aids present")
  
        elif (prediction == 10):
            st.success("Extremely Good and Rich State")
 
        
        # Print the score of the model 
        st.sidebar.write("The model used is trusted by beaurocratists and has an accuracy of ", round((score*100),2),"%")

# Call the app function
app(df, X, y)
