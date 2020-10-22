# marge-pdf
## About
* ちょっとしたPDFファイルの結合に便利

### Version
* python: 3.8.5

### Docker
* docker build
``` bash
$ docker build -t < Image Name >:latest .
```
* docker run
```bash
$ docker run -it --rm -v <host-path>:/python_doc < image Name > bash
```

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


