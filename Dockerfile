# ベースイメージ（ここは自由に変更）
FROM ubuntu:latest

# 必要なソフトのインストール
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# uvのインストール
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Default command
CMD ["/bin/bash"]
