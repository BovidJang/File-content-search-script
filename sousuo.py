import os
import sys

def search_files(directory, search_string):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encodings = ['utf-8', 'gbk', 'latin-1']
            for enc in encodings:
                try:
                    with open(file_path, 'r', encoding=enc) as f:
                        for line_num, line in enumerate(f, 1):
                            if search_string in line:
                                print(f"文件路径: {file_path}")
                                print(f"行号: {line_num}")
                                print(f"内容: {line.strip()}\n{'-'*40}")
                    break  # 成功读取后跳出编码循环
                except UnicodeDecodeError:
                    continue  # 尝试下一个编码
                except Exception as e:
                    print(f"读取文件错误 {file_path}: {e}", file=sys.stderr)
                    break
            else:
                print(f"无法解码文件: {file_path} (已尝试编码: {', '.join(encodings)})", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python jiaoben.py <目录> <搜索字符串>")
        print("示例: python jiaoben.py yuanma index.php")
        sys.exit(1)
    
    target_dir = sys.argv[1]
    target_str = sys.argv[2]
    
    if not os.path.isdir(target_dir):
        print(f"错误: 目录不存在: {target_dir}", file=sys.stderr)
        sys.exit(1)
    
    print(f"正在扫描目录: {target_dir}")
    print(f"搜索目标字符串: {target_str}\n")
    search_files(target_dir, target_str)