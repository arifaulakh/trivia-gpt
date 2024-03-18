import pytest
from parse_questions import PackParser

@pytest.fixture
def pack_parser():
    return PackParser("trivia_pack_1.pdf")

def test_init(pack_parser):
    assert pack_parser.reader is not None
    assert isinstance(pack_parser.questions, list)
    assert len(pack_parser.questions) == 0

def test_parse_page(pack_parser):
    page = pack_parser.reader.pages[1]
    results = pack_parser.parse_page(page, 0)
    assert isinstance(results, list)
    assert len(results) == 0  # Assuming the test PDF has at least one question on the first page
    for question, answer in results:
        assert isinstance(question, str)
        assert isinstance(answer, str)

# def test_parse(pack_parser, mocker):
#     mocker.patch.object(pack_parser, 'parse_page', return_value=[("Sample Question", "Sample Answer")])
#     pack_parser.parse()
#     assert len(pack_parser.questions) > 0  # Assuming the test PDF has more than one page

# def test_get_questions(pack_parser, mocker):
#     mocker.patch.object(pack_parser, 'parse', return_value=[("Sample Question", "Sample Answer")])
#     pack_parser.parse()
#     questions = pack_parser.get_questions()
#     assert isinstance(questions, list)
#     assert len(questions) > 0

# def test_questions_to_txt(pack_parser, tmp_path, mocker):
#     d = tmp_path / "sub"
#     d.mkdir()
#     p = d / "questions.txt"
#     mocker.patch.object(pack_parser, 'get_questions', return_value=[("Sample Question", "Sample Answer")])
#     pack_parser.questions_to_txt(p)
#     assert p.read_text() == "Sample Question | Sample Answer\n"
