# ポートフォリオ構築 作業ログ

## Day1（共通Flask雛形作成）
**目的**: 全アプリ共通で使えるFlask CRUDベースの雛形作成  
**作業内容**
- Flask + SQLite + Bootstrapの基本構造作成
- CRUD機能（Create, Read, Update, Delete）のベース実装
- requirements.txt作成
- ローカル動作確認済み
- GitHubへ初期コミット

---

## Day2（ポートフォリオ1: ユーザー管理アプリMVP完成）
**目的**: 応募用として見せられる最低限のユーザー管理アプリを完成  
**作業内容**
- Day1雛形をベースにユーザー管理テーブル作成（SQLite）
- ユーザー登録・一覧・編集・削除機能追加
- Bootstrapで最低限のUI調整
- ローカルでCRUD動作確認
- GitHubにDay2コミット

---

## Day3（EC2環境構築に変更）
**目的**: AWS EC2（Ubuntu 24.04）に開発環境を構築し、どこでも作業可能にする  
**作業内容**
- `.pem` キー配置 (`C:\Projects\aws_keys\my-ec2-key.pem`)
- EC2へSSH接続確認（ユーザー: ubuntu, リージョン: ap-southeast-2）
- 初期設定スクリプト `init_setup.sh` 作成・実行
  - パッケージ更新
  - 必須ツール（git, curl, build-essential）導入
  - タイムゾーンをAsia/Tokyoに設定
  - スワップ領域（1GB）追加
- GitHubへ途中プッシュ（README.md競合解消）
- 次回予定:
  - Python開発環境（pyenvまたはminiconda）構築
  - Flask簡易アプリ動作確認

---
