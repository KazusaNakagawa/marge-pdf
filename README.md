# merge PDF
## About
* ちょっとしたPDFファイルの結合に便利

## version
* python: 3.9.0

## Docker
* docker build
``` bash
$ docker-compose up -d
```
* docker run: bash で操作
```bash
$ docker-compose exec web bash
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
$ python merge_pdf.py <PDF dir name> <merge PDF file name>
```


