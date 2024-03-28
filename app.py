import streamlit as st
from story_content import get_story_content  # Import the function

# Initialize 'current_node' in session_state if it doesn't exist
def initialize_session_state():
    if 'current_node' not in st.session_state:
        st.session_state['current_node'] = '0'

# Call the function to ensure the session state is initialized
initialize_session_state()
# Function to display the story node. Refactored for better readability.

# Function to display choices and handle button clicks
def display_node_choices(node, node_id):
    choices = node.get('choices', [])
    for choice_text, next_node in choices:
        if st.button(choice_text):
            st.session_state['current_node'] = next_node
            st.experimental_rerun()
            return
    
    # If there are no choices (end of a story path), show the restart button
    if not choices and node_id != '0':  # Check if it's an end node and not the start node
        display_restart_option()

# Function to display node content
def display_node_content(node):
    if 'image' in node and node['image']:
        st.image(node['image'], width=400)
    st.write(node['text'])


# Function to display choices and handle button clicks
def display_node_choices(node, node_id):
    for choice_text, next_node in node.get('choices', []):
        if st.button(choice_text):
            st.session_state['current_node'] = next_node
            st.experimental_rerun()
            return
    if node_id != '0':  # Avoid showing restart on the initial node
        display_restart_option()


# Display an error message and an option to restart the story
def display_error_and_restart_option():
    st.error("The story node is missing or the story has ended. Choose a new path or restart the game.")
    display_restart_option()


# Display a restart button
def display_restart_option():
    if st.button('Restart the Story'):
        st.session_state['current_node'] = '0'
        st.experimental_rerun()


# Main 
def main():
    initialize_session_state()
    display_story_node(st.session_state['current_node'])


if __name__ == "__main__":
    main()
