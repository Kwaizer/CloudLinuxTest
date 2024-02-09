def generate_report_permissions(report_list_dirs, report_list_files):
    print("\n📜 Report:")
    if report_list_dirs:
        for report_item in report_list_dirs:
            print(f"Can't access: {report_item} dir")
    if not report_list_files:
        print("- Suspicious files haven't been found 😑")
    else:
        for report_item in report_list_files:
            file_path, description = next(iter(report_item.items()))
            print(f"- {description}: {file_path}")