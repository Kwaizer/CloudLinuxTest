import os
import pytest
from logic.traverse import process_file

current_path = os.path.abspath(__file__)
directory_path = os.path.dirname(current_path)

# Navigate up the directory structure until reaching 'test_folder'
while not os.path.exists(os.path.join(directory_path, 'test_folder')):
    directory_path = os.path.dirname(directory_path)


@pytest.mark.test
def test_classify_file_type():
    result = process_file(directory_path + "/test_folder/dir1/ww.txt")
    file_class = result[0]
    report = result[1]
    
    assert file_class.file_path == directory_path + "/test_folder/dir1/ww.txt"
    assert file_class.file_category == "Empty"
    assert file_class.file_permissions == {directory_path + "/test_folder/dir1/ww.txt": '0o100777'}
    assert file_class.file_size == 0.0
    assert report == {directory_path + "/test_folder/dir1/ww.txt": '🖊️  World-writable file'}