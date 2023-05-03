import streamlit as st

st.set_page_config(
    page_title="Documentation",
    page_icon="🎬",
)

st.write("# ADM Backup Utilities 🎬")

st.sidebar.success("Select page above")

st.markdown(
    """
    This is the Backup Utilies and Documentation Page for ADM. Below are the steps for our process to back up folders to a hard disk. On the left navigation menues are utilities to help with the process.
    ### Backup steps
    1. Make sure you have Hard Disk in doubles before starting the process
    2. Identify the projects and folders you would like to back up
    3. Multiple Projects can be backed up to one Hard Disk, as long as the project is not split in half.
    4. 👈 You can use the Storage Fitter tool on the left to check if the projects can fit on the disk, and how organize them to maximize efficiency
    5. Put an empty Hard Disk in ***slot one*** of the hard disk reader, and plug it into the kitsu/server machine in the ADM cave
    6. Send an email to DNS/Guillaume telling him the HD is plugged, and which projects are to be backed up.
    7. The dock is quite slow, and the copy can easily take a few days.
    8. Wait for the email from DNS or follow through to know when the copy is over
    9. (Alternatively, the whole copying process can be done manually on your own PC without gowing through DNS)
    10. 👈 Check if the copy was done successfully using the Folder Checker tool on the left
    11. If so, time to start the clone process. Put an identical empty hard-disk in slot 2. (Cloning direction is 1 => 2 )
    12. Long press the clone button. The led indicators will start flashing on the dock showing progress. The Cloning takes a few hours.
    13. Once the cloning process is done, label the hard disk accordingly with numbers and projects inside. This [document](https://docs.google.com/spreadsheets/d/1rd7FvmyfQHlIkRxKF2T1guqdbby4GINHbugaMiEzO2M/edit#gid=475023156) contains relevent information
    14. Update the previously mentionned document, and carefully pack and store the hard disk in the ADM cave (more info on correct location to be added later)
"""
)