from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Dillan', 'Rawlings') == 'Rawlings; Dillan'
    assert make_full_name('Tanner', 'Buckuneermire') == 'Buckuneermire; Tanner'
    assert make_full_name('Kavyn', 'Abel') == 'Abel; Kavyn'
    assert make_full_name('', 'Stop') == 'Stop; '
    assert make_full_name('Fu', 'Shang-Moshoo-pintang')== 'Shang-Moshoo-pintang; Fu'

def test_extract_family_name():
    assert extract_family_name('Rawlings; Dillan') == 'Rawlings'
    assert extract_family_name('Buckuneermire; Tanner') == 'Buckuneermire'
    assert extract_family_name('Abel; Kavyn') == 'Abel'
    assert extract_family_name('Stop; ') == 'Stop'
    assert extract_family_name('Shang-Moshoo-pintang; Fu')== 'Shang-Moshoo-pintang'

def test_extract_given_name():
    assert extract_given_name('Rawlings; Dillan') == 'Dillan'
    assert extract_given_name('Buckuneermire; Tanner') == 'Tanner'
    assert extract_given_name('Abel; Kavyn') == 'Kavyn'
    assert extract_given_name('Stop; ') == ''
    assert extract_given_name('Shang-Moshoo-pintang; Fu') == 'Fu'

    # Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])