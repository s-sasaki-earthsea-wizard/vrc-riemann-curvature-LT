# VRC Riemann Curvature LT

## プロジェクト概要

リーマン曲率を潮汐力から直感的に理解するYouTube動画およびプレゼンテーション資料の作成プロジェクト。
共変微分やクリストッフェル記号などの数学的道具を使わず、一般相対性理論の核心概念を解説する。

## ディレクトリ構造

```text
vrc-riemann-curvature-LT/
├── CLAUDE.md                 # プロジェクト設定・開発ルール
├── README.md                 # プロジェクト概要
├── Makefile                  # ビルドコマンド
├── docs/                     # 参考文献
│   └── chapter5.pdf          # Tidal Forces and Curvature (J. Rubio)
├── slides-jp/                # スライド・動画関連（reveal.js）
│   ├── index.html            # メインスライド
│   ├── yt_script.md          # YouTube動画脚本（本文）
│   ├── yt_script_outline.md  # 脚本の章立てドラフト・補足メモ
│   ├── youtube_description.md # 動画説明文
│   ├── yt_script_tts.md      # TTS用スクリプト
│   ├── css/                  # スタイルシート
│   ├── js/                   # JavaScript
│   ├── assets/               # 画像等のアセット
│   └── plugin/               # reveal.jsプラグイン
├── scripts/                  # ユーティリティスクリプト
└── .github/                  # GitHubテンプレート
```

## 言語設定

このプロジェクトでは**日本語**での応答を行ってください。コード内のコメント、ログメッセージ、エラーメッセージ、ドキュメンテーション文字列なども日本語で記述してください。

## 開発ルール

### コーディング規約

- Python: PEP 8準拠
- 関数名: snake_case
- クラス名: PascalCase
- 定数: UPPER_SNAKE_CASE
- Docstring: Google Style

## Git運用

- ブランチ戦略: feature/*, fix/*, refactor/*
- コミットメッセージ: 英文を使用、動詞から始める
- PRはmainブランチへ

## 開発ガイドライン

### ドキュメント更新プロセス

機能追加やPhase完了時には、以下のドキュメントを同期更新する：

1. **CLAUDE.md**: プロジェクト全体状況、Phase完了記録、技術仕様
2. **README.md**: ユーザー向け機能概要、実装状況、使用方法
3. **Makefile**: コマンドヘルプテキスト（## コメント）の更新
4. **makefiles/**: コマンドヘルプテキスト（## コメント）の更新

### コミットメッセージ規約

#### コミット粒度

- **1コミット = 1つの主要な変更**: 複数の独立した機能や修正を1つのコミットにまとめない
- **論理的な単位でコミット**: 関連する変更は1つのコミットにまとめる
- **段階的コミット**: 大きな変更は段階的に分割してコミット

#### プレフィックスと絵文字

- ✨ feat: 新機能
- 🐞 fix: バグ修正
- 📚 docs: ドキュメント
- 🎨 style: コードスタイル修正
- 🛠️ refactor: リファクタリング
- ⚡ perf: パフォーマンス改善
- ✅ test: テスト追加・修正
- 🏗️ chore: ビルド・補助ツール
- 🚀 deploy: デプロイ
- 🔒 security: セキュリティ修正
- 📝 update: 更新・改善
- 🗑️ remove: 削除

**重要**: Claude Codeを使用してコミットする場合は、必ず以下の署名を含める：

```text
🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```
