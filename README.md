# marge-pdf
## About
* ちょっとしたPDFファイルの結合に便利

### Version
* python: 3.8.5

### pip install
* PyPDF2==1.26.0

## Usage

* PDFが格納されたフォルダを選択する。
* 選択したフォルダの中にあるPDFファイルを1ファイルに結合する.

### ターミナルで操作

- arg2: 指定しなかった場合
  - 結合されるファイル名は、先頭と末尾のファイル名をハイフンで結合したファイル名となる.

- arg1: まとめたいPDF Dir Name
- arg2: 1ファイルするPDF file Name

``` bash
# 実行コマンド
$ python marge_pdf.py <PDF dir name> <marge PDF file name>
```


