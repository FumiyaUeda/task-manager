# Flask CRUD MVP

最短で応募用のポートフォリオを公開するための Flask + SQLite CRUD アプリの雛形です。

## ローカル起動 (Windows PowerShell)

```powershell
# 1) 仮想環境
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip

# 2) 依存関係
pip install -r requirements.txt

# 3) 起動
python app.py
# ブラウザ: http://127.0.0.1:5000/
```

## 本番 (EC2 予定コマンド例)

```bash
# Ubuntu 例
sudo apt update && sudo apt install -y python3-pip python3-venv nginx
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# Gunicorn 起動例
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```

Nginx のリバースプロキシ設定と systemd のサービス化は後続タスクで対応します。

## 機能
- アイテムの一覧 / 作成 / 編集 / 削除
- タイトル・メモの簡易検索

## 構成
- `app.py`: Flask アプリ本体（SQLAlchemy 使用）
- `templates/`: HTML テンプレート
- `static/`: CSS など静的ファイル
- `requirements.txt`: 依存パッケージ
- `.gitignore`

---

※構成図やスクリーンショットは別途追加予定です。
