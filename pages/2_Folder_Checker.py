import os
import streamlit as st

def get_folder_info(folder_path, status_text=None, total_size_scanned=0):
    total_size = 0
    file_count = 0

    for entry in os.scandir(folder_path):
        if entry.is_file():
            entry_size = entry.stat().st_size
            total_size += entry_size
            total_size_scanned += entry_size
            file_count += 1
            if status_text is not None:
                status_text.text(f"Scanning {folder_path}")
        elif entry.is_dir():
            subdir_size, subdir_file_count, total_size_scanned = get_folder_info(entry.path, status_text, total_size_scanned)
            total_size += subdir_size
            file_count += subdir_file_count

    return total_size, file_count, total_size_scanned

def start_comparison(directory_pairs, size_threshold, file_count_threshold, status_text=None):
    results = []

    for dir_a, dir_b in directory_pairs:
        size_a, num_files_a, _ = get_folder_info(dir_a, status_text)
        size_b, num_files_b, _ = get_folder_info(dir_b, status_text)

        size_delta = abs(size_a - size_b)
        file_count_delta = abs(num_files_a - num_files_b)

        if size_delta <= size_threshold and file_count_delta <= file_count_threshold:
            result = f'Directory pair {dir_a} and {dir_b} (pair {directory_pairs.index((dir_a, dir_b)) + 1}) are identical. The directory size is {size_a} bytes, and it contains {num_files_a} files.\n'
        else:
            result = f'Directory pair {dir_a} and {dir_b} (pair {directory_pairs.index((dir_a, dir_b)) + 1}) are different. The size delta between directories is {size_delta} bytes, and the file number delta is {file_count_delta} files.\n'

        identical = size_delta <= size_threshold and file_count_delta <= file_count_threshold
        results.append((result, identical))

    return results





size_threshold = st.sidebar.number_input("Size threshold", min_value=0, value=2000, step=1)
file_count_threshold = st.sidebar.number_input("File count threshold", min_value=0, value=0, step=1)

st.header("Directory Pairs")

if 'pair_count' not in st.session_state:
    st.session_state.pair_count = 1

st.session_state.directory_pairs = []

for i in range(st.session_state.pair_count):
    col1, col2 = st.columns(2)
    with col1:
        dir_a = st.text_input(f"Directory A (pair {i + 1})", key=f"dir_a_{i}")
    with col2:
        dir_b = st.text_input(f"Directory B (pair {i + 1})", key=f"dir_b_{i}")

    if dir_a and dir_b:
        st.session_state.directory_pairs.append((dir_a, dir_b))

if st.button("Add another pair"):
    st.session_state.pair_count += 1

if st.button("Start comparison"):
    if not st.session_state.get('directory_pairs', []):
        st.error("Please add at least one pair of directories.")
    else:
        # Create a progress bar and a status text output
        progress_bar = st.progress(0)
        status_text = st.empty()

        results = []
        num_pairs = len(st.session_state.directory_pairs)

        for index, pair in enumerate(st.session_state.directory_pairs, start=1):
            # Update progress bar
            progress_bar.progress(index / num_pairs)

            result, identical = start_comparison([pair], size_threshold, file_count_threshold, status_text)[0]
            results.append((result, identical))

            # Clear status text
            status_text.empty()

        for result, identical in results:
            background_color = "rgba(144, 238, 144, 0.5)" if identical else "rgba(255, 182, 193, 0.5)"
            st.markdown(f"<div style='background-color: {background_color}; padding: 10px;'>{result}</div>", unsafe_allow_html=True)
            st.write("---")