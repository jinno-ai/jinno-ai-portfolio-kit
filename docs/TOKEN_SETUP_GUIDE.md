# 🔑 GitHubトークン設定ガイド

このガイドでは、jinno-aiのGitHubポートフォリオを自動作成するために必要な**GitHub Personal Access Token**の取得方法を説明します。

---

## 📋 手順1: GitHubトークンの作成

### 1.1 GitHubの設定ページにアクセス

以下のURLをブラウザで開いてください（GitHubにログインした状態で）：

👉 **https://github.com/settings/tokens**

### 1.2 新しいトークンを生成

1. **"Generate new token (classic)"** ボタンをクリック
2. パスワードの再入力を求められる場合があります

### 1.3 トークンの設定

以下の項目を設定してください：

#### **Note（メモ）**
```
Portfolio Automation for jinno-ai
```

#### **Expiration（有効期限）**
```
90 days（推奨）
```

#### **Select scopes（権限の選択）**

以下の項目にチェックを入れてください：

✅ **repo** ← これをクリックすると、以下のサブ項目すべてが自動選択されます
   - repo:status
   - repo_deployment
   - public_repo
   - repo:invite
   - security_events

✅ **workflow** ← GitHub Actionsの設定用

✅ **write:packages** ← パッケージの公開用（オプション）

### 1.4 トークンの生成

1. ページの一番下までスクロール
2. **"Generate token"** ボタンをクリック

### 1.5 トークンのコピー

⚠️ **重要！** トークンは一度しか表示されません！

1. 表示されたトークンをコピー（`ghp_`で始まる40文字以上の文字列）
2. 例: `ghp_1234567890abcdefghijklmnopqrstuvwxyz1234`

---

## 📋 手順2: トークンの設定

トークンを取得したら、以下の**いずれかの方法**で設定してください。

### 方法A: 対話型セットアップ（推奨）🌟

このスクリプトを実行すると、対話的にトークンを設定できます：

```bash
cd /home/user/webapp
python setup_token.py
```

スクリプトの指示に従って、コピーしたトークンを貼り付けてください。

### 方法B: 手動で.envファイルを作成

1. `/home/user/webapp`ディレクトリに`.env`ファイルを作成
2. 以下の内容を記入（`your_token_here`を実際のトークンに置き換える）：

```
GITHUB_TOKEN=ghp_your_actual_token_here
```

3. ファイルを保存

---

## 📋 手順3: リポジトリの自動作成

トークンの設定が完了したら、以下のコマンドを実行してください：

```bash
cd /home/user/webapp
python create_repositories.py
```

このスクリプトが自動的に以下を実行します：

1. ✅ **jinno-ai** - プロフィールREADMEリポジトリ
2. ✅ **enterprise-rag-system** - RAGシステム
3. ✅ **llm-agent-framework** - エージェントフレームワーク
4. ✅ **realtime-edge-detection** - リアルタイム物体検出
5. ✅ **multilingual-sentiment-analyzer** - 多言語感情分析
6. ✅ **micro-instruction-engineering** - プロンプト最適化

各リポジトリには以下が自動設定されます：
- README.md（完成版）
- LICENSE（MIT）
- トピックタグ
- 必要なファイル（requirements.txt、docker-compose.yml等）

---

## 🔒 セキュリティに関する注意事項

### ⚠️ トークンを安全に保つために：

1. **絶対に公開しない**
   - GitHubにコミットしない（`.env`は`.gitignore`に含まれています）
   - SNSやチャットに貼り付けない
   - スクリーンショットを共有しない

2. **トークンが漏洩した場合**
   - すぐに https://github.com/settings/tokens でトークンを削除
   - 新しいトークンを作成し直す

3. **定期的な更新**
   - 90日後に有効期限が切れるので、その時に新しいトークンを作成

---

## 🆘 トラブルシューティング

### Q: トークンが無効と表示される
**A:** 以下を確認してください：
- トークンが正しくコピーされているか（余分なスペースがないか）
- 必要な権限（repo、workflow）が選択されているか
- トークンの有効期限が切れていないか

### Q: リポジトリがすでに存在する
**A:** スクリプトが既存のリポジトリを検出すると、更新するか確認します。`y`を入力すると既存のREADMEを更新します。

### Q: `.env`ファイルが見つからない
**A:** 以下を実行して確認してください：
```bash
cd /home/user/webapp
ls -la .env
```
ファイルが存在しない場合は、手動で作成してください。

---

## ✅ 確認チェックリスト

作業を開始する前に、以下を確認してください：

- [ ] GitHubにログインしている
- [ ] Personal Access Tokenを作成した
- [ ] トークンをコピーした（`ghp_`で始まる）
- [ ] 必要な権限（repo、workflow）を選択した
- [ ] `.env`ファイルにトークンを設定した
- [ ] PyGithubとpython-dotenvをインストールした（`pip install PyGithub python-dotenv`）

---

## 🚀 準備完了！

すべての準備が整ったら、以下のコマンドを実行してポートフォリオを作成しましょう：

```bash
cd /home/user/webapp
python create_repositories.py
```

作成完了後、あなたのGitHubプロフィールを確認してください：
👉 **https://github.com/jinno-ai**

魅力的なAIエンジニアポートフォリオの完成です！🎉

---

質問がある場合は、お気軽にお問い合わせください。
