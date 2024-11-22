import pandas as pd
import streamlit as st

# Function to merge header rows and clean up the DataFrame
def clean_dataframe(df):
    # Combine rows 2 and 3 to create a meaningful header, removing any NaN columns
    df.columns = [f"{col1} - {col2}" if pd.notna(col2) and col2 != 'nan' else col1 for col1, col2 in zip(df.iloc[1], df.iloc[2])]
    # Drop the first two rows since they are now merged into the header
    df = df.drop([0, 1, 2])
    return df

# Function to get data for a specific initial
def get_initial_data(initials):
    # Google Sheets public link in CSV format
    sheet_url = "https://docs.google.com/spreadsheets/d/1TXbsURISFld35_WD18c0rOwPuhRjVYo6DRI2GFsnEs4/export?format=csv"

    try:
        # Read the Google Sheet using pandas
        df = pd.read_csv(sheet_url, header=None)

        # Clean up the DataFrame to have a combined header
        df = clean_dataframe(df)

        # Convert all columns and data to uppercase for uniform search
        df = df.applymap(lambda x: x.upper() if isinstance(x, str) else x)

        # Search for the row where any cell matches the given initials exactly
        result = df[df.apply(lambda row: row.astype(str).str.strip().eq(initials).any(), axis=1)]

        if result.empty:
            return f"No data found for initials: {initials}"
        else:
            return result.iloc[0]
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit app
def main():
    
    # Add header image
    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.instagram.com%2Fatc_iq%2F&psig=AOvVaw3VSjCIDhDBAP434t3ANcTy&ust=1732396705684000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPjjgOnu8IkDFQAAAAAdAAAAABAI", caption="ACC Controllers - Training Department", use_column_width=True)
    
    # Update title with formatted text
    st.markdown("""
    <h1 style='text-align: center; color: #1E90FF;'>ACC CONTROLLERS INFO</h1>
    <h2 style='text-align: center; color: #4682B4;'>Training Department</h2>
    <h3 style='text-align: center; color: #708090;'>ACC Training Unit</h3>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<footer><p style='text-align: center;'>Programmed with the holy energy of coffee by MM</p></footer>", unsafe_allow_html=True):
    
    initials = st.text_input("Enter the initials (two letters):").upper()

    if st.button("Search"):
        if len(initials) == 2:
            data = get_initial_data(initials)
            st.write(data)
        else:
            st.write("Please enter exactly two letters.")

if __name__ == "__main__":
    main()

