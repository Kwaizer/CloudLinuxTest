import os
import pytest
from logic.classify_file import classify_file_permissions, classify_file_type

current_path = os.path.abspath(__file__)
directory_path = os.path.dirname(current_path)

# Navigate up the directory structure until reaching 'test_folder'
while not os.path.exists(os.path.join(directory_path, 'test_folder')):
    directory_path = os.path.dirname(directory_path)


@pytest.mark.test
def test_classify_file_type():
    result = classify_file_type(directory_path + "/test_folder/2.json")
    assert result == 'Json'

@pytest.mark.test
def test_classify_file_permissions():
    result, report = classify_file_permissions(directory_path + "/test_folder/dir1/ww.txt")
    assert result == {directory_path + "/test_folder/dir1/ww.txt": '0o100777'}
    assert report == {directory_path + "/test_folder/dir1/ww.txt": '🖊️  World-writable file'}