# KB Ops Scripts

知识库本地操作脚本，用于避免在文件操作上浪费 token。

## 脚本列表

### kb-scripts.sh

基础文件操作脚本：

```bash
# 列出 inbox 中的文件
./skills/kb-ops/scripts/kb-scripts.sh list

# 读取 inbox 中所有文件内容
./skills/kb-ops/scripts/kb-scripts.sh read

# 将 inbox 文件移动到 raw/external
./skills/kb-ops/scripts/kb-scripts.sh move

# 显示帮助
./skills/kb-ops/scripts/kb-scripts.sh help
```

### kb-ingest.sh

完整的摄取流程脚本：

```bash
# 摄取 inbox 中所有文件到 raw/external
./skills/kb-ops/scripts/kb-ingest.sh all

# 摄取单个文件
./skills/kb-ops/scripts/kb-ingest.sh file inbox/article.md

# 详细列出 inbox 内容（带行数和大小的统计）
./skills/kb-ops/scripts/kb-ingest.sh list

# 显示帮助
./skills/kb-ops/scripts/kb-ingest.sh help
```

## 使用场景

### 场景 1：快速查看 inbox 有什么
```bash
./skills/kb-ops/scripts/kb-ingest.sh list
```

### 场景 2：摄取所有 inbox 文件
```bash
./skills/kb-ops/scripts/kb-ingest.sh all
```

### 场景 3：移动文件后读取内容
```bash
# 先移动
./skills/kb-ops/scripts/kb-scripts.sh move

# 再读取（文件已在 raw/external/）
cat raw/external/*.md | head -100
```

## 为什么用脚本

1. **省 token** - 文件操作不需要消耗 LLM token
2. **成功率高** - 脚本处理文件名编码问题，避免 shell 转义错误
3. **可复用** - 一次编写，反复使用
4. **可观察** - 清晰的输出格式，方便快速理解状态

## 未来扩展

可以添加更多脚本：
- `kb-lint.sh` - 自动化 lint 检查
- `kb-search.sh` - 本地知识搜索
- `kb-sync.sh` - 同步多个仓库
