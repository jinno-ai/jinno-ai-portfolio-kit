# 🚀 jinno-ai GitHub ポートフォリオ実装ガイド（詳細版）

## 📋 概要

このガイドでは、jinno-aiアカウントで魅力的なAIエンジニアポートフォリオを構築するための**具体的な実装手順**を、ステップバイステップで詳細に説明します。

### 🎯 このガイドで達成できること

- プロフェッショナルなGitHubプロフィールの構築
- 6つの高品質AIプロジェクトリポジトリの作成
- 技術的なアーキテクチャ設計の理解
- 採用担当者に響くポートフォリオの完成

### 📊 全体スケジュール

| Phase | 内容 | 所要時間 | 優先度 |
|-------|------|----------|--------|
| Phase 1 | Profile README作成 | 1-2時間 | 🔴 最優先 |
| Phase 2 | Enterprise RAG System | 2-3日 | 🔴 最優先 |
| Phase 3 | LLM Agent Framework | 2-3日 | 🟡 高 |
| Phase 4 | 追加プロジェクト（4つ） | 各1-2日 | 🟢 中 |
| Phase 5-9 | 品質向上・プロモーション | 継続的 | 🟢 中 |

---

## ✅ Phase 1: Profile README作成（最優先）

### 🎯 目標

GitHubプロフィールページに表示される魅力的なREADMEを作成し、訪問者に強い第一印象を与える。

### Step 1-1: Profile READMEリポジトリの作成

#### 1.1.1 GitHubにログイン

1. ブラウザで [https://github.com](https://github.com) にアクセス
2. 右上の「Sign in」をクリック
3. ユーザー名とパスワードを入力してログイン

#### 1.1.2 新規リポジトリ作成画面へ移動

1. 右上の「+」アイコンをクリック
2. ドロップダウンから「New repository」を選択

#### 1.1.3 リポジトリ設定

以下の設定で新規リポジトリを作成：

| 項目 | 設定値 | 説明 |
|------|--------|------|
| Repository name | `jinno-ai` | ⚠️ **必ずユーザー名と完全一致させる** |
| Description | `My GitHub Profile` | 任意の説明文 |
| Visibility | `Public` | 公開設定（必須） |
| Initialize | ✅ Add a README file | チェックを入れる |

```text
⚠️ 重要: リポジトリ名がユーザー名と一致しないと、Profile READMEとして認識されません！
```

#### 1.1.4 作成完了の確認

「Create repository」ボタンをクリック後、以下を確認：
- リポジトリページに「jinno-ai/jinno-ai is a ✨ special ✨ repository」と表示される
- これが表示されれば、Profile READMEとして正しく認識されています

### Step 1-2: README.mdの更新

#### 1.2.1 編集画面を開く

1. 作成したリポジトリの `README.md` ファイルをクリック
2. 右上の鉛筆アイコン（Edit this file）をクリック

#### 1.2.2 コンテンツの貼り付け

1. このキットに含まれる `jinno-ai-profile-README.md` を開く
2. 全内容をコピー（Ctrl+A → Ctrl+C）
3. GitHub編集画面に貼り付け（Ctrl+V）

#### 1.2.3 コミット

1. 画面下部の「Commit changes」セクションへスクロール
2. コミットメッセージ: `Update profile README with professional content`
3. 「Commit changes」ボタンをクリック

### Step 1-3: カスタマイズ（必須）

以下の箇所を実際の情報に変更してください：

```markdown
# 変更必須箇所一覧

## SNSリンク（実際のURLに変更）
- LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN
- Twitter: https://twitter.com/YOUR_TWITTER
- Medium: https://medium.com/@YOUR_MEDIUM
- Portfolio: https://YOUR_PORTFOLIO_URL
- Email: YOUR_EMAIL@example.com

## 統計情報（ユーザー名を変更）
- github-readme-stats のURL内 `username=jinno-ai` を自分のユーザー名に
- github-readme-streak-stats のURL内 `user=jinno-ai` を自分のユーザー名に
```

### Step 1-4: 動作確認

1. GitHubプロフィールページ（`https://github.com/jinno-ai`）にアクセス
2. 作成したREADMEが表示されていることを確認
3. 各バッジ、統計情報が正しく表示されていることを確認

```text
✅ チェックリスト:
□ タイピングアニメーションが動作している
□ Tech Stackのバッジが表示されている
□ GitHub Statsが表示されている
□ SNSリンクが正しく機能する
```

---

## ✅ Phase 2: Enterprise RAG System リポジトリの作成

### 🎯 目標

本格的なRAG（Retrieval-Augmented Generation）システムのリポジトリを作成し、AIエンジニアとしての技術力を示す。

### 📐 アーキテクチャ概要

```text
┌─────────────────────────────────────────────────────────────────┐
│                    Enterprise RAG System                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│  │   User      │───▶│  FastAPI    │───▶│  Query      │        │
│  │   Query     │    │  Endpoint   │    │  Processor  │        │
│  └─────────────┘    └─────────────┘    └──────┬──────┘        │
│                                               │                │
│                     ┌─────────────────────────┼────────────┐   │
│                     │                         ▼            │   │
│                     │  ┌─────────────┐  ┌─────────────┐   │   │
│                     │  │  Semantic   │  │   BM25      │   │   │
│                     │  │  Search     │  │   Search    │   │   │
│                     │  │  (Vector)   │  │  (Keyword)  │   │   │
│                     │  └──────┬──────┘  └──────┬──────┘   │   │
│                     │         │                │          │   │
│                     │         └────────┬───────┘          │   │
│                     │                  ▼                  │   │
│                     │         ┌─────────────┐             │   │
│                     │         │  RRF Fusion │             │   │
│                     │         │  (Hybrid)   │             │   │
│                     │         └──────┬──────┘             │   │
│                     │                │                    │   │
│                     │    Retrieval   │   Layer            │   │
│                     └────────────────┼────────────────────┘   │
│                                      ▼                        │
│                            ┌─────────────┐                    │
│                            │  Re-Ranker  │                    │
│                            │  (Cross-    │                    │
│                            │   Encoder)  │                    │
│                            └──────┬──────┘                    │
│                                   ▼                           │
│                            ┌─────────────┐                    │
│                            │  Context    │                    │
│                            │ Compressor  │                    │
│                            └──────┬──────┘                    │
│                                   ▼                           │
│                            ┌─────────────┐                    │
│                            │    LLM      │                    │
│                            │  (GPT-4/    │                    │
│                            │   Claude)   │                    │
│                            └──────┬──────┘                    │
│                                   ▼                           │
│                            ┌─────────────┐                    │
│                            │  Response   │                    │
│                            │  + Sources  │                    │
│                            └─────────────┘                    │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### 📊 技術スタック詳細

| レイヤー | 技術 | 役割 | 選定理由 |
|----------|------|------|----------|
| **API** | FastAPI | RESTful API | 高速、型安全、自動ドキュメント生成 |
| **UI** | Streamlit | デモインターフェース | 迅速なプロトタイピング、Pythonネイティブ |
| **Embedding** | OpenAI Ada-002 | ベクトル化 | 高品質、1536次元、多言語対応 |
| **Vector DB** | Pinecone | 類似検索 | マネージド、スケーラブル、低レイテンシ |
| **Keyword Search** | BM25 | キーワード検索 | 軽量、高速、専門用語に強い |
| **Re-Ranker** | Cross-Encoder | 精度向上 | 文脈理解、関連性スコアリング |
| **LLM** | GPT-4 / Claude | 回答生成 | 高品質な自然言語生成 |
| **Cache** | Redis | 応答キャッシュ | 低レイテンシ、TTL管理 |
| **Monitoring** | LangSmith | デバッグ・監視 | LangChain公式、詳細トレース |

### Step 2-1: リポジトリ作成

#### 2.1.1 GitHub上で新規リポジトリを作成

1. GitHubにログイン
2. 右上の「+」→「New repository」をクリック
3. 以下の設定で作成：

| 項目 | 設定値 |
|------|--------|
| Repository name | `enterprise-rag-system` |
| Description | `Production-grade RAG pipeline for enterprise knowledge bases` |
| Visibility | `Public` |
| Initialize | ✅ Add a README file |
| .gitignore | `Python` を選択 |
| License | `MIT License` を選択 |

4. 「Create repository」をクリック

### Step 2-2: ローカル環境セットアップ

#### 2.2.1 リポジトリをクローン

```bash
# ホームディレクトリまたは作業ディレクトリに移動
cd ~/projects  # または任意のディレクトリ

# リポジトリをクローン
git clone https://github.com/jinno-ai/enterprise-rag-system.git

# ディレクトリに移動
cd enterprise-rag-system
```

#### 2.2.2 Python仮想環境の作成（推奨）

```bash
# Python仮想環境を作成
python -m venv venv

# 仮想環境を有効化
# Linux/Mac:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# pipをアップグレード
pip install --upgrade pip
```

### Step 2-3: プロジェクト構造の作成

#### 2.3.1 ディレクトリ構造

以下のコマンドで完全なディレクトリ構造を作成：

```bash
# メインアプリケーション構造
mkdir -p app/core
mkdir -p app/api/routes
mkdir -p app/services
mkdir -p app/utils
mkdir -p app/models

# UI関連
mkdir -p ui/components
mkdir -p ui/styles

# スクリプト・ツール
mkdir -p scripts

# テスト構造
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p tests/e2e
mkdir -p tests/fixtures

# ドキュメント
mkdir -p docs/images
mkdir -p docs/api

# Jupyter Notebooks
mkdir -p notebooks

# デプロイメント設定
mkdir -p deployment/kubernetes
mkdir -p deployment/terraform
mkdir -p deployment/docker

# データディレクトリ
mkdir -p data/documents
mkdir -p data/processed
mkdir -p data/evaluation

# GitHub Actions
mkdir -p .github/workflows
```

#### 2.3.2 Pythonパッケージ初期化ファイル

```bash
# __init__.py ファイルを作成（Pythonパッケージとして認識させる）
touch app/__init__.py
touch app/core/__init__.py
touch app/api/__init__.py
touch app/api/routes/__init__.py
touch app/services/__init__.py
touch app/utils/__init__.py
touch app/models/__init__.py
touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py
```

#### 2.3.3 最終的なディレクトリ構造

```text
enterprise-rag-system/
├── .github/
│   └── workflows/
│       ├── test.yml           # 自動テスト
│       └── lint.yml           # コード品質チェック
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPIエントリーポイント
│   ├── config.py              # 設定管理
│   ├── core/
│   │   ├── __init__.py
│   │   ├── embeddings.py      # Embeddingモデル
│   │   ├── retriever.py       # 検索ロジック
│   │   ├── reranker.py        # Re-ranking
│   │   └── generator.py       # LLM回答生成
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py            # 依存性注入
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── query.py       # クエリエンドポイント
│   │       ├── ingest.py      # ドキュメント取り込み
│   │       └── health.py      # ヘルスチェック
│   ├── services/
│   │   ├── __init__.py
│   │   ├── document_processor.py  # ドキュメント処理
│   │   ├── vector_store.py        # ベクトルDB操作
│   │   └── cache.py               # キャッシュ管理
│   ├── models/
│   │   ├── __init__.py
│   │   ├── schemas.py         # Pydanticスキーマ
│   │   └── database.py        # DBモデル
│   └── utils/
│       ├── __init__.py
│       ├── logging.py         # ロギング設定
│       └── metrics.py         # メトリクス収集
├── ui/
│   ├── app.py                 # Streamlitメインアプリ
│   ├── components/
│   │   ├── chat.py            # チャットUI
│   │   └── sidebar.py         # サイドバー
│   └── styles/
│       └── custom.css         # カスタムCSS
├── scripts/
│   ├── ingest.py              # ドキュメント取り込みスクリプト
│   ├── init_vectordb.py       # ベクトルDB初期化
│   └── evaluate.py            # 評価スクリプト
├── tests/
│   ├── __init__.py
│   ├── conftest.py            # pytest設定
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_embeddings.py
│   │   └── test_retriever.py
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_api.py
│   └── e2e/
│       └── test_full_pipeline.py
├── docs/
│   ├── README.md              # ドキュメントトップ
│   ├── architecture.md        # アーキテクチャ詳細
│   ├── api.md                 # API仕様
│   └── images/
│       └── demo.gif           # デモGIF
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_evaluation.ipynb
├── deployment/
│   ├── kubernetes/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── terraform/
│   │   └── main.tf
│   └── docker/
│       └── Dockerfile.prod
├── data/
│   ├── documents/             # 元ドキュメント
│   ├── processed/             # 処理済みデータ
│   └── evaluation/            # 評価データセット
├── .env.example               # 環境変数テンプレート
├── .gitignore                 # Git除外設定
├── docker-compose.yml         # Docker Compose設定
├── Dockerfile                 # APIコンテナ
├── Dockerfile.streamlit       # UIコンテナ
├── requirements.txt           # Python依存関係
├── requirements-dev.txt       # 開発用依存関係
├── pyproject.toml             # プロジェクト設定
├── README.md                  # プロジェクトREADME
├── CONTRIBUTING.md            # コントリビューションガイド
└── LICENSE                    # MITライセンス
```

### Step 2-4: 重要ファイルの配置

#### 2.4.1 README.mdの配置

```bash
# このキットのREADMEをコピー
cp /path/to/jinno-ai-portfolio-kit/enterprise-rag-system-README.md README.md
```

#### 2.4.2 requirements.txtの配置

```bash
# 依存関係ファイルをコピー
cp /path/to/jinno-ai-portfolio-kit/requirements.txt .
```

#### 2.4.3 docker-compose.ymlの配置

```bash
# Docker Compose設定をコピー
cp /path/to/jinno-ai-portfolio-kit/docker-compose.yml .
```

#### 2.4.4 環境変数テンプレートの作成

`.env.example` ファイルを作成：

```bash
cat > .env.example << 'EOF'
# ===========================================
# Enterprise RAG System - Environment Variables
# ===========================================

# LLM API Keys
OPENAI_API_KEY=sk-your-openai-api-key-here
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here

# Vector Database (Pinecone)
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENVIRONMENT=us-west1-gcp
PINECONE_INDEX_NAME=enterprise-rag

# Embedding Configuration
EMBEDDING_MODEL=text-embedding-ada-002
EMBEDDING_DIMENSION=1536

# Search Configuration
HYBRID_SEARCH_ALPHA=0.5
TOP_K_RESULTS=5
RERANKER_MODEL=cross-encoder/ms-marco-MiniLM-L-12-v2

# Cache Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
ENABLE_CACHING=true
CACHE_TTL_SECONDS=3600

# Database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=raguser
POSTGRES_PASSWORD=changeme
POSTGRES_DB=ragdb

# Monitoring
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=enterprise-rag
ARIZE_API_KEY=your-arize-api-key

# Application
DEBUG=false
LOG_LEVEL=INFO
MAX_WORKERS=4
EOF
```

### Step 2-5: コアファイルの実装

#### 2.5.1 FastAPIメインアプリケーション（app/main.py）

```python
"""
Enterprise RAG System - Main Application
Production-grade RAG pipeline for enterprise knowledge bases
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.routes import query, ingest, health
from app.config import settings
from app.utils.logging import setup_logging

# Setup logging
logger = setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan management"""
    # Startup
    logger.info("Starting Enterprise RAG System...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    yield
    # Shutdown
    logger.info("Shutting down Enterprise RAG System...")


app = FastAPI(
    title="Enterprise RAG System",
    description="Production-grade RAG pipeline for enterprise knowledge bases",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["Health"])
app.include_router(query.router, prefix="/api/v1", tags=["Query"])
app.include_router(ingest.router, prefix="/api/v1", tags=["Ingest"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Enterprise RAG System API",
        "version": "1.0.0",
        "docs": "/docs",
    }
```

#### 2.5.2 設定管理（app/config.py）

```python
"""
Configuration management using Pydantic Settings
"""

from pydantic_settings import BaseSettings
from typing import List
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""
    
    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    
    # API Keys
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    
    # Vector Database
    PINECONE_API_KEY: str = ""
    PINECONE_ENVIRONMENT: str = "us-west1-gcp"
    PINECONE_INDEX_NAME: str = "enterprise-rag"
    
    # Embedding
    EMBEDDING_MODEL: str = "text-embedding-ada-002"
    EMBEDDING_DIMENSION: int = 1536
    
    # Search
    HYBRID_SEARCH_ALPHA: float = 0.5
    TOP_K_RESULTS: int = 5
    RERANKER_MODEL: str = "cross-encoder/ms-marco-MiniLM-L-12-v2"
    
    # Cache
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    ENABLE_CACHING: bool = True
    CACHE_TTL_SECONDS: int = 3600
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8501"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()


settings = get_settings()
```

#### 2.5.3 Pydanticスキーマ（app/models/schemas.py）

```python
"""
Pydantic schemas for request/response validation
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class QueryRequest(BaseModel):
    """Query request schema"""
    query: str = Field(..., min_length=1, max_length=1000, description="User query")
    collection: str = Field(default="default", description="Document collection name")
    top_k: int = Field(default=5, ge=1, le=20, description="Number of results")
    include_sources: bool = Field(default=True, description="Include source documents")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "What is our company policy on remote work?",
                "collection": "hr-policies",
                "top_k": 5,
                "include_sources": True
            }
        }


class Source(BaseModel):
    """Source document schema"""
    document: str
    page: Optional[int] = None
    relevance_score: float
    text: str


class QueryResponse(BaseModel):
    """Query response schema"""
    answer: str
    sources: List[Source]
    confidence: float = Field(ge=0, le=1)
    latency_ms: int
    tokens_used: int
    cached: bool = False


class IngestRequest(BaseModel):
    """Document ingestion request"""
    source_path: str
    collection: str = "default"
    chunk_size: int = Field(default=1000, ge=100, le=4000)
    chunk_overlap: int = Field(default=200, ge=0, le=500)


class IngestResponse(BaseModel):
    """Document ingestion response"""
    status: str
    documents_processed: int
    chunks_created: int
    collection: str
    timestamp: datetime


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    version: str
    services: dict
```

#### 2.5.4 クエリAPIルート（app/api/routes/query.py）

```python
"""
Query API endpoints
"""

from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
import time

from app.models.schemas import QueryRequest, QueryResponse, Source
from app.core.retriever import HybridRetriever
from app.core.generator import ResponseGenerator
from app.services.cache import CacheService
from app.config import settings

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
async def query_documents(
    request: QueryRequest,
    retriever: HybridRetriever = Depends(),
    generator: ResponseGenerator = Depends(),
    cache: CacheService = Depends(),
):
    """
    Query the RAG system with a natural language question.
    
    - **query**: The question to ask
    - **collection**: Document collection to search
    - **top_k**: Number of relevant documents to retrieve
    - **include_sources**: Whether to include source citations
    """
    start_time = time.time()
    
    # Check cache
    if settings.ENABLE_CACHING:
        cached_response = await cache.get(request.query, request.collection)
        if cached_response:
            cached_response.cached = True
            return cached_response
    
    try:
        # Retrieve relevant documents
        documents = await retriever.retrieve(
            query=request.query,
            collection=request.collection,
            top_k=request.top_k,
        )
        
        if not documents:
            raise HTTPException(
                status_code=404,
                detail="No relevant documents found for the query"
            )
        
        # Generate response
        response = await generator.generate(
            query=request.query,
            documents=documents,
        )
        
        # Calculate latency
        latency_ms = int((time.time() - start_time) * 1000)
        
        # Build response
        result = QueryResponse(
            answer=response.answer,
            sources=[
                Source(
                    document=doc.metadata.get("source", "Unknown"),
                    page=doc.metadata.get("page"),
                    relevance_score=doc.score,
                    text=doc.content[:500],
                )
                for doc in documents
            ] if request.include_sources else [],
            confidence=response.confidence,
            latency_ms=latency_ms,
            tokens_used=response.tokens_used,
        )
        
        # Cache response
        if settings.ENABLE_CACHING:
            await cache.set(request.query, request.collection, result)
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

#### 2.5.5 ハイブリッド検索（app/core/retriever.py）

```python
"""
Hybrid Retriever combining semantic and keyword search
"""

from typing import List, Optional
from dataclasses import dataclass
import numpy as np

from langchain_openai import OpenAIEmbeddings
from langchain_community.retrievers import BM25Retriever
from pinecone import Pinecone

from app.config import settings


@dataclass
class RetrievedDocument:
    """Retrieved document with metadata"""
    content: str
    metadata: dict
    score: float


class HybridRetriever:
    """
    Hybrid retriever combining:
    - Semantic search (dense vectors via Pinecone)
    - Keyword search (BM25)
    - Reciprocal Rank Fusion for result merging
    """
    
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model=settings.EMBEDDING_MODEL,
            openai_api_key=settings.OPENAI_API_KEY,
        )
        self.pinecone = Pinecone(api_key=settings.PINECONE_API_KEY)
        self.index = self.pinecone.Index(settings.PINECONE_INDEX_NAME)
        self.alpha = settings.HYBRID_SEARCH_ALPHA  # 0=keyword, 1=semantic
    
    async def retrieve(
        self,
        query: str,
        collection: str,
        top_k: int = 5,
    ) -> List[RetrievedDocument]:
        """
        Retrieve documents using hybrid search
        
        Args:
            query: User query
            collection: Document collection name
            top_k: Number of results to return
            
        Returns:
            List of retrieved documents with scores
        """
        # Get semantic search results
        semantic_results = await self._semantic_search(query, collection, top_k * 2)
        
        # Get keyword search results
        keyword_results = await self._keyword_search(query, collection, top_k * 2)
        
        # Merge using Reciprocal Rank Fusion
        merged_results = self._reciprocal_rank_fusion(
            semantic_results,
            keyword_results,
            k=60,  # RRF constant
        )
        
        return merged_results[:top_k]
    
    async def _semantic_search(
        self,
        query: str,
        collection: str,
        top_k: int,
    ) -> List[RetrievedDocument]:
        """Perform semantic search using vector similarity"""
        # Generate query embedding
        query_embedding = self.embeddings.embed_query(query)
        
        # Search Pinecone
        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            namespace=collection,
            include_metadata=True,
        )
        
        return [
            RetrievedDocument(
                content=match.metadata.get("text", ""),
                metadata=match.metadata,
                score=match.score,
            )
            for match in results.matches
        ]
    
    async def _keyword_search(
        self,
        query: str,
        collection: str,
        top_k: int,
    ) -> List[RetrievedDocument]:
        """Perform keyword search using BM25"""
        # Implementation depends on your document store
        # This is a placeholder for BM25 search
        return []
    
    def _reciprocal_rank_fusion(
        self,
        semantic_results: List[RetrievedDocument],
        keyword_results: List[RetrievedDocument],
        k: int = 60,
    ) -> List[RetrievedDocument]:
        """
        Merge results using Reciprocal Rank Fusion
        
        RRF Score = Σ 1 / (k + rank)
        """
        doc_scores = {}
        
        # Score semantic results
        for rank, doc in enumerate(semantic_results):
            doc_id = doc.metadata.get("id", doc.content[:100])
            rrf_score = self.alpha * (1 / (k + rank + 1))
            doc_scores[doc_id] = doc_scores.get(doc_id, 0) + rrf_score
            doc_scores[f"{doc_id}_doc"] = doc
        
        # Score keyword results
        for rank, doc in enumerate(keyword_results):
            doc_id = doc.metadata.get("id", doc.content[:100])
            rrf_score = (1 - self.alpha) * (1 / (k + rank + 1))
            doc_scores[doc_id] = doc_scores.get(doc_id, 0) + rrf_score
            if f"{doc_id}_doc" not in doc_scores:
                doc_scores[f"{doc_id}_doc"] = doc
        
        # Sort by RRF score
        sorted_docs = sorted(
            [(k, v) for k, v in doc_scores.items() if not k.endswith("_doc")],
            key=lambda x: x[1],
            reverse=True,
        )
        
        return [
            RetrievedDocument(
                content=doc_scores[f"{doc_id}_doc"].content,
                metadata=doc_scores[f"{doc_id}_doc"].metadata,
                score=score,
            )
            for doc_id, score in sorted_docs
        ]
```

### Step 2-6: Streamlit UI（ui/app.py）

```python
"""
Streamlit UI for Enterprise RAG System
"""

import streamlit as st
import requests
from typing import Optional

# Page configuration
st.set_page_config(
    page_title="Enterprise RAG System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        margin-bottom: 1rem;
    }
    .source-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .confidence-high { color: #4CAF50; }
    .confidence-medium { color: #FF9800; }
    .confidence-low { color: #F44336; }
</style>
""", unsafe_allow_html=True)

# API configuration
API_BASE_URL = st.secrets.get("API_BASE_URL", "http://localhost:8000")


def query_rag_system(
    query: str,
    collection: str,
    top_k: int,
) -> Optional[dict]:
    """Send query to RAG API"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/v1/query",
            json={
                "query": query,
                "collection": collection,
                "top_k": top_k,
                "include_sources": True,
            },
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error querying API: {str(e)}")
        return None


# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=RAG+System", width=150)
    st.markdown("---")
    
    st.subheader("⚙️ Settings")
    collection = st.selectbox(
        "Document Collection",
        ["hr-policies", "technical-docs", "product-specs", "default"],
        index=0,
    )
    
    top_k = st.slider(
        "Number of Sources",
        min_value=1,
        max_value=10,
        value=5,
    )
    
    st.markdown("---")
    st.markdown("### 📊 System Status")
    st.success("✅ API Connected")
    st.info("📚 3 Collections Available")

# Main content
st.markdown('<p class="main-header">🎯 Enterprise RAG System</p>', unsafe_allow_html=True)
st.markdown("Ask questions about your enterprise knowledge base")

# Query input
query = st.text_input(
    "Enter your question:",
    placeholder="What is our company policy on remote work?",
    key="query_input",
)

# Search button
if st.button("🔍 Search", type="primary") or query:
    if query:
        with st.spinner("Searching knowledge base..."):
            result = query_rag_system(query, collection, top_k)
        
        if result:
            # Display answer
            st.markdown("### 💡 Answer")
            st.markdown(result["answer"])
            
            # Display metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                confidence = result["confidence"]
                confidence_class = (
                    "confidence-high" if confidence > 0.8
                    else "confidence-medium" if confidence > 0.5
                    else "confidence-low"
                )
                st.metric("Confidence", f"{confidence:.0%}")
            with col2:
                st.metric("Latency", f"{result['latency_ms']}ms")
            with col3:
                st.metric("Tokens Used", result["tokens_used"])
            with col4:
                st.metric("Cached", "Yes" if result.get("cached") else "No")
            
            # Display sources
            if result["sources"]:
                st.markdown("### 📚 Sources")
                for i, source in enumerate(result["sources"], 1):
                    with st.expander(
                        f"Source {i}: {source['document']} "
                        f"(Relevance: {source['relevance_score']:.2f})"
                    ):
                        st.markdown(f"**Page:** {source.get('page', 'N/A')}")
                        st.markdown(f"**Excerpt:**")
                        st.markdown(f"> {source['text']}")
    else:
        st.warning("Please enter a question")

# Footer
st.markdown("---")
st.markdown(
    "Built with ❤️ using LangChain, Pinecone, and GPT-4 | "
    "[GitHub](https://github.com/jinno-ai/enterprise-rag-system)"
)
```

### Step 2-7: Dockerファイルの作成

#### 2.7.1 APIコンテナ（Dockerfile）

```dockerfile
# Dockerfile for FastAPI Backend
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/
COPY scripts/ ./scripts/

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 2.7.2 UIコンテナ（Dockerfile.streamlit）

```dockerfile
# Dockerfile for Streamlit UI
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir streamlit requests

# Copy UI code
COPY ui/ ./ui/

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "ui/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Step 2-8: GitHub Actionsの設定

#### 2.8.1 テストワークフロー（.github/workflows/test.yml）

```yaml
name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        python-version: ['3.10', '3.11']
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Cache pip dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov pytest-asyncio
      
      - name: Run tests with coverage
        run: |
          pytest tests/ -v --cov=app --cov-report=xml --cov-report=html
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          fail_ci_if_error: false

  lint:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      
      - name: Install linting tools
        run: |
          pip install black flake8 mypy
      
      - name: Check formatting with Black
        run: black --check app/ tests/
      
      - name: Lint with flake8
        run: flake8 app/ tests/ --max-line-length=100
      
      - name: Type check with mypy
        run: mypy app/ --ignore-missing-imports
```

### Step 2-9: 初期コミットとプッシュ

```bash
# すべてのファイルをステージング
git add .

# 初期コミット
git commit -m "feat: Initial project structure with core RAG implementation

- Add FastAPI backend with query and ingest endpoints
- Implement hybrid search (semantic + BM25) with RRF fusion
- Add Streamlit UI for interactive querying
- Configure Docker and docker-compose for deployment
- Set up GitHub Actions for CI/CD
- Add comprehensive documentation"

# リモートにプッシュ
git push origin main
```

### Step 2-10: リポジトリをPinned Repositoriesに追加

1. GitHubプロフィールページ（`https://github.com/jinno-ai`）にアクセス
2. 「Customize your pins」をクリック
3. `enterprise-rag-system` にチェックを入れる
4. 「Save pins」をクリック

---

## ✅ Phase 3: LLM Agent Framework リポジトリの作成

### 🎯 目標

マルチエージェントオーケストレーションシステムを構築し、複雑なタスク自動化能力を示す。

### 📐 アーキテクチャ概要

```text
┌─────────────────────────────────────────────────────────────────┐
│                    LLM Agent Framework                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   Supervisor Agent                       │   │
│  │  ┌─────────────────────────────────────────────────┐    │   │
│  │  │  Task Analysis → Agent Selection → Coordination  │    │   │
│  │  └─────────────────────────────────────────────────┘    │   │
│  └──────────────────────────┬──────────────────────────────┘   │
│                             │                                   │
│         ┌───────────────────┼───────────────────┐              │
│         │                   │                   │              │
│         ▼                   ▼                   ▼              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│  │  Research   │    │    Code     │    │    Data     │        │
│  │   Agent     │    │   Agent     │    │   Agent     │        │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘        │
│         │                  │                  │                │
│         ▼                  ▼                  ▼                │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│  │ Web Search  │    │   Python    │    │    SQL      │        │
│  │ Wikipedia   │    │  Executor   │    │   Pandas    │        │
│  │ Document    │    │   GitHub    │    │   Plotly    │        │
│  └─────────────┘    └─────────────┘    └─────────────┘        │
│       Tools              Tools              Tools              │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │                    Shared Memory                         │  │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │  │
│  │  │ Context │  │ Results │  │  State  │  │  Logs   │    │  │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 📊 ReActパターン詳細

```text
ReAct (Reasoning + Acting) Pattern:

┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  User Query: "Research AI trends and create visualization"  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ THOUGHT 1: I need to find information about AI      │   │
│  │            trends. I'll use web search.             │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ACTION 1: search("AI trends 2025")                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ OBSERVATION 1: [Search results with 15 articles]    │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ THOUGHT 2: I found relevant articles. Now I need    │   │
│  │            to extract key statistics for viz.       │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ACTION 2: extract_data(articles)                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ OBSERVATION 2: [Structured data with trends]        │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ THOUGHT 3: Data extracted. Now create Python        │   │
│  │            visualization script.                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ACTION 3: python_execute(visualization_code)        │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ OBSERVATION 3: [Chart saved to ai_trends.png]       │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ FINAL ANSWER: Created visualization showing top     │   │
│  │ AI trends: RAG (35%), Agents (28%), Multi-modal...  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step 3-1: リポジトリ作成

```bash
# GitHub上で新規リポジトリを作成
# リポジトリ名: llm-agent-framework
# 説明: Multi-agent orchestration system for complex task automation
# Public リポジトリ
# README, .gitignore (Python), MIT License を追加
```

### Step 3-2: プロジェクト構造の作成

```bash
# リポジトリをクローン
git clone https://github.com/jinno-ai/llm-agent-framework.git
cd llm-agent-framework

# ディレクトリ構造を作成
mkdir -p agent_framework/agents
mkdir -p agent_framework/tools
mkdir -p agent_framework/memory
mkdir -p agent_framework/utils
mkdir -p examples
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p docs

# __init__.py を作成
touch agent_framework/__init__.py
touch agent_framework/agents/__init__.py
touch agent_framework/tools/__init__.py
touch agent_framework/memory/__init__.py
touch agent_framework/utils/__init__.py
touch tests/__init__.py
```

### Step 3-3: コアファイルの実装

#### 3.3.1 ベースエージェント（agent_framework/agents/base.py）

```python
"""
Base Agent class for all specialized agents
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class AgentStatus(Enum):
    """Agent execution status"""
    IDLE = "idle"
    THINKING = "thinking"
    ACTING = "acting"
    COMPLETED = "completed"
    ERROR = "error"


@dataclass
class AgentAction:
    """Represents an action taken by an agent"""
    tool: str
    tool_input: Dict[str, Any]
    log: str


@dataclass
class AgentObservation:
    """Represents an observation from tool execution"""
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentStep:
    """A single step in the agent's reasoning"""
    thought: str
    action: Optional[AgentAction] = None
    observation: Optional[AgentObservation] = None


class BaseAgent(ABC):
    """
    Abstract base class for all agents.
    
    Implements the ReAct (Reasoning + Acting) pattern:
    1. THOUGHT: Reason about the current state
    2. ACTION: Choose and execute a tool
    3. OBSERVATION: Process the result
    4. Repeat until task is complete
    """
    
    def __init__(
        self,
        name: str,
        description: str,
        tools: List[str] = None,
        max_iterations: int = 10,
        verbose: bool = True,
    ):
        self.name = name
        self.description = description
        self.tools = tools or []
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.status = AgentStatus.IDLE
        self.steps: List[AgentStep] = []
    
    @abstractmethod
    async def think(self, task: str, context: Dict[str, Any]) -> str:
        """
        Generate a thought about the current state.
        
        Args:
            task: The current task description
            context: Current context including previous steps
            
        Returns:
            The agent's thought process
        """
        pass
    
    @abstractmethod
    async def act(self, thought: str, context: Dict[str, Any]) -> AgentAction:
        """
        Decide on and prepare an action based on the thought.
        
        Args:
            thought: The current thought
            context: Current context
            
        Returns:
            The action to take
        """
        pass
    
    @abstractmethod
    async def observe(self, action: AgentAction) -> AgentObservation:
        """
        Execute the action and observe the result.
        
        Args:
            action: The action to execute
            
        Returns:
            The observation from executing the action
        """
        pass
    
    async def execute(self, task: str) -> str:
        """
        Execute the full ReAct loop for a task.
        
        Args:
            task: The task to complete
            
        Returns:
            The final answer or result
        """
        self.status = AgentStatus.THINKING
        self.steps = []
        context = {"task": task, "steps": []}
        
        for iteration in range(self.max_iterations):
            if self.verbose:
                logger.info(f"[{self.name}] Iteration {iteration + 1}")
            
            # THOUGHT
            thought = await self.think(task, context)
            if self.verbose:
                logger.info(f"[{self.name}] THOUGHT: {thought}")
            
            # Check if we have a final answer
            if self._is_final_answer(thought):
                self.status = AgentStatus.COMPLETED
                return self._extract_final_answer(thought)
            
            # ACTION
            self.status = AgentStatus.ACTING
            action = await self.act(thought, context)
            if self.verbose:
                logger.info(f"[{self.name}] ACTION: {action.tool}({action.tool_input})")
            
            # OBSERVATION
            observation = await self.observe(action)
            if self.verbose:
                logger.info(f"[{self.name}] OBSERVATION: {observation.content[:200]}...")
            
            # Record step
            step = AgentStep(thought=thought, action=action, observation=observation)
            self.steps.append(step)
            context["steps"].append(step)
            
            self.status = AgentStatus.THINKING
        
        # Max iterations reached
        self.status = AgentStatus.ERROR
        return "Max iterations reached without finding an answer."
    
    def _is_final_answer(self, thought: str) -> bool:
        """Check if the thought contains a final answer"""
        return "FINAL ANSWER:" in thought.upper()
    
    def _extract_final_answer(self, thought: str) -> str:
        """Extract the final answer from the thought"""
        if "FINAL ANSWER:" in thought.upper():
            idx = thought.upper().index("FINAL ANSWER:")
            return thought[idx + len("FINAL ANSWER:"):].strip()
        return thought
```

#### 3.3.2 リサーチエージェント（agent_framework/agents/research.py）

```python
"""
Research Agent for web search and information gathering
"""

from typing import Dict, Any, List
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from .base import BaseAgent, AgentAction, AgentObservation
from ..tools.search import WebSearchTool, WikipediaTool


class ResearchAgent(BaseAgent):
    """
    Specialized agent for research tasks.
    
    Capabilities:
    - Web search using multiple search engines
    - Wikipedia lookups
    - Document retrieval and summarization
    - Fact verification
    """
    
    def __init__(
        self,
        llm_model: str = "gpt-4",
        temperature: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            name="ResearchAgent",
            description="Specialized in web search, information gathering, and fact verification",
            tools=["web_search", "wikipedia", "document_retrieval"],
            **kwargs,
        )
        
        self.llm = ChatOpenAI(model=llm_model, temperature=temperature)
        self.web_search = WebSearchTool()
        self.wikipedia = WikipediaTool()
        
        self.think_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a research agent. Your job is to find accurate information.

Available tools:
- web_search: Search the web for current information
- wikipedia: Look up factual information on Wikipedia
- document_retrieval: Search internal documents

Based on the task and previous steps, decide what to do next.
If you have enough information, respond with "FINAL ANSWER: [your answer]"

Previous steps:
{steps}
"""),
            ("human", "Task: {task}\n\nWhat should I do next?"),
        ])
        
        self.act_prompt = ChatPromptTemplate.from_messages([
            ("system", """Based on the thought, choose a tool and provide input.
Respond in JSON format:
{{"tool": "tool_name", "input": {{"query": "search query"}}}}
"""),
            ("human", "Thought: {thought}"),
        ])
    
    async def think(self, task: str, context: Dict[str, Any]) -> str:
        """Generate a thought about what to research next"""
        steps_str = self._format_steps(context.get("steps", []))
        
        response = await self.llm.ainvoke(
            self.think_prompt.format_messages(task=task, steps=steps_str)
        )
        return response.content
    
    async def act(self, thought: str, context: Dict[str, Any]) -> AgentAction:
        """Decide which research tool to use"""
        response = await self.llm.ainvoke(
            self.act_prompt.format_messages(thought=thought)
        )
        
        # Parse the JSON response
        import json
        action_data = json.loads(response.content)
        
        return AgentAction(
            tool=action_data["tool"],
            tool_input=action_data["input"],
            log=f"Using {action_data['tool']} to research",
        )
    
    async def observe(self, action: AgentAction) -> AgentObservation:
        """Execute the research tool and return results"""
        if action.tool == "web_search":
            results = await self.web_search.search(action.tool_input["query"])
            return AgentObservation(
                content=self._format_search_results(results),
                metadata={"source": "web_search", "num_results": len(results)},
            )
        elif action.tool == "wikipedia":
            content = await self.wikipedia.lookup(action.tool_input["query"])
            return AgentObservation(
                content=content,
                metadata={"source": "wikipedia"},
            )
        else:
            return AgentObservation(
                content=f"Unknown tool: {action.tool}",
                metadata={"error": True},
            )
    
    def _format_steps(self, steps: List) -> str:
        """Format previous steps for the prompt"""
        if not steps:
            return "No previous steps."
        
        formatted = []
        for i, step in enumerate(steps, 1):
            formatted.append(f"Step {i}:")
            formatted.append(f"  Thought: {step.thought}")
            if step.action:
                formatted.append(f"  Action: {step.action.tool}({step.action.tool_input})")
            if step.observation:
                formatted.append(f"  Observation: {step.observation.content[:200]}...")
        
        return "\n".join(formatted)
    
    def _format_search_results(self, results: List[Dict]) -> str:
        """Format search results for observation"""
        formatted = []
        for i, result in enumerate(results[:5], 1):
            formatted.append(f"{i}. {result['title']}")
            formatted.append(f"   URL: {result['url']}")
            formatted.append(f"   Snippet: {result['snippet']}")
        return "\n".join(formatted)
```

#### 3.3.3 スーパーバイザーエージェント（agent_framework/agents/supervisor.py）

```python
"""
Supervisor Agent for orchestrating multiple specialized agents
"""

from typing import Dict, Any, List, Optional
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END

from .base import BaseAgent


class SupervisorAgent:
    """
    Orchestrates multiple specialized agents to complete complex tasks.
    
    Responsibilities:
    - Task analysis and decomposition
    - Agent selection and delegation
    - Result synthesis and coordination
    - Error handling and recovery
    """
    
    def __init__(
        self,
        llm_model: str = "gpt-4",
        temperature: float = 0.0,
    ):
        self.llm = ChatOpenAI(model=llm_model, temperature=temperature)
        self.agents: Dict[str, BaseAgent] = {}
        self.workflow = None
        
        self.routing_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a supervisor coordinating specialized agents.

Available agents:
{agent_descriptions}

Analyze the task and decide which agent should handle it.
If the task is complete, respond with "FINISH".
Otherwise, respond with the agent name.
"""),
            ("human", "Task: {task}\n\nCurrent progress:\n{progress}\n\nWhich agent should work next?"),
        ])
    
    def register_agent(self, agent: BaseAgent) -> None:
        """Register a specialized agent"""
        self.agents[agent.name] = agent
    
    def _build_workflow(self) -> StateGraph:
        """Build the LangGraph workflow"""
        workflow = StateGraph(dict)
        
        # Add supervisor node
        workflow.add_node("supervisor", self._supervisor_node)
        
        # Add agent nodes
        for name, agent in self.agents.items():
            workflow.add_node(name, self._create_agent_node(agent))
        
        # Add conditional edges from supervisor
        workflow.add_conditional_edges(
            "supervisor",
            self._route_to_agent,
            {name: name for name in self.agents.keys()} | {"FINISH": END},
        )
        
        # Add edges from agents back to supervisor
        for name in self.agents.keys():
            workflow.add_edge(name, "supervisor")
        
        workflow.set_entry_point("supervisor")
        
        return workflow.compile()
    
    async def _supervisor_node(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Supervisor decision node"""
        agent_descriptions = "\n".join([
            f"- {name}: {agent.description}"
            for name, agent in self.agents.items()
        ])
        
        progress = state.get("progress", "No progress yet.")
        
        response = await self.llm.ainvoke(
            self.routing_prompt.format_messages(
                agent_descriptions=agent_descriptions,
                task=state["task"],
                progress=progress,
            )
        )
        
        state["next_agent"] = response.content.strip()
        return state
    
    def _route_to_agent(self, state: Dict[str, Any]) -> str:
        """Route to the next agent or finish"""
        next_agent = state.get("next_agent", "FINISH")
        if next_agent in self.agents:
            return next_agent
        return "FINISH"
    
    def _create_agent_node(self, agent: BaseAgent):
        """Create a node function for an agent"""
        async def agent_node(state: Dict[str, Any]) -> Dict[str, Any]:
            result = await agent.execute(state["task"])
            state["progress"] = state.get("progress", "") + f"\n{agent.name}: {result}"
            state["results"] = state.get("results", []) + [{"agent": agent.name, "result": result}]
            return state
        return agent_node
    
    async def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute a complex task using multiple agents.
        
        Args:
            task: The task description
            
        Returns:
            Dictionary with results from all agents
        """
        if self.workflow is None:
            self.workflow = self._build_workflow()
        
        initial_state = {
            "task": task,
            "progress": "",
            "results": [],
        }
        
        final_state = await self.workflow.ainvoke(initial_state)
        
        return {
            "task": task,
            "results": final_state.get("results", []),
            "final_progress": final_state.get("progress", ""),
        }
```

### Step 3-4: 使用例（examples/basic_usage.py）

```python
"""
Basic usage example for LLM Agent Framework
"""

import asyncio
from agent_framework import SupervisorAgent, ResearchAgent, CodeAgent


async def main():
    # Initialize supervisor
    supervisor = SupervisorAgent(llm_model="gpt-4")
    
    # Create and register specialized agents
    research_agent = ResearchAgent()
    code_agent = CodeAgent()
    
    supervisor.register_agent(research_agent)
    supervisor.register_agent(code_agent)
    
    # Execute a complex task
    result = await supervisor.execute(
        "Research the latest trends in AI and create a Python script to visualize them"
    )
    
    print("=" * 50)
    print("Task Completed!")
    print("=" * 50)
    
    for agent_result in result["results"]:
        print(f"\n{agent_result['agent']}:")
        print(f"  {agent_result['result'][:200]}...")
    
    print(f"\nFinal Progress:\n{result['final_progress']}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Step 3-5: 初期コミットとプッシュ

```bash
# READMEを配置
cp /path/to/jinno-ai-portfolio-kit/llm-agent-framework-README.md README.md

# すべてのファイルをステージング
git add .

# コミット
git commit -m "feat: Initial multi-agent framework with LangGraph

- Implement BaseAgent with ReAct pattern
- Add ResearchAgent for web search and information gathering
- Add SupervisorAgent for multi-agent orchestration
- Configure LangGraph workflow for agent coordination
- Add usage examples and documentation"

# プッシュ
git push origin main
```

---

## ✅ Phase 4: 追加プロジェクトの作成

### 4-1: realtime-edge-detection

#### 📐 アーキテクチャ

```text
┌─────────────────────────────────────────────────────────────┐
│              Real-time Edge Detection System                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│  │   Camera    │───▶│   Frame     │───▶│   YOLO v8   │    │
│  │   Input     │    │  Capture    │    │   Model     │    │
│  └─────────────┘    └─────────────┘    └──────┬──────┘    │
│                                               │            │
│                     ┌─────────────────────────┘            │
│                     │                                      │
│                     ▼                                      │
│              ┌─────────────┐                               │
│              │  TensorRT   │  ← GPU Optimization           │
│              │  Engine     │                               │
│              └──────┬──────┘                               │
│                     │                                      │
│         ┌───────────┼───────────┐                         │
│         │           │           │                         │
│         ▼           ▼           ▼                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐         │
│  │  Bounding   │ │   Class     │ │ Confidence  │         │
│  │   Boxes     │ │   Labels    │ │   Scores    │         │
│  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘         │
│         │               │               │                 │
│         └───────────────┼───────────────┘                 │
│                         │                                 │
│                         ▼                                 │
│              ┌─────────────────┐                          │
│              │   Visualization │                          │
│              │   & Output      │                          │
│              └─────────────────┘                          │
│                                                           │
│  Performance: 30+ FPS on Raspberry Pi 4 / Jetson Nano    │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

#### セットアップ手順

```bash
# リポジトリ作成
# GitHub上で: realtime-edge-detection
# 説明: Low-latency object detection optimized for edge devices

# クローンとセットアップ
git clone https://github.com/jinno-ai/realtime-edge-detection.git
cd realtime-edge-detection

# ディレクトリ構造
mkdir -p src/models src/utils src/inference
mkdir -p configs examples tests docs/images
mkdir -p deployment/raspberry_pi deployment/jetson

# 主要ファイル作成
touch src/__init__.py
touch src/models/__init__.py
touch src/detector.py
touch src/optimizer.py
touch configs/yolov8_config.yaml
```

#### 技術スタック

| コンポーネント | 技術 | 役割 |
|---------------|------|------|
| モデル | YOLO v8 | 物体検出 |
| 最適化 | TensorRT | GPU推論高速化 |
| フレームワーク | OpenCV | 画像処理 |
| エクスポート | ONNX | クロスプラットフォーム |
| エッジデバイス | Raspberry Pi, Jetson | デプロイ先 |

### 4-2: multilingual-sentiment-analyzer

#### 📐 アーキテクチャ

```text
┌─────────────────────────────────────────────────────────────┐
│           Multilingual Sentiment Analyzer                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐                                           │
│  │   Input     │  Japanese / English / Chinese             │
│  │   Text      │                                           │
│  └──────┬──────┘                                           │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Language Detection                      │   │
│  │              (fastText / langdetect)                 │   │
│  └──────────────────────┬──────────────────────────────┘   │
│                         │                                   │
│         ┌───────────────┼───────────────┐                  │
│         │               │               │                  │
│         ▼               ▼               ▼                  │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │  Japanese   │ │   English   │ │   Chinese   │          │
│  │  Tokenizer  │ │  Tokenizer  │ │  Tokenizer  │          │
│  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘          │
│         │               │               │                  │
│         └───────────────┼───────────────┘                  │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              XLM-RoBERTa Model                       │   │
│  │         (Fine-tuned for Sentiment)                   │   │
│  └──────────────────────┬──────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │   Output: Positive / Negative / Neutral + Score     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### セットアップ手順

```bash
# リポジトリ作成
# GitHub上で: multilingual-sentiment-analyzer
# 説明: Cross-lingual sentiment analysis with fine-tuned transformers

# クローンとセットアップ
git clone https://github.com/jinno-ai/multilingual-sentiment-analyzer.git
cd multilingual-sentiment-analyzer

# ディレクトリ構造
mkdir -p src/models src/preprocessing src/api
mkdir -p data/train data/test data/raw
mkdir -p notebooks configs tests
mkdir -p deployment/docker

# 主要ファイル作成
touch src/__init__.py
touch src/analyzer.py
touch src/api/main.py
touch configs/model_config.yaml
```

### 4-3: micro-instruction-engineering

#### 📐 フレームワーク概要

```text
┌─────────────────────────────────────────────────────────────┐
│           Micro-Instruction Engineering Framework           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Traditional Prompt:                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ "Summarize this article and extract key points"     │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  Micro-Instruction Decomposition:                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Step 1: Read and understand the article             │   │
│  │ Step 2: Identify the main topic                     │   │
│  │ Step 3: Extract 3-5 key points                      │   │
│  │ Step 4: Summarize in 2-3 sentences                  │   │
│  │ Step 5: Format output as bullet points              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Benefits:                                                  │
│  ✅ +40% accuracy improvement                              │
│  ✅ More consistent outputs                                │
│  ✅ Better reasoning chains                                │
│  ✅ Easier debugging                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### セットアップ手順

```bash
# リポジトリ作成
# GitHub上で: micro-instruction-engineering
# 説明: Systematic methodology for prompt optimization & AI reasoning

# クローンとセットアップ
git clone https://github.com/jinno-ai/micro-instruction-engineering.git
cd micro-instruction-engineering

# ディレクトリ構造
mkdir -p src/decomposer src/evaluator src/optimizer
mkdir -p notebooks examples benchmarks
mkdir -p data/prompts data/results
mkdir -p docs/methodology

# 主要ファイル作成
touch src/__init__.py
touch src/decomposer/instruction_decomposer.py
touch src/evaluator/prompt_evaluator.py
touch notebooks/01_introduction.ipynb
touch notebooks/02_decomposition_examples.ipynb
```

---

## ✅ Phase 5: README品質向上

### 5-1: デモGIF/動画の作成

#### 推奨ツール

| OS | ツール | 特徴 |
|----|--------|------|
| Windows | ScreenToGif | 軽量、編集機能付き |
| Mac | Kap | シンプル、高品質 |
| Linux | Peek | GTK対応、軽量 |
| クロスプラットフォーム | OBS Studio | 高機能、動画も可 |

#### GIF作成手順（ScreenToGifの例）

```text
1. ScreenToGifをダウンロード・インストール
   https://www.screentogif.com/

2. アプリケーションを起動

3. 「Recorder」を選択

4. 録画範囲をアプリケーションウィンドウに合わせる

5. 「Record」ボタンで録画開始

6. デモ操作を実行:
   - クエリを入力
   - 検索ボタンをクリック
   - 結果が表示されるまで待機

7. 「Stop」で録画終了

8. エディタで編集:
   - 不要なフレームを削除
   - フレームレートを調整（15-20fps推奨）
   - ファイルサイズを最適化（5MB以下推奨）

9. 「Save As」でGIFとして保存
   保存先: docs/images/demo.gif
```

#### GIF最適化のコツ

```text
✅ 推奨設定:
- 解像度: 800x600 以下
- フレームレート: 15-20 fps
- 長さ: 10-30秒
- ファイルサイズ: 5MB以下

❌ 避けるべき:
- 4K解像度での録画
- 60fpsでの録画
- 1分以上の長いGIF
- 10MB以上のファイル
```

### 5-2: アーキテクチャ図の作成

#### Mermaidを使用した図（README内に直接記述）

```markdown
## Architecture

```mermaid
graph TB
    A[User Query] --> B[API Gateway]
    B --> C[Query Processor]
    C --> D{Search Type}
    D -->|Semantic| E[Vector DB]
    D -->|Keyword| F[BM25 Index]
    E --> G[Result Fusion]
    F --> G
    G --> H[Re-Ranker]
    H --> I[LLM Generator]
    I --> J[Response]
```
```

#### draw.ioを使用した図

```text
1. draw.io (https://app.diagrams.net/) にアクセス

2. 「Create New Diagram」を選択

3. テンプレートから「Flowchart」を選択

4. コンポーネントを配置:
   - Rectangle: サービス/コンポーネント
   - Diamond: 判断ポイント
   - Cylinder: データベース
   - Arrow: データフロー

5. スタイル設定:
   - フォント: Arial または Roboto
   - 色: 一貫したカラースキーム
   - 線: 2px、矢印付き

6. エクスポート:
   - Format: PNG (透過背景)
   - Scale: 2x (高解像度)
   - 保存先: docs/images/architecture.png
```

### 5-3: バッジの追加

#### 基本バッジセット

```markdown
<!-- プロジェクトの状態 -->
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

<!-- GitHub統計 -->
![Stars](https://img.shields.io/github/stars/jinno-ai/enterprise-rag-system)
![Forks](https://img.shields.io/github/forks/jinno-ai/enterprise-rag-system)
![Issues](https://img.shields.io/github/issues/jinno-ai/enterprise-rag-system)
![Last Commit](https://img.shields.io/github/last-commit/jinno-ai/enterprise-rag-system)

<!-- CI/CD -->
![Tests](https://github.com/jinno-ai/enterprise-rag-system/workflows/Tests/badge.svg)
![Coverage](https://codecov.io/gh/jinno-ai/enterprise-rag-system/branch/main/graph/badge.svg)

<!-- 技術スタック -->
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=chainlink&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
```

#### カスタムバッジの作成

```text
shields.io でカスタムバッジを作成:

URL形式:
https://img.shields.io/badge/{LABEL}-{MESSAGE}-{COLOR}

例:
- https://img.shields.io/badge/accuracy-85%25-brightgreen
- https://img.shields.io/badge/latency-<3s-blue
- https://img.shields.io/badge/docs-comprehensive-orange
```

---

## ✅ Phase 6: GitHub Actionsの設定

### 6-1: 自動テストワークフロー

`.github/workflows/test.yml`:

```yaml
name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  PYTHON_VERSION: '3.10'

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      redis:
        image: redis:7-alpine
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: 'pip'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov pytest-asyncio
      
      - name: Run unit tests
        run: pytest tests/unit -v --cov=app --cov-report=xml
      
      - name: Run integration tests
        run: pytest tests/integration -v
        env:
          REDIS_HOST: localhost
          REDIS_PORT: 6379
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml

  lint:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      
      - name: Install linters
        run: pip install black flake8 isort mypy
      
      - name: Check formatting
        run: |
          black --check app/ tests/
          isort --check-only app/ tests/
      
      - name: Lint code
        run: flake8 app/ tests/ --max-line-length=100
      
      - name: Type check
        run: mypy app/ --ignore-missing-imports

  security:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Run security scan
        uses: pyupio/safety@v2.3.5
        with:
          api-key: ${{ secrets.SAFETY_API_KEY }}
```

### 6-2: 自動リリースワークフロー

`.github/workflows/release.yml`:

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      
      - name: Build package
        run: |
          pip install build
          python -m build
      
      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          files: dist/*
          generate_release_notes: true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ghcr.io/${{ github.repository }}:${{ github.ref_name }}
            ghcr.io/${{ github.repository }}:latest
```

---

## ✅ Phase 7: プロフィール強化

### 7-1: GitHub Stats設定

Profile READMEに追加するStats:

```markdown
## 📊 GitHub Stats

<div align="center">

<!-- 基本統計 -->
![GitHub stats](https://github-readme-stats.vercel.app/api?username=jinno-ai&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00D9FF&icon_color=00D9FF&text_color=C9D1D9)

<!-- 使用言語 -->
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=jinno-ai&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00D9FF&text_color=C9D1D9)

<!-- コミットストリーク -->
![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=jinno-ai&theme=tokyonight&hide_border=true&background=0D1117&stroke=00D9FF&ring=00D9FF&fire=FF6B6B&currStreakLabel=00D9FF)

<!-- アクティビティグラフ -->
![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=jinno-ai&theme=tokyo-night&hide_border=true&bg_color=0D1117)

</div>
```

### 7-2: Skill Iconsの設定

```markdown
## 🛠️ Tech Stack

<!-- skillicons.dev を使用 -->
![My Skills](https://skillicons.dev/icons?i=python,pytorch,tensorflow,docker,kubernetes,aws,gcp,fastapi,react,typescript&perline=5)

<!-- または個別バッジ -->
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
```

---

## ✅ Phase 8: コミュニティ活動

### 8-1: Issues & Discussions有効化

各リポジトリで以下を設定:

```text
1. リポジトリページで「Settings」タブをクリック

2. 左メニューから「General」を選択

3. 「Features」セクションまでスクロール

4. 以下にチェックを入れる:
   ✅ Issues
   ✅ Discussions (コミュニティ構築用)
   ✅ Projects (タスク管理用)
   ✅ Wiki (ドキュメント用、オプション)

5. 「Save」をクリック
```

### 8-2: Issue/PRテンプレートの作成

`.github/ISSUE_TEMPLATE/bug_report.md`:

```markdown
---
name: Bug Report
about: Report a bug to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

## Bug Description
A clear and concise description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g., Ubuntu 22.04]
- Python version: [e.g., 3.10]
- Package version: [e.g., 1.0.0]

## Additional Context
Any other context about the problem.
```

`.github/PULL_REQUEST_TEMPLATE.md`:

```markdown
## Description
Brief description of the changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing tests pass locally
- [ ] I have updated the documentation accordingly

## Related Issues
Fixes #(issue number)
```

### 8-3: CONTRIBUTINGガイド

`CONTRIBUTING.md`:

```markdown
# Contributing to Enterprise RAG System

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- Git

### Development Setup

```bash
# Clone the repository
git clone https://github.com/jinno-ai/enterprise-rag-system.git
cd enterprise-rag-system

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

## 📝 Code Style

We follow these conventions:
- **PEP 8** for Python code style
- **Black** for code formatting
- **isort** for import sorting
- **Type hints** for all functions

Run formatters before committing:
```bash
black app/ tests/
isort app/ tests/
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=app --cov-report=html

# Run specific test file
pytest tests/unit/test_retriever.py -v
```

## 📤 Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linters
5. Commit with a descriptive message
6. Push to your fork
7. Open a Pull Request

### Commit Message Format

```text
type(scope): subject

body (optional)

footer (optional)
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Example:
```text
feat(retriever): add hybrid search with RRF fusion

- Implement semantic search using Pinecone
- Add BM25 keyword search
- Merge results using Reciprocal Rank Fusion

Closes #123
```

## 🤝 Code of Conduct

Please be respectful and constructive in all interactions.

## 📞 Questions?

- Open an issue for bugs or feature requests
- Start a discussion for questions
- Reach out on [Twitter](https://twitter.com/jinno_ai)
```

---

## ✅ Phase 9: プロモーション

### 9-1: Twitter/X投稿テンプレート

#### プロジェクトリリース投稿

```text
🚀 Just launched my Enterprise RAG System on GitHub!

A production-ready RAG pipeline with:
✅ Hybrid search (semantic + keyword)
✅ Multi-format document support
✅ <3s response latency
✅ 85%+ answer relevancy
✅ Full observability with LangSmith

Built with #LangChain #Pinecone #GPT4

Check it out: https://github.com/jinno-ai/enterprise-rag-system

#AI #MachineLearning #RAG #OpenSource #Python
```

#### 技術解説スレッド

```text
🧵 Thread: How I built a production-grade RAG system

1/7 The problem: Enterprise knowledge is scattered across PDFs, Confluence, Notion...

Traditional search fails to capture semantic meaning.

Here's how I solved it 👇

---

2/7 Architecture Overview:

The system uses a hybrid search approach:
- Semantic search (dense vectors)
- Keyword search (BM25)
- Reciprocal Rank Fusion for merging

This gives the best of both worlds 🎯

---

3/7 Key Components:

📄 Document Ingestion: Unstructured.io
🔢 Embeddings: OpenAI Ada-002
🗄️ Vector DB: Pinecone
🔍 Search: Hybrid (semantic + BM25)
🤖 LLM: GPT-4 / Claude

---

4/7 Performance Results:

After testing on 10,000 enterprise docs:
- Answer Relevancy: 85.3%
- Faithfulness: 91.2%
- Latency (p95): 2.9s
- Cost per query: $0.03

---

5/7 The secret sauce: Re-ranking

Using Cross-Encoder models to re-rank results improved accuracy by 15%!

The model understands context better than simple similarity scores.

---

6/7 Lessons learned:

1. Chunking strategy matters A LOT
2. Hybrid search > pure semantic
3. Caching is essential for production
4. Monitor everything with LangSmith

---

7/7 Want to try it?

🔗 GitHub: [link]
📖 Docs: [link]
🐳 Docker: docker-compose up -d

Star ⭐ if you find it useful!

Questions? Reply below 👇
```

### 9-2: LinkedIn投稿テンプレート

```text
🎯 Excited to share my latest open-source project: Enterprise RAG System

After months of development and testing, I'm releasing a production-grade Retrieval-Augmented Generation pipeline designed for enterprise knowledge bases.

🔥 Key Features:
• Hybrid search combining semantic and keyword approaches
• Multi-format document support (PDF, Markdown, Confluence, Notion)
• Sub-3-second response latency
• 85%+ answer relevancy on enterprise datasets
• Full observability with LangSmith integration

💡 Why I built this:
Modern enterprises struggle with information scattered across multiple systems. Traditional search fails to capture semantic meaning, and generic LLMs hallucinate without proper context.

This system bridges that gap with a production-ready architecture.

🛠️ Tech Stack:
• LangChain for orchestration
• Pinecone for vector storage
• GPT-4/Claude for generation
• FastAPI + Streamlit for API/UI
• Docker for deployment

📊 Results:
Tested on 10,000 enterprise documents:
• Answer Relevancy: 85.3%
• Faithfulness: 91.2%
• Latency (p95): 2.9s

🔗 Check it out: https://github.com/jinno-ai/enterprise-rag-system

I'd love to hear your feedback and suggestions!

#AI #MachineLearning #RAG #LLM #OpenSource #Python #LangChain
```

### 9-3: Reddit投稿ガイド

#### 適切なサブレディット

| サブレディット | 内容 | 投稿タイプ |
|---------------|------|-----------|
| r/MachineLearning | 研究・技術 | [P] Project |
| r/learnmachinelearning | 学習者向け | チュートリアル |
| r/LocalLLaMA | ローカルLLM | 実装共有 |
| r/LangChain | LangChain関連 | プロジェクト |
| r/OpenSource | OSS全般 | リリース告知 |

#### 投稿テンプレート（r/MachineLearning）

```text
[P] Enterprise RAG System - Production-grade RAG pipeline with hybrid search

I've been working on a RAG system designed for enterprise use cases and wanted to share it with the community.

**Problem:**
Enterprise knowledge is scattered across multiple document formats and systems. Traditional keyword search fails to capture semantic meaning, and generic LLMs hallucinate without proper context.

**Solution:**
A hybrid search approach combining:
- Semantic search using dense vectors (Pinecone)
- Keyword search using BM25
- Reciprocal Rank Fusion for result merging
- Cross-Encoder re-ranking for improved accuracy

**Results:**
Tested on 10,000 enterprise documents:
- Answer Relevancy: 85.3% (RAGAS score)
- Faithfulness: 91.2%
- Latency (p95): 2.9s
- Cost per query: $0.03 (GPT-4 Turbo)

**Tech Stack:**
- LangChain for orchestration
- Pinecone for vector storage
- OpenAI Ada-002 for embeddings
- GPT-4/Claude for generation
- FastAPI + Streamlit

**GitHub:** [link]

Would love to hear feedback, especially on:
1. Chunking strategies for different document types
2. Evaluation methodologies
3. Production deployment experiences

Happy to answer any questions!
```

---

## 📊 成功指標トラッキング

### 週次チェックリスト

```text
□ 最低5コミット (緑のマスを維持)
  - 月曜: ドキュメント更新
  - 水曜: 機能追加/バグ修正
  - 金曜: テスト追加
  - 土日: リファクタリング/改善

□ README更新 (進捗を反映)
  - 新機能の追加
  - バッジの更新
  - ロードマップの更新

□ Issues対応 (ある場合)
  - 24時間以内に初回返信
  - 1週間以内にクローズ目標

□ 技術ブログ執筆 (隔週)
  - Medium または Qiita
  - 1500-3000文字
  - コード例を含める

□ SNS投稿 (週1回)
  - 進捗報告
  - 技術Tips
  - コミュニティ交流
```

### 月次目標

```text
Month 1:
├── Profile README完成 ✅
├── enterprise-rag-system 初版リリース
├── llm-agent-framework 初版リリース
├── Stars: 10+ (合計)
└── ブログ記事: 2本

Month 2:
├── 追加プロジェクト2つ完成
├── デモGIF/動画追加
├── GitHub Actions設定
├── Stars: 50+ (合計)
└── ブログ記事: 4本 (累計)

Month 3:
├── 全6プロジェクト完成
├── OSS貢献開始 (LangChain等)
├── Followers: 50+
├── Stars: 100+ (合計)
└── 企業からのスカウト: 初回
```

### KPIダッシュボード

```text
┌─────────────────────────────────────────────────────────────┐
│                    Portfolio KPIs                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  GitHub Metrics:                                            │
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐ │
│  │   Stars     │   Forks     │  Followers  │   Commits   │ │
│  │    100+     │    20+      │    50+      │   500+/yr   │ │
│  └─────────────┴─────────────┴─────────────┴─────────────┘ │
│                                                             │
│  Content Metrics:                                           │
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐ │
│  │   Repos     │   Blogs     │   Tweets    │   LinkedIn  │ │
│  │     6       │    12/yr    │   52/yr     │   12/yr     │ │
│  └─────────────┴─────────────┴─────────────┴─────────────┘ │
│                                                             │
│  Engagement Metrics:                                        │
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐ │
│  │   Issues    │    PRs      │  Discussions│   Scouts    │ │
│  │   Resolved  │   Merged    │   Active    │   Received  │ │
│  │    20+      │    5+       │    10+      │    3+       │ │
│  └─────────────┴─────────────┴─────────────┴─────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 優先順位まとめ

### 今日やること (Day 1)

1. ✅ Profile README作成・公開
2. ✅ enterprise-rag-system リポジトリ作成
3. ✅ READMEとプロジェクト構造を配置
4. ✅ Pinned Repositoriesに追加

### 今週やること (Week 1)

1. RAG Systemの基本実装開始
   - app/main.py
   - app/core/retriever.py
   - app/api/routes/query.py
2. デモGIF作成
3. Twitter/LinkedIn投稿

### 今月やること (Month 1)

1. RAG System完成
2. Agent Framework開始
3. ブログ記事2本執筆
4. Pinned Repositoriesを6つ埋める

---

## 🆘 トラブルシューティング

### Q: Profile READMEが表示されない

```text
原因: リポジトリ名がユーザー名と一致していない

解決策:
1. リポジトリ名を確認 (大文字小文字も一致させる)
2. リポジトリがPublicになっているか確認
3. README.mdファイルが存在するか確認
4. キャッシュをクリア (Ctrl+Shift+R)
```

### Q: GitHubバッジが表示されない

```text
原因: URLのユーザー名/リポジトリ名が間違っている

解決策:
1. shields.ioのURLを確認
2. ユーザー名とリポジトリ名が正確か確認
3. リポジトリがPublicか確認
4. 数分待ってリロード
```

### Q: GitHub Actionsが動かない

```text
原因: ワークフローファイルの構文エラーまたは権限不足

解決策:
1. Settings → Actions → "Allow all actions" を確認
2. YAMLの構文をチェック (インデント注意)
3. Actions タブでエラーログを確認
4. secrets が正しく設定されているか確認
```

### Q: Docker Composeが起動しない

```text
原因: 環境変数が設定されていない

解決策:
1. .env ファイルが存在するか確認
2. .env.example をコピーして .env を作成
3. 必要なAPIキーを設定
4. docker-compose down && docker-compose up -d
```

### Q: Pineconeに接続できない

```text
原因: APIキーまたは環境設定が間違っている

解決策:
1. PINECONE_API_KEY が正しいか確認
2. PINECONE_ENVIRONMENT が正しいか確認
3. Pineconeダッシュボードでインデックスが存在するか確認
4. ネットワーク接続を確認
```

---

## 📚 参考リソース

### ドキュメント・チュートリアル

- [GitHub Profile README Generator](https://rahuldkjain.github.io/gh-profile-readme-generator/)
- [Shields.io](https://shields.io/) - バッジ生成
- [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats)
- [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme)

### 技術リソース

- [LangChain Documentation](https://python.langchain.com/docs/)
- [Pinecone Documentation](https://docs.pinecone.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

### コミュニティ

- [LangChain Discord](https://discord.gg/langchain)
- [Pinecone Community](https://community.pinecone.io/)
- [r/MachineLearning](https://reddit.com/r/MachineLearning)
- [AI Twitter Community](https://twitter.com/i/communities)

---

## 🎉 完成イメージ

**3ヶ月後のあなたのGitHubプロフィール:**

```text
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ✨ 魅力的なProfile README                                  │
│     - タイピングアニメーション                              │
│     - Tech Stackバッジ                                      │
│     - GitHub Stats                                          │
│     - Featured Projects                                     │
│                                                             │
│  📦 6つのピン留めプロジェクト (全てスター10+)              │
│     1. enterprise-rag-system ⭐ 50+                         │
│     2. llm-agent-framework ⭐ 30+                           │
│     3. realtime-edge-detection ⭐ 20+                       │
│     4. multilingual-sentiment-analyzer ⭐ 15+               │
│     5. micro-instruction-engineering ⭐ 10+                 │
│     6. langchain-google-contributions ⭐ 10+                │
│                                                             │
│  🟢 コミット活動の継続 (緑のマス)                          │
│     - 週5+コミット                                          │
│     - 継続的な改善                                          │
│                                                             │
│  ⭐ 合計100+ スター                                         │
│  👥 50+ フォロワー                                          │
│  📝 定期的なブログ更新 (月2本)                             │
│  🤝 OSS貢献実績 (LangChain等)                              │
│  💼 企業からのスカウト複数                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**結果:** re:shineや他のプラットフォームで「この人を採用したい!」と思われるポートフォリオの完成

---

頑張ってください! 🚀

質問があれば、いつでも聞いてください。
