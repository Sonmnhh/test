import streamlit as st
import requests


# Streamlit UI
def main():
    st.title("Stock News Sentiment Analysis")

    # Input text boxes for user input
    headline = st.text_input("Enter the news headline:")
    content = st.text_area("Enter the news content:")

    # Button to trigger prediction
    if st.button("Predict"):
        # Combine headline and content
        combined_text = headline + " " + content


        # Map labels to sentiment categories
        label_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
        scores = output[0]

        # Display predicted sentiment percentages
        st.subheader("Predicted Sentiment:")

# Ensure the output is not empty
        if output:
            predictions = output[0]

    # Define the mapping between labels and sentiment categories
            label_map = {'LABEL_0': 'Negative', 'LABEL_1': 'Neutral', 'LABEL_2': 'Positive'}

    # Sort the predictions based on score in descending order
            sorted_predictions = sorted(predictions, key=lambda x: x['score'], reverse=True)

    # Display each sentiment category along with its score
            for prediction in sorted_predictions:
                label = prediction['label']
                sentiment_label = label_map.get(label, 'Unknown')
                score = prediction['score'] * 100
        
        # Display sentiment label with appropriate emoji and percentage
                if sentiment_label == 'Positive':
                    st.write(f"{sentiment_label.capitalize()} ✅:- {score:.2f}%", unsafe_allow_html=True)
                elif sentiment_label == 'Negative':
                    st.write(f"{sentiment_label.capitalize()} ❌:- {score:.2f}%", unsafe_allow_html=True)
                else:
                    st.write(f"{sentiment_label.capitalize()} ⏳:- {score:.2f}%", unsafe_allow_html=True)
        else:
            st.write("No sentiment prediction available.")


if __name__ == "__main__":
    main()
