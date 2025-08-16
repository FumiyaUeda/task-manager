# Task Manager

Flask と SQLite を使用したシンプルかつ拡張性の高いタスク管理アプリです。  
日常業務や個人利用の効率化を目的に開発し、実務アプリとして自然なUIとわかりやすいコード構造を意識しました。

---

## 概要
- タスクの作成、編集、削除、検索、完了管理が可能
- 共通レイアウトテンプレートによるUI統一
- シンプル設計で機能追加・保守が容易

---

## 技術スタック
**Backend**
- Python 3.x
- Flask
- SQLite
- SQLAlchemy

**Frontend**
- HTML5 / CSS3
- Jinja2 テンプレートエンジン
- Bootstrap（一部UI調整に使用可能）

**Webサーバ**
- Gunicorn
- Nginx（本番環境）

---

## 設計の工夫
- **SQLAlchemy ORM** による安全で効率的なDB操作
- **テンプレート継承** で共通部分を集約し、保守性を向上
- **モジュール分割** により可読性と拡張性を確保
- シンプルなHTML構造でCSSカスタマイズを容易化

---

## 今後の拡張予定
- ユーザー認証（ログイン機能）
- 期限・タグ管理機能
- モバイルデバイス向けUI最適化
- APIエンドポイントの提供

---

## セットアップ方法（ローカル環境 / Windows PowerShell）

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
