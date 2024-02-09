def generate_report_file_categories(return_files):
    
    category_info = {}
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