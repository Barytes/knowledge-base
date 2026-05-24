#!/bin/bash
# kb-scripts: 知识库本地操作脚本
# 用法：./kb-scripts.sh <command> [args]

set -e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
INBOX_DIR="$ROOT_DIR/inbox"
RAW_EXTERNAL_DIR="$ROOT_DIR/raw/external"

list_inbox() {
    echo "=== Inbox 内容 ==="
    if [ -d "$INBOX_DIR" ]; then
        find "$INBOX_DIR" -name "*.md" -type f ! -name "README.md" | sort
    else
        echo "inbox 目录不存在"
    fi
}

read_inbox() {
    echo "=== 读取 Inbox 文件 ==="
    if [ -d "$INBOX_DIR" ]; then
        for f in "$INBOX_DIR"/*.md; do
            if [ -f "$f" ] && [ "$(basename "$f")" != "README.md" ]; then
                echo ""
                echo "--- 文件：$(basename "$f") ---"
                head -50 "$f"
            fi
        done
    else
        echo "inbox 目录不存在"
    fi
}

move_to_external() {
    echo "=== 移动 Inbox 到 raw/external ==="
    if [ ! -d "$INBOX_DIR" ]; then
        echo "inbox 目录不存在"
        exit 1
    fi
    if [ ! -d "$RAW_EXTERNAL_DIR" ]; then
        echo "创建 raw/external 目录"
        mkdir -p "$RAW_EXTERNAL_DIR"
    fi

    local count=0
    for f in "$INBOX_DIR"/*; do
        if [ -f "$f" ] && [ "$(basename "$f")" != "README.md" ]; then
            filename=$(basename "$f")
            echo "移动：$filename"
            mv "$f" "$RAW_EXTERNAL_DIR/"
            ((count++)) || true
        fi
    done
    echo "完成：移动了 $count 个文件"
}

show_help() {
    echo "用法：$0 <command>"
    echo ""
    echo "可用命令:"
    echo "  list     - 列出 inbox 中的文件"
    echo "  read     - 读取 inbox 中所有文件内容"
    echo "  move     - 将 inbox 文件移动到 raw/external"
    echo "  help     - 显示帮助信息"
}

# 主入口
case "${1:-help}" in
    list)
        list_inbox
        ;;
    read)
        read_inbox
        ;;
    move)
        move_to_external
        ;;
    help|*)
        show_help
        ;;
esac
