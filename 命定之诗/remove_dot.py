import sys
import os

def remove_trailing_dot(file_path):
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误: 找不到文件 '{file_path}'")
        return

    try:
        with open(file_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            
            # 逻辑：去除末尾的空白符（如换行）后，检查是否以句号结尾
            # rstrip() 用于临时检查，不会删除文件中间的内容
            if content.rstrip().endswith('.'):
                # 找到最后一个句号的位置
                last_dot_index = content.rfind('.')
                
                # 重组内容：保留句号前的部分 + 句号后的部分（如果有换行符的话）
                # 这样做可以保留文件末尾原本存在的换行符
                new_content = content[:last_dot_index] + content[last_dot_index+1:]
                
                #由于文件变短了，我们需要回退指针并截断文件
                f.seek(0)
                f.write(new_content)
                f.truncate()
                print(f"成功: 已删除 '{file_path}' 末尾的句号。")
            else:
                print(f"提示: '{file_path}' 的末尾没有句号，未做修改。")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python remove_dot.py <文件名>")
    else:
        remove_trailing_dot(sys.argv[1])