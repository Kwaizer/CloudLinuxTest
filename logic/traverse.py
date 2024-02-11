import os
import concurrent.futures
from models.file_model import FileModel
from logic.classify_file import classify_file_permissions, classify_file_type
from reports.gen_rep_ctg import generate_report_file_categories
from reports.gen_rep_permisions import generate_report_permissions
from reports.gen_rep_thr import generate_report_large_files


def process_file(file_path):
    file_category = classify_file_type(file_path)
    if file_category == 'Not accessed':
        report = {file_path : f"Can't access a file. Possibly broken symlink or denied access"}
        return FileModel(file_path, file_category), report
    file_size = os.lstat(file_path).st_size / 1000000
    file_permissions, report = classify_file_permissions(file_path)
    return FileModel(file_path, file_category, file_size, file_permissions), report

def traverse_directory(directory):
    """
    Traversing through a directory recursively.
    """
    return_files = []
    report_list_files = []
    report_list_dirs = []

    file_paths = []

    for root, dirs, files in os.walk(directory):
        # Appending inaccessible directories
        for d in dirs:
            dir_path = os.path.join(root, d)
            if not os.access(dir_path, os.R_OK):
                report_list_dirs.append(dir_path)

        # Collecting file paths for processing
        file_paths.extend([os.path.join(root, file) for file in files])

    # Using ThreadPoolExecutor for concurrent I/O-bound operations
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Processing files in batches
        batch_size = 100  
        for i in range(0, len(file_paths), batch_size):
            batch_files = file_paths[i:i + batch_size]
            results = list(executor.map(process_file, batch_files))
            for result, report in results:
                return_files.append(result)
                if report:
                    report_list_files.append(report)

    return return_files, report_list_dirs, report_list_files


def get_info(dir, thr, rep, ctg):
    directory_path = dir
    size_threshold = thr 
    if os.path.isdir(directory_path) and os.access(directory_path, os.R_OK):
        return_files, report_list_dirs, report_list_files = traverse_directory(directory_path)
        if return_files:

            # Categories display
            if ctg == True:
                generate_report_file_categories(return_files)
            
            # Inaccessible directories and suspicious files report
            if rep == True:
                generate_report_permissions(report_list_dirs, report_list_files)

            # Large files report
            if thr != None:
                generate_report_large_files(return_files, size_threshold)
        else:
            print("No files found in the specified directory.")
    else:
        print("Invalid directory path or access denied.")
