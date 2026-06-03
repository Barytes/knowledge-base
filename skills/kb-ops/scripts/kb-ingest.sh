#!/bin/bash
# kb-ingest: 知识库摄取脚本
# 用法：./kb-ingest.sh [source_file] [target_dir]

set -e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/../../.. && pwd)"
INBOX_DIR="$ROOT_DIR/inbox"
RAW_EXTERNAL_DIR="$ROOT_DIR/raw/external"
RAW_PERSONAL_DIR="$ROOT_DIR/raw/personal"
WIKI_KNOWLEDGE_DIR="$ROOT_DIR/wiki/knowledge"
WIKI_LOG="$ROOT_DIR/wiki/log.md"

refresh_site() {
    local builder="$ROOT_DIR/scripts/reorganize_wiki.py"
    if [ ! -f "$builder" ]; then
        echo "错误：找不到站点生成脚本：$builder"
        exit 1
    fi

    echo "重新生成 wiki/site/ 静态网页视图..."
    python3 "$builder"
}

# 从 inbox 摄取所有文件
ingest_all() {
    echo "=== 摄取 Inbox 所有文件 ==="

    if [ ! -d "$INBOX_DIR" ]; then
        echo "错误：inbox 目录不存在"
        exit 1
    fi

    local count=0
    for f in "$INBOX_DIR"/*; do
        if [ -f "$f" ] && [ "$(basename "$f")" != "README.md" ]; then
            filename=$(basename "$f")
            echo "处理：$filename"

            # 移动文件到 raw/external
            mv "$f" "$RAW_EXTERNAL_DIR/"
            echo "  -> 已移动到 raw/external/"
            ((count++)) || true
        fi
    done

    echo "完成：处理了 $count 个文件"
    refresh_site
    echo ""
    echo "下一步：使用 kb-scripts.sh read 查看文件内容，或手动创建 wiki 页面"
}

# 摄取单个文件
ingest_file() {
    local source_file="$1"
    local target_dir="${2:-$RAW_EXTERNAL_DIR}"

    if [ ! -f "$source_file" ]; then
        echo "错误：文件不存在：$source_file"
        exit 1
    fi

    filename=$(basename "$source_file")
    echo "处理：$filename"

    # 确保目标目录存在
    mkdir -p "$target_dir"

    # 移动文件
    mv "$source_file" "$target_dir/"
    echo "  -> 已移动到：$target_dir/"

    # 记录日志
    local today=$(date +%Y-%m-%d)
    local log_entry="## [$today] 摄取 | $filename\n\n已移动到 $target_dir/\n\n"

    refresh_site
    echo "完成：已处理 $filename"
}

# 列出 inbox 内容（详细）
list_inbox_detail() {
    echo "=== Inbox 详细内容 ==="
    echo ""

    if [ -d "$INBOX_DIR" ]; then
        local count=0
        for f in "$INBOX_DIR"/*; do
            if [ -f "$f" ] && [ "$(basename "$f")" != "README.md" ]; then
                filename=$(basename "$f")
                size=$(wc -c < "$f" | tr -d ' ')
                lines=$(wc -l < "$f" | tr -d ' ')
                echo "📄 $filename ($lines 行，$size 字节)"
                ((count++)) || true
            fi
        done
        echo ""
        echo "共 $count 个文件待处理"
    else
        echo "inbox 目录不存在"
    fi
}

# 显示帮助
show_help() {
    echo "用法：$0 <command> [args]"
    echo ""
    echo "命令:"
    echo "  all              - 摄取 inbox 中所有文件到 raw/external"
    echo "  file <path>      - 摄取单个文件到指定目录"
    echo "  list             - 详细列出 inbox 内容"
    echo "  site             - 重新生成 wiki/site/ 静态网页视图"
    echo "  help             - 显示帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 all                        # 处理所有 inbox 文件"
    echo "  $0 file inbox/article.md      # 处理单个文件"
    echo "  $0 site                       # 刷新 HTML 网站"
    echo "  $0 list                       # 查看详细列表"
}

# 主入口
case "${1:-help}" in
    all)
        ingest_all
        ;;
    file)
        if [ -z "$2" ]; then
            echo "错误：缺少文件路径"
            show_help
            exit 1
        fi
        ingest_file "$2" "${3:-$RAW_EXTERNAL_DIR}"
        ;;
    list)
        list_inbox_detail
        ;;
    site)
        refresh_site
        ;;
    help|*)
        show_help
        ;;
esac
