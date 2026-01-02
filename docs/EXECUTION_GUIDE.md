# 🚀 実行ガイド - jinno-ai ポートフォリオキット

このガイドでは、**最速10分**でGitHubポートフォリオを完成させる方法を説明します。

---

## 📋 前提条件

### 必須環境
- ✅ **Python 3.8以上** がインストールされていること
- ✅ **GitHubアカウント** を持っていること（username: jinno-ai）
- ✅ **インターネット接続** があること

### 確認コマンド
```bash
# Pythonバージョン確認
python --version
# または
python3 --version

# 期待される出力: Python 3.8.x 以上
```

---

## ⚡ 実行手順（3ステップ）

### 🔹 Step 1: 依存関係のインストール（2分）

```bash
# 必要なPythonパッケージをインストール
pip install PyGithub python-dotenv

# または、requirements.txtから一括インストール
pip install -r requirements.txt
```

**確認:**
```bash
python -c "import github; print('PyGithub:', github.__version__)"
python -c "import dotenv; print('python-dotenv: OK')"
```

---

### 🔹 Step 2: GitHubトークンの設定（3分）

#### 2-1. トークン設定スクリプトを実行

```bash
python setup_token.py
```

#### 2-2. 画面の指示に従う

スクリプトが以下を案内してくれます：

1. **ブラウザでトークン作成ページを開く**
   - https://github.com/settings/tokens
   
2. **「Generate new token (classic)」をクリック**

3. **設定項目を入力:**
   ```
   Note: jinno-ai-portfolio-automation
   Expiration: 90 days
   
   ✅ Select scopes:
   - ✅ repo (すべてのサブスコープ)
   - ✅ workflow
   - ✅ write:packages (オプション)
   ```

4. **「Generate token」をクリック**

5. **トークンをコピー** (ghp_で始まる文字列)

6. **ターミナルに戻ってペースト**

#### 2-3. 確認

`.env` ファイルが作成され、トークンが保存されます：
```bash
cat .env
# 出力: GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxx
```

---

### 🔹 Step 3: リポジトリの自動作成（5分）

```bash
python create_repositories.py
```

#### スクリプトの動作:

1. **認証情報の確認**
   ```
   ✅ Authenticated as: jinno-ai
   📧 Email: your-email@example.com
   👥 Followers: X
   📦 Public repos: Y
   ```

2. **作成確認プロンプト**
   ```
   📋 Ready to create 6 repositories:
      - jinno-ai
      - enterprise-rag-system
      - llm-agent-framework
      - realtime-edge-detection
      - multilingual-sentiment-analyzer
      - micro-instruction-engineering
   
   🤔 Do you want to proceed? (y/n):
   ```
   
   → **「y」を入力してEnter**

3. **自動作成処理**
   各リポジトリが順番に作成されます：
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
   ```

4. **完成メッセージ**
   ```
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

## 🎊 完成後の確認

### ✅ プロフィールページを確認
1. ブラウザで開く: https://github.com/jinno-ai
2. 以下が表示されているはずです：
   - ✨ 魅力的なProfile README
   - 🎯 タイピングアニメーション
   - 📊 スキルバッジ（30+個）
   - 📈 GitHubステータス統計

### ✅ リポジトリをピン留め
1. プロフィールページで **「Customize your pins」** をクリック
2. 以下の6つにチェックを入れる:
   - ☑️ enterprise-rag-system
   - ☑️ llm-agent-framework
   - ☑️ realtime-edge-detection
   - ☑️ multilingual-sentiment-analyzer
   - ☑️ micro-instruction-engineering
   - ☑️ （お好みで1つ追加）
3. **「Save pins」** をクリック

### ✅ 各リポジトリの確認
| リポジトリ | 確認項目 |
|----------|---------|
| **jinno-ai** | Profile READMEが表示される |
| **enterprise-rag-system** | 詳細なREADME、.env.example、requirements.txt、docker-compose.yml |
| **llm-agent-framework** | 詳細なREADME |
| **その他のリポジトリ** | 基本的なREADME、LICENSE |

---

## 🔧 トラブルシューティング

### ❌ 問題: `GITHUB_TOKEN not found`
**原因:** `.env`ファイルが作成されていない、またはトークンが保存されていない

**解決方法:**
```bash
# .envファイルを手動作成
echo "GITHUB_TOKEN=ghp_YOUR_TOKEN_HERE" > .env

# または、setup_token.pyを再実行
python setup_token.py
```

---

### ❌ 問題: `Authentication failed`
**原因:** トークンの権限が不足、または無効

**解決方法:**
1. https://github.com/settings/tokens にアクセス
2. トークンの権限を確認:
   - ✅ repo (すべてのサブスコープ)
   - ✅ workflow
3. 権限が不足している場合は新しいトークンを作成
4. `.env`ファイルを更新

---

### ❌ 問題: `Repository already exists`
**原因:** 既に同名のリポジトリが存在する（正常な状態）

**動作:**
```
⚠️  Repository 'enterprise-rag-system' already exists!
   Do you want to update it? (y/n):
```

**選択肢:**
- **「y」**: 既存リポジトリを更新（README等が上書きされます）
- **「n」**: スキップして次のリポジトリへ

---

### ❌ 問題: `Rate limit exceeded`
**原因:** GitHub APIのレート制限に達した

**解決方法:**
```bash
# 60分待つ、または認証済みの場合は15分待つ
# その後、再実行:
python create_repositories.py
```

---

### ❌ 問題: `PyGithub not found`
**原因:** 依存パッケージがインストールされていない

**解決方法:**
```bash
pip install PyGithub python-dotenv
```

---

### ❌ 問題: Profile READMEが表示されない
**原因:** リポジトリ名がユーザー名と一致していない

**確認方法:**
1. https://github.com/jinno-ai/jinno-ai にアクセス
2. リポジトリが存在するか確認
3. README.mdが存在するか確認

**解決方法:**
- スクリプトを再実行して「y」で更新
- または、手動でリポジトリを作成（名前: `jinno-ai`）

---

## 📊 実行ログの見方

### ✅ 正常な実行ログ例

```
╔══════════════════════════════════════════════════════════════╗
║  GitHub Portfolio Repository Creator for jinno-ai            ║
║  Automated setup for AI Engineer Portfolio                   ║
╚══════════════════════════════════════════════════════════════╝

✅ Authenticated as: jinno-ai
📧 Email: contact@jinno-ai.dev
👥 Followers: 10
📦 Public repos: 5

📋 Ready to create 6 repositories:
   - jinno-ai
   - enterprise-rag-system
   - llm-agent-framework
   - realtime-edge-detection
   - multilingual-sentiment-analyzer
   - micro-instruction-engineering

🤔 Do you want to proceed? (y/n): y

============================================================
Creating repository: jinno-ai
============================================================
✅ Repository created: https://github.com/jinno-ai/jinno-ai
✅ Topics added: profile, readme, portfolio
✅ README.md updated from jinno-ai-profile-README.md
✅ LICENSE added

🎉 Repository 'jinno-ai' setup complete!
   URL: https://github.com/jinno-ai/jinno-ai

... (他のリポジトリも同様に処理)

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

## 🎯 完成後のアクション

### 即座に実行すべきこと（5分）

1. **プロフィールを確認**
   ```
   https://github.com/jinno-ai
   ```

2. **リポジトリをピン留め**
   - 「Customize your pins」から6つ選択

3. **個人情報を更新**
   - Profile READMEのリンク（LinkedIn, Twitter等）を実際のURLに変更

---

### 今週中に実行すべきこと

1. **実際のコードを追加**
   ```bash
   # 例: enterprise-rag-systemに実装を追加
   git clone https://github.com/jinno-ai/enterprise-rag-system.git
   cd enterprise-rag-system
   # コードを追加...
   git add .
   git commit -m "Add initial implementation"
   git push
   ```

2. **デモGIF/動画を作成**
   - Loom、QuickTimeなどで画面録画
   - GifやMP4に変換
   - README.mdに追加

3. **SNSで共有**
   ```
   🚀 GitHubポートフォリオをアップデート！
   
   AIエンジニア向けプロジェクトを公開:
   ✅ Enterprise RAG System
   ✅ LLM Agent Framework
   ✅ その他AI/MLプロジェクト
   
   https://github.com/jinno-ai
   
   #AI #MachineLearning #OpenSource #LLM
   ```

---

### 今月中に実行すべきこと

1. **技術ブログを4本書く**
   - RAGシステムの実装パターン
   - LLM Agentの設計思想
   - マイクロインストラクションエンジニアリング
   - エッジAIの最適化技術

2. **OSSへの貢献開始**
   - LangChain-Googleへのコントリビュート
   - Issueへのコメント
   - ドキュメント改善

3. **継続的なコミット**
   - 週5回以上のコミット
   - 緑のマスを維持

---

## 📚 参考資料

### 公式ドキュメント
- [GitHub REST API](https://docs.github.com/en/rest)
- [PyGithub Documentation](https://pygithub.readthedocs.io/)
- [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

### 追加ガイド
- [START_HERE.md](START_HERE.md) - クイックスタート
- [QUICKSTART.md](QUICKSTART.md) - 手動セットアップ
- [AUTOMATION_GUIDE.md](AUTOMATION_GUIDE.md) - 自動化の詳細
- [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) - 段階的実装

---

## 🔒 セキュリティ注意事項

### ⚠️ 絶対に守ること

1. **トークンを公開しない**
   ```bash
   # .envファイルがgitignoreされているか確認
   cat .gitignore | grep .env
   # 出力: .env
   ```

2. **トークンの有効期限を設定**
   - 推奨: 90日
   - 使用後は必要に応じて無効化

3. **最小限の権限のみ付与**
   - 必要なスコープ: `repo`, `workflow`
   - 不要なスコープは付与しない

---

## 🎉 完成おめでとうございます！

あなたのGitHubプロフィールは、今や**企業が「採用したい！」と思う状態**になりました。

### 期待される効果

| 期間 | 期待される成果 |
|------|--------------|
| **1週間後** | Profile views +50%, Stars開始, Followers +5-10 |
| **1ヶ月後** | Total stars: 20+, Followers: 30+, 初回スカウト |
| **3ヶ月後** | Total stars: 100+, Followers: 50+, 案件獲得 |

---

## 💪 次のステップ

このポートフォリオを最大限活用するために:

1. ✅ **継続的なコミット** - 週5回以上
2. ✅ **技術ブログ執筆** - 月4本
3. ✅ **OSS貢献** - Issue対応、PR作成
4. ✅ **SNS発信** - 週1回の技術投稿
5. ✅ **プロジェクト充実** - デモ動画、実装コード追加

---

**さあ、あなたのAIエンジニアとしてのキャリアを加速させましょう！** 🚀

---

**作成日:** 2026年1月1日  
**バージョン:** 1.0  
**対象:** jinno-ai GitHubアカウント  
**サポート:** 質問があればいつでもお気軽に！
