<h2 align="center">Mario Kart Wii Codes for Python (Dolphin only)</h2>

## 〈Overview〉
Pythonを使ったMKWのチートプログラムを作るためのテンプレートと、その簡単な例のセットです。<br>
自動でゲーム・リージョンの判別を行ってくれるため、アドレスさえ追加すれば、リージョンごとに分岐を作る必要はありません。<br>
<br>
※プログラム自体はPythonだけで作れますが、値の読み書きにはPowerPCの知識が必要になります。<br>
※Pythonプログラムであるため、実機での使用はできません。

## 〈Download〉
Codeと書かれた緑のボタンから、Download ZIPを押してZIPファイルをダウンロードするか、<br>
以下のコマンドを実行してリポジトリをクローンしてください。
```bash
git clone https://github.com/Mrmkroll/mkw-codes-python.git
```

## 〈Requirements〉
- <a href="https://www.python.jp/">Python 3.X</a>
- <a href="https://github.com/dolphin-emu/dolphin">Dolphine Emulator</a>
- <a href="https://github.com/aldelaro5/Dolphin-memory-engine">Dolphin Memory Engine</a>
- <a href="https://github.com/henriquegemignani/py-dolphin-memory-engine">Python Dolphin Memory Engine</a>
- PowerPC, Pythonの知識

## 〈Usage〉
1. DolphinでMKWを起動
2. DMEを起動、HookされていなければHookをクリック
3. 使用したいPythonプログラムを起動

<br>
プログラムの初めには必ず以下の内容を書き込んでください。

```python
from lib import fun as fn
from lib import ppc

fn.hook()
```

### ppc.py
PowerPCにあるニーモニックを模した関数が定義されており、既存のニーモニックと同様の感覚で操作することができます。<br>
### fun.py
既存のPowerPCにはないオリジナルのニーモニック風関数と、いくつかの補助的関数が定義されています。<br>
<br>
*※fn.hook()内のプログラムとsymbolフォルダ内のアドレスを書き換えることで、MKW以外のWiiソフト用プログラムを作ることができます。*

## 〈Developer〉
- Mrmk
- sow