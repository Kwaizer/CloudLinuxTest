import os
from file import traverse_directory


def traverse(dir, thr):
    directory_path = dir
    size_threshold = thr 
    category_info = {}
    large_files = []
    if os.path.isdir(directory_path) and os.access(directory_path, os.R_OK):
        return_files, report_list = traverse_directory(directory_path)
        if return_files:
            if size_threshold is not None:
                for file in return_files:
                    if file.file_size > size_threshold:
                        large_files.append(file)
            # Update the size for the file category in the dictionary
            for file in return_files:
                category_info[file.file_category] = {
                    'size': category_info.get(file.file_category, {'size': 0})['size'] + file.file_size,
                    'count': category_info.get(file.file_category, {'count': 0})['count'] + 1
                }
            # Display the results
            print("\n💾 Files categorized based on type and total size:")
            for category, info in category_info.items():
                print(f"- {category}: {info['count']} files, Total Size: {info['size']:.2f} mb")
            print("\n📜 Report:")
            if not report_list:
                print("- Nothing suspicious has been found 😑")
            else:
                for report_item in report_list:
                    file_path, description = next(iter(report_item.items()))
                    print(f"- {description}: {file_path}")
            print("\n🍔 Large Files:")
            if large_files:
                output = "\n".join([f"- {file.file_path} - {file.file_size:.2f} mb" for file in large_files])
                print(output)
            else:
                print("- No large files found.")
        else:
            print("No files found in the specified directory.")
    else:
        print("Invalid directory path or access denied.")


def traverse_with_report(dir, thr):
    pass


def traverse_with_categories(dir, thr):
    pass


def traverse_with_thr(dir, thr):
    pass


def traverse_with_report_and_categories(dir, thr):
    pass


def traverse_with_report_and_categories_and_thr(dir, thr):
    pass