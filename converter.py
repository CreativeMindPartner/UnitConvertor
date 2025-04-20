import streamlit as st

st.markdown("""
    <style>
    .main {
        background-color:rgb(0, 52, 58);
        padding: 30px;
        border-radius: 12px;
        max-width: 750px;
        margin: auto;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        border: 2px solid #3aafa9;
    }

    h1 {
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        text-align: center;
        font-size: 2.8em;
        margin-bottom: 15px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    h2 {
        color: #3aafa9;
        font-family: 'Roboto', sans-serif;
        font-size: 1.6em;
        text-align: center;
        margin-bottom: 25px;
    }

    .stSelectbox, .stRadio > div, .stNumberInput > div > div {
        background-color: #2d3839;
        border: 2px solid #3aafa9;
 brochure        border-radius: 10px;
        padding: 12px;
        margin-bottom: 20px;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
    }

    .stSelectbox label, .stRadio label {
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        font-size: 1.1em;
    }

    .stNumberInput label {
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        font-size: 1.1em;
    }

    .stButton > button {
        background-color: #3aafa9;
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
        font-size: 1.2em;
        padding: 12px 25px;
        border-radius: 10px;
        border: 2px solid #2d3839;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .stButton > button:hover {
        background-color: #2d3839;
        border-color: #3aafa9;
        color: #3aafa9;
        transform: translateY(-2px);
        cursor: pointer;
    }

    .stAlert {
        background-color: #2d3839;
        color: #ffffff;
        border: 2px solid #3aafa9;
        border-radius: 10px;
        padding: 15px;
        font-family: 'Roboto', sans-serif;
        font-size: 1.1em;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
    }

    @media (max-width: 600px) {
        h1 {
            font-size: 2.2em;
        }
        h2 {
            font-size: 1.3em;
        }
        .stButton > button {
            font-size: 1em;
            padding: 10px 20px;
        }
        .main {
            padding: 20px;
        }
    }
    </style>
""", unsafe_allow_html=True)

def length_converter(value, choice):
    if choice == "Kilometers to Miles":
        return f"{value} km is {value * 0.621371:.2f} miles"
    elif choice == "Miles to Kilometers":
        return f"{value} miles is {value * 1.60934:.2f} km"

def weight_converter(value, choice):
    if choice == "Kilograms to Pounds":
        return f"{value} kg is {value * 2.20462:.2f} pounds"
    elif choice == "Pounds to Kilograms":
        return f"{value} pounds is {value * 0.453592:.2f} kg"

def temp_converter(value, choice):
    if choice == "Celsius to Fahrenheit":
        return f"{value}°C is {(value * 9/5) + 32:.2f}°F"
    elif choice == "Fahrenheit to Celsius":
        return f"{value}°F is {(value - 32) * 5/9:.2f}°C"

def main():
    st.title("Unit Converter")
    st.subheader("Convert Length, Weight, and Temperature")
    
# Container for better layout
    with st.container():
        option = st.selectbox("Choose Conversion Type", ["Length Converter", "Weight Converter", "Temperature Converter"])
        
        if option == "Length Converter":
            choice = st.radio("Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
            value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
            if st.button("Convert"):
                st.success(length_converter(value, choice))
        
        elif option == "Weight Converter":
            choice = st.radio("Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
            value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
            if st.button("Convert"):
                st.success(weight_converter(value, choice))
        
        elif option == "Temperature Converter":
            choice = st.radio("Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
            value = st.number_input("Enter Value", format="%.2f")
            if st.button("Convert"):
                st.success(temp_converter(value, choice))

if __name__ == "__main__":
    main()