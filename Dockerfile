FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

ENV ENVDIR="/app"
ENV PATH="$ENVDIR/.venv/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Setup Python env
WORKDIR $ENVDIR

# 既存の設定ファイルを読み込む場合
COPY pyproject.toml .python-version uv.lock $ENVDIR
RUN uv sync --no-cache --frozen

# Default command
CMD ["/bin/bash"]
