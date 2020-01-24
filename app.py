import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from gtts import gTTS
from time import time

def getText(path):
  if path:
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
    with open(path, 'rb') as fh:
      for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
        page_interpreter.process_page(page)

      text = fake_file_handle.getvalue()
 
    # close open handles
    converter.close()
    fake_file_handle.close()
 
    return text
  
def audibify(text, toSave, name):
  audio = gTTS(text=text, lang="en")
  audio.save("{}{}.mp3".format(toSave.split('\\')[:-1], name))
  pass
  
def main(path):
  # Check timing
  started = time()
  # Create MP3
  audibify(getText(path), path, path.split('\\')[-1].split('.')[0] + ".mp3")
  # log timing to console
  print('took', "{0:.2f}".format(time() - started), 'seconds')
  exit()