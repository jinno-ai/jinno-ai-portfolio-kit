# 🚀 改善版セットアップ手順 - jinno-ai Portfolio Kit

## 📋 概要

このドキュメントでは、**1回の設定で完了する効率的なワークフロー**を説明します。

---

## ✨ 改善ポイント

### 🔴 以前の問題点
- 毎回GitHubトークンを手動で入力する必要があった
- 状況確認とセットアップが非効率だった
- push → PR作成 → マージ を手動で実行する必要があった

### 🟢 改善後
- **GitHubトークンを1回設定すれば自動取得**
- **1コマンドでpush → PR作成 → マージまで完了**
- **効率的な状況確認ツール**
- **完全自動化されたデプロイメント**

---

## 🎯 クイックスタート（初回のみ）

### Step 1: GitHubトークンの自動セットアップ

このステップは**1回だけ**実行すれば、以降は自動的にトークンが使用されます。

```bash
cd /home/user/webapp
python3 setup_token.py
```

または、GitHubトークンを直接設定：

```bash
echo "GITHUB_TOKEN=ghp_your_token_here" > .env
chmod 600 .env
```

**トークンの取得方法：**
1. https://github.com/settings/tokens にアクセス
2. "Generate new token (classic)" をクリック
3. スコープを選択: `repo`, `workflow`
4. トークンをコピー（`ghp_`で始まる）

---

## 🚀 デプロイメント（2回目以降）

### 方法1: 完全自動デプロイ（推奨）

```bash
bash auto_deploy_all.sh
```

このコマンドは以下をすべて実行します：
1. ✅ すべてのリポジトリを取得
2. ✅ developブランチをGitHubにプッシュ
3. ✅ Pull Requestを自動作成
4. ✅ PRを自動マージ
5. ✅ developブランチを削除
6. ✅ mainブランチに切り替え

### 方法2: 個別リポジトリのデプロイ

```bash
bash deploy_single_repo.sh <repository_directory>
```

例：
```bash
bash deploy_single_repo.sh enterprise-rag-system
bash deploy_single_repo.sh llm-agent-framework
```

---

## 🛠️ 便利なツール

### 1. セットアップ状況確認

```bash
python3 check_setup.py
```

**出力例：**
```
✅ Environment: .env file found
✅ Dependencies: All installed
✅ GitHub API: Token valid
✅ Repositories: 5 ready to deploy
```

### 2. 開発ワークフロー管理

```bash
python3 dev_workflow.py
```

**機能：**
- リポジトリの状態確認
- 自動コミット
- 自動プッシュ
- PR作成支援

### 3. インタラクティブセットアップ

```bash
bash setup_and_deploy.sh
```

**機能：**
- トークンの対話的設定
- 自動デプロイメント実行
- エラーハンドリング

---

## 📁 ファイル構成

```
/home/user/webapp/
├── .env                          # GitHubトークン（自動生成）
├── .gitignore                    # .envを除外
│
├── check_setup.py                # セットアップ状況確認
├── dev_workflow.py               # 開発ワークフロー管理
├── setup_token.py                # トークン設定ツール
│
├── auto_deploy_all.sh            # 完全自動デプロイ（推奨）
├── deploy_single_repo.sh         # 個別リポジトリデプロイ
├── setup_and_deploy.sh           # インタラクティブセットアップ
│
├── IMPROVED_SETUP.md             # このファイル
├── DEPLOYMENT_RESULTS.md         # デプロイ結果
├── README_QUICK.md               # クイックリファレンス
│
└── <repositories>/               # クローンされたリポジトリ
    ├── enterprise-rag-system/
    ├── llm-agent-framework/
    ├── realtime-edge-detection/
    ├── multilingual-sentiment-analyzer/
    └── micro-instruction-engineering/
```

---

## 🔄 ワークフロー詳細

### 通常の開発フロー

```mermaid
graph LR
    A[コード修正] --> B[コミット]
    B --> C[auto_deploy_all.sh]
    C --> D[Push develop]
    D --> E[Create PR]
    E --> F[Auto-merge]
    F --> G[Switch to main]
    G --> H[完了]
```

### コマンドフロー

```bash
# 1. リポジトリをクローン（初回のみ）
git clone https://github.com/jinno-ai/enterprise-rag-system.git
cd enterprise-rag-system

# 2. developブランチで開発
git checkout -b develop
# ... コード修正 ...
git add .
git commit -m "feat: implement new feature"

# 3. 自動デプロイ（親ディレクトリから）
cd /home/user/webapp
bash auto_deploy_all.sh
```

---

## 🎯 ベストプラクティス

### 1. トークン管理

```bash
# トークンは .env ファイルに保存（自動）
GITHUB_TOKEN=ghp_xxxxxxxxxxxxx

# .gitignore に .env が含まれていることを確認
grep ".env" .gitignore
```

### 2. 定期的な状況確認

```bash
# 毎日の開発開始時に実行
python3 check_setup.py
```

### 3. エラー時の対処

```bash
# トークンが無効になった場合
python3 setup_token.py

# リポジトリの状態を確認
cd <repository>
git status
gh pr list
```

---

## 🐛 トラブルシューティング

### Issue 1: "Token is invalid"

**原因:** GitHubトークンが期限切れまたは無効

**解決策:**
```bash
python3 setup_token.py
# 新しいトークンを入力
```

### Issue 2: "PR already exists"

**原因:** 既にPRが作成されている

**解決策:**
```bash
cd <repository>
gh pr list
gh pr merge <PR番号> --merge --delete-branch
```

### Issue 3: "Permission denied"

**原因:** トークンのスコープが不足

**解決策:**
1. https://github.com/settings/tokens でトークンを確認
2. `repo` と `workflow` スコープが選択されていることを確認
3. 新しいトークンを生成して設定

---

## 📚 参考ドキュメント

- **DEPLOYMENT_RESULTS.md** - デプロイ結果の詳細
- **README_QUICK.md** - クイックリファレンス
- **IMPLEMENTATION_GUIDE.md** - 実装ガイド全体
- **TOKEN_SETUP_GUIDE.md** - トークン設定の詳細

---

## ✅ チェックリスト

### 初回セットアップ
- [ ] GitHubトークンを取得
- [ ] `python3 setup_token.py` を実行
- [ ] `.env` ファイルが作成されたことを確認
- [ ] `python3 check_setup.py` で状況確認

### デプロイメント前
- [ ] コードの変更をコミット
- [ ] `python3 check_setup.py` で状況確認
- [ ] `bash auto_deploy_all.sh` を実行

### デプロイメント後
- [ ] `DEPLOYMENT_RESULTS.md` で結果確認
- [ ] GitHubでPRがマージされたことを確認
- [ ] mainブランチが最新であることを確認

---

## 🎉 まとめ

このシステムでは、**1回の設定**で以下が自動化されます：

1. ✅ GitHubトークンの管理
2. ✅ リポジトリへのプッシュ
3. ✅ Pull Requestの作成
4. ✅ 自動マージ
5. ✅ ブランチのクリーンアップ

**次回以降は、`bash auto_deploy_all.sh` を実行するだけで完了します！**

---

**最終更新**: 2026-01-02  
**バージョン**: 2.0 (改善版)
