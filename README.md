# uv-devcontainer-template
uvを使用したPython環境のdevcontainer

### 使用方法
※DockerやDev Container等の設定については完了している前提とします。  

1. このリポジトリをクローン
  お好きなフォルダで下記のコマンドを実行  
  `git clone https://github.com/muetaek0321/uv-devcontainer-template.git`  

2. リポジトリのフォルダをVSCodeから開き、Dev Containerを立ち上げ  
  VSCode上から「**コンテナで再度開く（Reopen in Container）**」  
  プロジェクトのフォルダ内に仮想環境（.venv）が作成されます  

3. 必要なライブラリをインストール
  インストール時は下記のコマンドを実行  
  \[package\]はインストールしたいライブラリ名を入れてください。（numpy, pandasなど）  
  `uv add [package]`  

### 下記も併せてご参考ください
[https://fallpoke-tech.hatenadiary.jp/entry/2025/02/25/080000](https://fallpoke-tech.hatenadiary.jp/entry/2025/02/25/080000)