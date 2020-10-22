""" 2020/10/22
VerSion:
    Python 3.8.5

pip install:
    PyPDF2==1.26.0

---------------------------------------
# PDFが格納されたフォルダを選択する。
# 選択したフォルダの中にあるPDFファイルを1ファイルに結合する.

## コマンドラインで操作
arg2: 指定しなかった場合
        結合されるファイル名は、先頭と末尾のファイル名をハイフンで結合したファイル名となる.

arg1: まとめたいPDFフォルダ名
arg2: 1ファイルするPDFファイル名

ex:
  $ python marge_pdf.py <PDF dir name> <marge PDF file name>

"""

import PyPDF2
import sys

from pathlib import Path


class NotPdfFileError(Exception):
    """ pdfファイルがないとき """
    pass


def get_pdf_dir(args):
    """ コマンドライン入力: 第1引数に1ファイルにしたいPDFフォルダを指定

    :param args: pdf dir
    :return
        第一引数に指定したフォルダ名を返す
    """
    pdf_dir_ = args[1]

    pdf_dir_name = Path(pdf_dir_)
    print(f"pdf dir name : {pdf_dir_name}\n")
    return pdf_dir_name


def create_pdf_file_list_ascending_order(pdf_dir_name):
    """ PDFが格納されているフォルダから、*.pdfの一覧をリストにして返す

    :param
        pdf_dir_name: pdfが格納されたフォルダ名

    :return
        *.pdfが含まれた一覧を昇順ソートし、リストで返す

    """
    pdf_files_ = sorted(pdf_dir_name.glob("*.pdf"))
    if not pdf_files_:
        raise NotPdfFileError(f"\n\n<{pdf_dir_name}>にPDFファイルはありません\n処理を停止しました.")

    return [file for file in pdf_files_]


def create_marge_pdf_file_name(pdf_files_):
    """
    保存ファイル名を返す（先頭と末尾のファイル名で作成）

    arg2:
        指定あり: 指定したファイル名を返す
        指定なし: 先頭と末尾のファイル名をハイフンで結合したファイル名を返す

    :param
        pdf_files_(list): pdfファイルのリスト

    :return:
        保存するファイル名を返す
    """
    args = sys.argv
    try:
        marged_pdf_name_ = args[2]
        return Path(marged_pdf_name_ + '.pdf')
    except IndexError:
        merged_file_name_ = f"{pdf_files_[0].stem}-{pdf_files_[-1].stem}.pdf"
        return Path(merged_file_name_)


def write_marge_pdf(pdf_files_, merged_file_name_):
    """
    PDFファイルを1ファイルにまとめ書き込む
    _save()を呼び出し保存する

    strict=False
        > ignore: PdfReadWarning: Superfluous whitespace found in object header b'1' b'0' [pdf.py:1666]

    :param
        pdf_files_(list):          リストにしたpdfファイル
        merged_file_name_(str):    保存するPDFファイル名

    :return
        1ファイルにしたPDFが生成し、保存する
    """

    print('<marge file list>')

    pdf_writer = PyPDF2.PdfFileWriter()
    for idx, pdf_file in enumerate(pdf_files_):
        print(f"{idx}: {pdf_file}")
        pdf_reader = PyPDF2.PdfFileReader(str(pdf_file), strict=False)
        for i in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(i))

    _save(merged_file_name_, pdf_writer)

    print(f"\nsave pdf file fullpath:\n{merged_file_name_.absolute()}\n")
    print('done')


def _save(merged_file_name_, pdf_writer):
    with open(merged_file_name_, "wb") as f:
        pdf_writer.write(f)


def help_msg():
    return """
help
-----------------------------

# PDFが格納されたフォルダを選択する。
# 選択したフォルダの中にあるPDFファイルを1ファイルに結合する.

## コマンドラインで操作

arg1: まとめたいPDFフォルダ名
arg2: 1ファイルするPDFファイル名

arg2: 指定しなかった場合
        結合されるファイル名は、先頭と末尾のファイル名をハイフンで結合したファイル名となる.

ex:
  $ python marge_pdf.py <PDF dir name> <marge PDF file name>

end  
-----------------------------
"""


def help_check(args):
    try:
        if args[1] == '-h' or args[1] == '-H':
            print(help_msg())
            sys.exit()
    except IndexError:
        print(help_msg())
        sys.exit()


def main():
    args = sys.argv

    help_check(args)
    pdf_dir = get_pdf_dir(args)
    pdf_files = create_pdf_file_list_ascending_order(pdf_dir)
    merged_file_name = create_marge_pdf_file_name(pdf_files)
    write_marge_pdf(pdf_files, merged_file_name)


if __name__ == '__main__':
    main()
