import sys, os

sys.path.append('.')
sys.path.append('..')

from check_boking_done import check_boking_done

def test_check_boking_done():
    file = "/".join([os.path.realpath(os.path.dirname(__file__)), "test_data/bekraftad_bokning.html"])
    with open(file, "r") as f:
        content = f.read()
        boking = check_boking_done(content)
        assert boking == "661181989"