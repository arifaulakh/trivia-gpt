# from PyPDF2 import PdfReader
import re
from pypdf import PdfReader


class PackParser:
    def __init__(self, filename):
        self.reader = PdfReader(filename)
        self.questions = []

    def parse_page(self, page, i):
        page_text = page.extract_text()
        text = page_text.replace('\n', ' ')
        pattern = re.compile(r'(\d+\..*?)(?=\s*\d+\..*|$)')
        matches = pattern.findall(text)
        result = []
        for match in matches:
            if 'A:' in match:
                question, answer = match.split('A:')
                result.append((question.strip(), answer.strip()))
            else:
                result.append((match.strip(), 'No answer found'))

        return result
    def parse(self):
        for i in range(1, len(self.reader.pages)):
            print(f"starting to parse page {i}")
            self.questions += self.parse_page(self.reader.pages[i], i)
            print(f"finished parsing page {i}")
        
        print("completed parsing")
    def get_questions(self):
        return self.questions
    
    def questions_to_txt(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for question, answer in self.questions:
                f.write('{} | {}\n'.format(question, answer))

# pack_parser = PackParser("trivia_pack_1.pdf")
# pack_parser.parse()
# pack_parser.questions_to_txt('pack_1_parsed.txt')

