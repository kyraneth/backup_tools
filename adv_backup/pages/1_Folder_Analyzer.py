import os
import streamlit as st

def get_folder_info(folder_path, status_text=None):
    total_size = 0
    file_count = 0

    for entry in os.scandir(folder_path):
        if entry.is_file():
            total_size += entry.stat().st_size
            file_count += 1
        elif entry.is_dir():
            subdir_size, subdir_file_count = get_folder_info(entry.path, status_text)
            total_size += subdir_size
            file_count += subdir_file_count

        if status_text:
            status_text.text(f"Scanning {entry.name}, in {folder_path}")

    return total_size, file_count

def efficient_fitting_greedy(folder_infos, hard_disk_size_tb, safety_margin_percent):
    hard_disk_size_bytes = hard_disk_size_tb * (1024 ** 4)
    safety_margin = hard_disk_size_bytes * (safety_margin_percent / 100)
    adjusted_hard_disk_size_bytes = hard_disk_size_bytes - safety_margin

    folder_sizes = [(folder, size) for folder, size, _ in folder_infos]
    folder_sizes.sort(key=lambda x: x[1], reverse=True)

    result_folders = []
    remaining_space = adjusted_hard_disk_size_bytes

    for folder, size in folder_sizes:
        if size <= remaining_space:
            result_folders.append((folder, size))
            remaining_space -= size

    return result_folders, remaining_space

st.title("Folder Analyzer")

hard_disk_size_tb = st.sidebar.number_input("Hard Disk Size (TB)", min_value=0.0, value=1.0, step=0.01)
safety_margin_percent = st.sidebar.slider("Safety Margin (%)", min_value=0, max_value=100, value=10)

st.header("Folders")

if 'folder_count' not in st.session_state:
    st.session_state.folder_count = 1

st.session_state.folders = []

for i in range(st.session_state.folder_count):
    folder = st.text_input(f"Folder {i + 1}", key=f"folder_{i}")
    if folder:
        st.session_state.folders.append(folder)

if st.button("Add another folder"):
    st.session_state.folder_count += 1

if st.button("Scan Storage"):
    if not st.session_state.get('folders', []):
        st.error("Please add at least one folder.")
    else:
        status_text = st.empty()
        progress_bar = st.progress(0)

        folder_infos = []
        for i, folder in enumerate(st.session_state.folders):
            progress_bar.progress((i + 1) / len(st.session_state.folders))
            size, file_count = get_folder_info(folder, status_text)
            folder_infos.append((folder, size, file_count))

        status_text.empty()
        progress_bar.empty()

        st.write("Folder information:")
        for folder, size, file_count in folder_infos:
            st.write(f"{folder} - {size / (1024 ** 2):.2f} MB - {file_count} files")

        st.session_state.folder_infos = folder_infos

if st.button("Fit in Hard Disk"):
    if not st.session_state.get('folder_infos', []):
        st.error("Please scan the storage first.")
    else:
        result_folders, remaining_space = efficient_fitting_greedy(
            st.session_state.folder_infos, hard_disk_size_tb, safety_margin_percent
        )
        
        st.write("Folders to fit in hard disk:")
        for folder, size in result_folders:
            st.write(f"{folder} - {size / (1024 ** 2):.2f} MB")

        st.write(f"Remaining space: {remaining_space / (1024 ** 4):.2f} TB")   
