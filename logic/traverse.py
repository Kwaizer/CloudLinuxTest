from multiprocessing import Pool
import os
from logic.classify_file import classify_file_permissions, classify_file_type
from reports.gen_rep_ctg import generate_report_file_categories
from reports.gen_rep_permisions import generate_report_permissions
from models.file_model import FileModel
from reports.gen_rep_thr import generate_report_large_files


def process_file(file_path):
    file_category = classify_file_type(file_path)
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

    pool = Pool()  

    for root, dirs, files in os.walk(directory):
        # Appending inaccessible directories
        for d in dirs:
            dir_path = os.path.join(root, d)
            if not os.access(dir_path, os.R_OK):
                report_list_dirs.append(dir_path)

        # Processing files using multiprocessing pool
        file_paths = [os.path.join(root, file) for file in files]
        results = pool.map(process_file, file_paths)

        # Unpacking the results
        for result, report in results:
            return_files.append(result)
            if report:
                report_list_files.append(report)

    pool.close()
    pool.join()

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
