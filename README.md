# Task Manager 📝

Flask + SQLite3 で構築したシンプルな **タスク管理アプリ** です。  
Webブラウザからタスクを登録・編集・削除し、進捗や優先度をレポート画面で確認できます。  

## 🚀 デモ画面

### 一覧画面
![一覧](docs/screenshot_index.png)

### レポート画面
![レポート](docs/screenshot_report.png)

---

## 🛠 技術スタック

- **Backend** : Python 3.11 / Flask
- **Database** : SQLite3
- **Frontend** : HTML / Jinja2 / Bootstrap 5 / CSS カスタム
- **Infra** : AWS EC2 (Ubuntu 24.04 LTS)

---

## 📌 主な機能

- ✅ タスクの新規作成・編集・削除 (CRUD)
- 🔄 完了 / 未完了 の切替
- 🎯 優先度設定 (High / Medium / Low)
- ⏰ 期限日 + 時間の指定
- 🔍 キーワード検索 (タイトル / メモ)
- 📊 レポート画面で統計表示
  - 優先度別タスク数
  - 完了率のプログレスバー

---

## ⚙️ セットアップ手順

### 1. リポジトリを取得
```bash
git clone https://github.com/FumiyaUeda/task-manager.git
cd task-manager
