import os
import magic
from models.file_model import FileModel


def classify_file_type(file_path):
    """
    Classifing a file into categories based on its MIME type.
    """
    file_class = FileModel()
    
    mime = magic.Magic(mime=True)
    try:
        file_category = mime.from_file(file_path)
    except:
        file_class.file_category = 'Not accessed'
        return file_class.file_category

    match file_category:
        case t if 'x-empty' in t:
            file_class.file_category = 'Empty'
            return file_class.file_category
        case t if t.startswith('text'):
            file_class.file_category = 'Text'
            return file_class.file_category
        case t if t.startswith('image'):
            file_class.file_category = 'Image'
            return file_class.file_category
        case t if 'executable' in t:
            file_class.file_category = 'Executable'
            return file_class.file_category
        case t if t.startswith('application/zip') or t.startswith('application/x-gzip'):
            file_class.file_category = 'Compressed'
            return file_class.file_category
        case t if t.startswith('audio/'):
            file_class.file_category = 'Audio'
            return file_class.file_category
        case t if t.startswith('video/'):
            file_class.file_category = 'Video'
            return file_class.file_category
        case t if t.startswith('application/pdf'):
            file_class.file_category = 'PDF'
            return file_class.file_category
        case t if t.startswith('application/msword') or t.startswith('application/vnd.openxmlformats-officedocument.wordprocessingml.document'):
            file_class.file_category = 'MSWord'
            return file_class.file_category
        case t if t.startswith('application/vnd.ms-excel') or t.startswith('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
            file_class.file_category = 'Spreadsheet'
            return file_class.file_category
        case t if t.startswith('application/vnd.ms-powerpoint') or t.startswith('application/vnd.openxmlformats-officedocument.presentationml.presentation'):
            file_class.file_category = 'Presentation'
            return file_class.file_category
        case t if 'json' in t:
            file_class.file_category = 'Json'
            return file_class.file_category
        case _:
            file_class.file_category = 'Other'
            return file_class.file_category
        

def classify_file_permissions(file_path):
    file_class = FileModel()
    file_permissions = {}
    report = {}
    file_class.file_permissions = os.lstat(file_path).st_mode

    # Check for world-writable files
    if file_class.file_permissions & 0o002:
        report[file_path] = "🖊️  World-writable file"
    # Check for setuid/setgid files
    if file_class.file_permissions > 0o100777 and file_class.file_permissions < 0o116100:
        report[file_path] = "🚨 Setuid/setgid/sticky bit"
    # Check for files with no permissions
    if file_class.file_permissions == 0o100000:
        report[file_path] = "🚫 No permissions"

    file_permissions[file_path] = oct(file_class.file_permissions)

    return file_permissions, report
