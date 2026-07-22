# Driving Assist AI

ドライブレコーダー映像を解析し、危険を検知してドライバーに警告するAI運転支援システム。

## 概要

YOLOv8を用いた物体検出をベースに、車線逸脱検知・距離推定・危険警告機能を段階的に実装していく開発中のプロジェクトです。

## 現在実装済みの機能

- [x] YOLOv8による物体検出(車・歩行者・自転車など)
- [x] 動画ファイルに対するリアルタイム物体検出

## 今後実装予定の機能

- [ ] 車線逸脱検知
- [ ] 前方車両との距離推定
- [ ] 衝突危険時の警告機能
- [ ] 危険シーンの自動保存
- [ ] Flaskを用いたWebアプリ化

## 使用技術

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- Flask(予定)

## セットアップ方法

```bash
git clone https://github.com/kuma46169/driving-assist-ai.git
cd driving-assist-ai
python -m venv venv
venv\Scripts\activate
pip install ultralytics opencv-python flask
```

## 使い方

画像に対する物体検出:

```bash
python test_yolo.py
```

動画に対するリアルタイム物体検出:

```bash
python video-test.py
```

`q` キーで再生を終了できます。

## 開発の背景

大阪情報ITクリエイター専門学校の卒業制作として開始。将来的には就職活動用ポートフォリオとしても継続開発予定。