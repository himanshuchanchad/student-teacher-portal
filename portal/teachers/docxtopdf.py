import sys
import os
import comtypes.client
from portal.settings import MEDIA_ROOT
wdFormatPDF = 17


def converter(in_file,type,name):
    print("vvvvvvvvvvvvvvvvvvvvvv")
    out = os.path.join(MEDIA_ROOT,type,name)
    out_file=os.path.abspath(name)
    print(out_file)
    print(".................................................................")
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
    print(out_file)
    return out_file
