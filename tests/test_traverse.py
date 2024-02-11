import os
import pytest

from logic.traverse import traverse_directory


current_path = os.path.abspath(__file__)
directory_path = os.path.dirname(current_path)

# Navigate up the directory structure until reaching 'test_folder'
while not os.path.exists(os.path.join(directory_path, 'test_folder')):
    directory_path = os.path.dirname(directory_path)

    
@pytest.mark.test
def test_traverse_directory():
    result = traverse_directory(directory_path + "/test_folder")
    files = result[0]
    report_dir = result[1]
    report_files = result[2]

    assert len(files) == 4
    assert report_dir == []
    assert report_files == [{'/home/kwaizer/CloudLinux/test/test_folder/dir1/ww.txt': '🖊️  World-writable file'},
                            {'/home/kwaizer/CloudLinux/test/test_folder/dir1/s.txt': '🚨 Setuid/setgid/sticky bit'}]