# 🚀 jinno-ai Portfolio - 開発スタートガイド

**リポジトリ作成済み・トークン設定済みの方向け**

---

## ⚡ クイックスタート（3ステップ）

### ステップ1: 現状確認

```bash
cd /home/user/webapp
python check_setup.py
```

このスクリプトが現在の状態を診断し、次にすべきことを教えてくれます。

### ステップ2: 必要に応じてトークン設定

`.env`ファイルがない場合のみ実行：

```bash
# 方法A: 対話型
bash quick_env_setup.sh

# 方法B: トークンを直接指定
bash quick_env_setup.sh ghp_your_token_here

# 方法C: 手動作成
echo "GITHUB_TOKEN=ghp_your_token_here" > .env
chmod 600 .env
```

### ステップ3: 開発ワークフローを起動

```bash
python dev_workflow.py
```

このスクリプトで以下ができます：
- 📦 リポジトリのクローン
- 📊 開発優先度の確認
- 📂 プロジェクトの状態確認
- 🎯 次にすべきタスクの表示

---

## 📚 各リポジトリの開発内容

### 1. enterprise-rag-system（最優先）

**目標**: 本格的なRAGシステムの実装

```bash
cd enterprise-rag-system

# プロジェクト構造作成
mkdir -p app/{core,api/routes,services,utils}
mkdir -p ui/{components,styles}
mkdir -p scripts tests/{unit,integration,e2e}
mkdir -p docs/images data/{documents,processed}

# 必要なファイル作成
touch app/__init__.py app/core/__init__.py
touch app/api/__init__.py app/services/__init__.py
```

**実装順序**:
1. ドキュメント読み込み機能（`scripts/ingest.py`）
2. ベクトルDB接続（`app/core/vectordb.py`）
3. 検索機能（`app/services/retrieval.py`）
4. FastAPI エンドポイント（`app/api/routes/query.py`）
5. Streamlit UI（`ui/app.py`）

### 2. llm-agent-framework（次点）

**目標**: マルチエージェントシステムの構築

```bash
cd llm-agent-framework

# プロジェクト構造
mkdir -p agent_framework/{agents,tools,utils}
mkdir -p examples tests docs

# ベースエージェントクラス
touch agent_framework/agents/base_agent.py
touch agent_framework/agents/react_agent.py
```

**実装順序**:
1. ベースエージェントクラス
2. ReActエージェント実装
3. ツール統合システム
4. エージェントオーケストレーション

### 3. realtime-edge-detection

**目標**: エッジデバイス向け物体検出

```bash
cd realtime-edge-detection

mkdir -p src/{models,utils,preprocessing}
mkdir -p scripts tests deployment
mkdir -p notebooks

# YOLO実装
touch src/models/yolo_detector.py
touch src/inference.py
```

### 4. multilingual-sentiment-analyzer

**目標**: 多言語感情分析API

```bash
cd multilingual-sentiment-analyzer

mkdir -p src/{models,api,preprocessing}
mkdir -p tests deployment

touch src/models/sentiment_model.py
touch src/api/main.py
```

### 5. micro-instruction-engineering

**目標**: プロンプト最適化フレームワーク

```bash
cd micro-instruction-engineering

mkdir -p src/{templates,evaluation,benchmarks}
mkdir -p notebooks examples

touch src/prompt_optimizer.py
touch notebooks/01_introduction.ipynb
```

---

## 🔄 開発ワークフロー

### 基本的な作業フロー

```bash
# 1. ブランチ作成
git checkout -b feature/document-ingestion

# 2. コード実装
# ... your code ...

# 3. コミット
git add .
git commit -m "feat: implement document ingestion pipeline"

# 4. プッシュ
git push origin feature/document-ingestion

# 5. PR作成（GitHubのWebUIで）
```

### コミットメッセージ規約

```
feat: 新機能追加
fix: バグ修正
docs: ドキュメント更新
test: テスト追加
refactor: リファクタリング
chore: その他の変更
```

---

## 📊 開発優先度マトリックス

| プロジェクト | 優先度 | 推定時間 | インパクト |
|-------------|--------|----------|-----------|
| enterprise-rag-system | ⭐⭐⭐⭐⭐ | 3-5日 | 非常に高い |
| llm-agent-framework | ⭐⭐⭐⭐ | 2-3日 | 高い |
| realtime-edge-detection | ⭐⭐⭐ | 2-3日 | 中 |
| multilingual-sentiment-analyzer | ⭐⭐⭐ | 2日 | 中 |
| micro-instruction-engineering | ⭐⭐ | 1-2日 | 中 |

---

## 🎯 今日の目標（Day 1）

### enterprise-rag-system

- [ ] プロジェクト構造の作成
- [ ] ドキュメント読み込みスクリプトの基本実装
- [ ] ベクトルDB接続コードの作成
- [ ] 最初のコミット＆プッシュ

### コマンド例

```bash
cd /home/user/webapp
python dev_workflow.py  # メニューから[1]を選択してRAGシステムをクローン

cd enterprise-rag-system
git checkout -b develop

# プロジェクト構造作成
mkdir -p app/{core,api/routes,services,utils}
mkdir -p ui tests/unit scripts

# 基本ファイル作成
cat > app/core/vectordb.py << 'EOF'
"""Vector database connection and operations"""

class VectorDB:
    def __init__(self, config):
        self.config = config
    
    def connect(self):
        """Connect to vector database"""
        pass
    
    def upsert(self, vectors, metadata):
        """Insert or update vectors"""
        pass
    
    def search(self, query_vector, top_k=5):
        """Search for similar vectors"""
        pass
EOF

# コミット
git add .
git commit -m "feat: initial project structure and vectordb interface"
git push origin develop
```

---

## 🛠️ 開発環境セットアップ

### 推奨ツール

```bash
# Python環境
python -m venv venv
source venv/bin/activate

# 開発ツールインストール
pip install black flake8 pytest pytest-cov
pip install pre-commit

# pre-commitフックのセットアップ
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
EOF

pre-commit install
```

---

## 📈 進捗管理

### GitHubプロジェクトボードの活用

1. 各リポジトリでProjectsを有効化
2. カンバンボード作成（To Do / In Progress / Done）
3. Issuesでタスク管理

### 週次チェックリスト

```
□ 最低5コミット（緑のマスを維持）
□ README更新
□ コードレビュー
□ テスト追加
□ ドキュメント更新
```

---

## 🆘 トラブルシューティング

### Q: リポジトリがクローンできない

```bash
# SSH設定を確認
ssh -T git@github.com

# HTTPSを使用する場合
git config --global url."https://github.com/".insteadOf git@github.com:
```

### Q: .envファイルが見つからない

```bash
# 再作成
bash quick_env_setup.sh
```

### Q: コミットエラーが出る

```bash
# ユーザー設定を確認
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 💡 効率化のヒント

### 1. エイリアス設定

```bash
# ~/.bashrc または ~/.zshrc に追加
alias gst='git status'
alias gco='git checkout'
alias gcm='git commit -m'
alias gp='git push'
alias dev='python dev_workflow.py'
alias check='python check_setup.py'
```

### 2. tmux/screen でマルチタスク

```bash
# 複数のターミナルセッションを管理
tmux new -s dev
# Ctrl+b, c で新しいウィンドウ
# Ctrl+b, n で次のウィンドウ
```

### 3. VSCode統合ターミナル

```bash
# VSCodeでワークスペースを開く
code enterprise-rag-system
```

---

## 📚 参考資料

- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Python Best Practices](https://docs.python-guide.org/)

---

## ✅ 準備完了チェック

開発を始める前に確認：

- [ ] `python check_setup.py` が全て✅
- [ ] 少なくとも1つのリポジトリをクローン済み
- [ ] Git設定完了（user.name, user.email）
- [ ] 開発ブランチを作成済み
- [ ] やるべきタスクが明確

---

**🚀 準備完了！コーディングを始めましょう！**

最初は`enterprise-rag-system`から始めることをお勧めします。

```bash
python dev_workflow.py
```
