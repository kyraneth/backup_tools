import streamlit as st

st.set_page_config(
    page_title="Documentation",
    page_icon="🎬",
)

st.write("# ADM Backup Utilities 🎬")

st.sidebar.success("Select page above")

st.markdown(
    """
    This is the Backup Utilies and Documentation Page for ADM
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)