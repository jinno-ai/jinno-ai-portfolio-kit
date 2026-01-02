# 🤖 GitHub自動化ガイド - ワンコマンドでポートフォリオを構築

## 🎯 概要

このガイドでは、**Pythonスクリプトを使って全てのリポジトリを自動作成**する方法を説明します。

**所要時間:** 約10分（セットアップ5分 + 実行5分）

---

## ✅ 前提条件

- Python 3.8以上がインストールされている
- GitHubアカウントを持っている
- 基本的なターミナル操作ができる

---

## 🚀 クイックスタート（3ステップ）

### Step 1: Personal Access Tokenの取得（5分）

1. **GitHubにログイン**して以下にアクセス:
   ```
   https://github.com/settings/tokens
   ```

2. **「Generate new token (classic)」をクリック**

3. **設定を行う:**
   ```
   Token名: Portfolio Automation
   有効期限: 90 days (または希望の期間)
   
   ✅ チェックを入れるスコープ:
   □ repo (全てのサブ項目にチェック)
   □ workflow
   □ write:packages
   ```

4. **「Generate token」をクリック**

5. **トークンをコピー** (一度しか表示されません!)
   ```
   ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

---

### Step 2: スクリプトのセットアップ（3分）

#### 2-1. 必要なファイルをダウンロード

すでに提供されているファイルを使用します:
```bash
# ダウンロードしたフォルダに移動
cd /path/to/jinno-ai-github-setup
```

#### 2-2. 依存関係のインストール

```bash
# 仮想環境の作成（推奨）
python -m venv venv

# 仮想環境の有効化
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 必要なパッケージをインストール
pip install PyGithub python-dotenv
```

#### 2-3. 環境変数の設定

`.env` ファイルを作成:

```bash
# Windowsの場合
echo GITHUB_TOKEN=ghp_your_token_here > .env

# Mac/Linuxの場合
echo "GITHUB_TOKEN=ghp_your_token_here" > .env
```

または、テキストエディタで `.env` ファイルを作成して以下を記載:
```
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**⚠️ 重要:** `.env` ファイルは絶対に公開しないでください!

---

### Step 3: スクリプトの実行（2分）

```bash
# スクリプトを実行
python create_repositories.py
```

**実行すると:**
```
╔══════════════════════════════════════════════════════════════╗
║  GitHub Portfolio Repository Creator for jinno-ai            ║
║  Automated setup for AI Engineer Portfolio                   ║
╚══════════════════════════════════════════════════════════════╝

✅ Authenticated as: jinno-ai
📧 Email: your-email@example.com
👥 Followers: 5
📦 Public repos: 2

📋 Ready to create 6 repositories:
   - jinno-ai
   - enterprise-rag-system
   - llm-agent-framework
   - realtime-edge-detection
   - multilingual-sentiment-analyzer
   - micro-instruction-engineering

🤔 Do you want to proceed? (y/n): 
```

**「y」を入力してEnter**

```
============================================================
Creating repository: jinno-ai
============================================================
✅ Repository created: https://github.com/jinno-ai/jinno-ai
✅ Topics added: profile, readme, portfolio
✅ README.md updated from jinno-ai-profile-README.md
✅ LICENSE added

🎉 Repository 'jinno-ai' setup complete!
   URL: https://github.com/jinno-ai/jinno-ai

============================================================
Creating repository: enterprise-rag-system
============================================================
✅ Repository created: https://github.com/jinno-ai/enterprise-rag-system
✅ Topics added: rag, llm, langchain, vector-database, ai, machine-learning, enterprise
✅ README.md updated from enterprise-rag-system-README.md
✅ requirements.txt created
✅ docker-compose.yml created
✅ .env.example created
✅ .gitignore created
✅ LICENSE added

🎉 Repository 'enterprise-rag-system' setup complete!
   URL: https://github.com/jinno-ai/enterprise-rag-system

[... 他のリポジトリも同様に作成 ...]

============================================================
🎉 Setup Complete!
============================================================
✅ Successfully created/updated 6 repositories

📍 Your GitHub Profile: https://github.com/jinno-ai

📌 Next steps:
   1. Visit your profile to see the new README
   2. Pin your favorite repositories
   3. Start adding code to your projects
   4. Share on social media!

🚀 Your AI Engineer portfolio is ready!
```

---

## 🎊 完成! 次のステップ

### 1. プロフィールを確認
```
https://github.com/jinno-ai
```
魅力的なREADMEが表示されているはず!

### 2. リポジトリをピン留め

1. プロフィールページで「Customize your pins」をクリック
2. 以下を選択:
   - ✅ enterprise-rag-system
   - ✅ llm-agent-framework
   - ✅ realtime-edge-detection
   - ✅ multilingual-sentiment-analyzer
   - ✅ micro-instruction-engineering
   - ✅ jinno-ai (Profile README)
3. 「Save pins」をクリック

### 3. SNSで共有

**Twitter/X:**
```
🚀 GitHubポートフォリオを大幅アップデート!

AI Engineer向けに以下を公開:
✅ Enterprise RAG System
✅ LLM Agent Framework
✅ Edge Detection
✅ Sentiment Analyzer

チェックしてみてください!
https://github.com/jinno-ai

#AI #MachineLearning #OpenSource #GitHubPortfolio
```

**LinkedIn:**
```
AIエンジニアとしてのポートフォリオをGitHubで公開しました。

主なプロジェクト:
• Enterprise RAG System - 本番環境対応のRAGパイプライン
• LLM Agent Framework - マルチエージェント協調システム
• その他、Computer Vision、NLP関連プロジェクト

実装の詳細やアーキテクチャはGitHubで公開しています。
フィードバックやコラボレーションを歓迎します!

https://github.com/jinno-ai
```

---

## 🔧 トラブルシューティング

### ❌ エラー: "GITHUB_TOKEN not found"

**原因:** `.env` ファイルが正しく作成されていない

**解決方法:**
```bash
# .envファイルの内容を確認
cat .env  # Mac/Linux
type .env  # Windows

# 正しいフォーマット:
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### ❌ エラー: "Authentication failed"

**原因:** トークンが無効または権限不足

**解決方法:**
1. トークンが正しくコピーされているか確認
2. トークンの有効期限を確認
3. 必要なスコープ（repo, workflow）が選択されているか確認
4. 新しいトークンを生成して再試行

---

### ❌ エラー: "Repository already exists"

**これは正常です!** スクリプトは自動的に対応します:
```
⚠️  Repository 'enterprise-rag-system' already exists!
   Do you want to update it? (y/n):
```

- **「y」**: 既存のリポジトリを更新（READMEや設定を上書き）
- **「n」**: スキップして次へ

---

### ❌ エラー: "Rate limit exceeded"

**原因:** GitHubのAPI制限に達した

**解決方法:**
```bash
# 60分待つか、スクリプトを再実行（途中から再開可能）
python create_repositories.py
```

---

## 📝 スクリプトのカスタマイズ

### リポジトリの追加・削除

`create_repositories.py` の `REPOSITORIES` リストを編集:

```python
REPOSITORIES = [
    {
        "name": "my-new-project",
        "description": "My awesome project description",
        "topics": ["python", "ai", "machine-learning"]
    },
    # ... 他のリポジトリ
]
```

### README以外のファイルを追加

```python
{
    "name": "my-project",
    "description": "...",
    "additional_files": {
        "setup.py": "path/to/setup.py",
        "CONTRIBUTING.md": "path/to/CONTRIBUTING.md"
    }
}
```

---

## 🔒 セキュリティのベストプラクティス

### ✅ やるべきこと:
- Personal Access Tokenを `.env` ファイルに保存
- `.env` を `.gitignore` に追加
- トークンの有効期限を設定（90日推奨）
- 使用後はトークンを無効化（必要に応じて）

### ❌ やってはいけないこと:
- トークンをソースコードにハードコード
- トークンを公開リポジトリにコミット
- トークンをSNSやチャットで共有
- 無期限のトークンを作成

---

## 🎯 自動化の利点

### 手動作成と比較:

| 作業 | 手動 | 自動化 |
|-----|------|--------|
| リポジトリ作成 | 6回 × 3分 = 18分 | 1回 × 5秒 = 30秒 |
| README配置 | 6回 × 2分 = 12分 | 自動 |
| 設定ファイル追加 | 複数 × 2分 = 10分+ | 自動 |
| Topics設定 | 6回 × 1分 = 6分 | 自動 |
| LICENSE追加 | 6回 × 1分 = 6分 | 自動 |
| **合計** | **約52分** | **約5分** |

**時間節約:** 約47分（90%削減）

---

## 📚 参考リソース

- [PyGithub Documentation](https://pygithub.readthedocs.io/)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

---

## 🆘 サポート

問題が発生した場合:

1. **エラーメッセージを確認**
2. **このガイドのトラブルシューティングセクションを参照**
3. **GitHub API Status を確認**: https://www.githubstatus.com/
4. **それでも解決しない場合は、質問してください!**

---

## 🎉 成功!

**自動化スクリプトで、あなたのGitHubポートフォリオは数分で完成しました!**

次は:
1. ✅ プロフィールの確認
2. ✅ リポジトリのピン留め
3. ✅ 実際のコードを追加開始
4. ✅ SNSで共有してネットワーク構築

**素晴らしいポートフォリオの完成です! 🚀**
