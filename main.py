import os
import shutil
from pathlib import Path

# 定义分类规则：扩展名 -> 文件夹名
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.md'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Installers': ['.exe', '.msi', '.dmg', '.apk'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp']
}

def organize_files(target_dir: str):
    """整理指定目录下的文件"""
    source_path = Path(target_dir)
    
    if not source_path.exists():
        print(f"❌ 错误：路径 {target_dir} 不存在！")
        return

    print(f"🚀 开始整理文件夹: {target_dir} ...")
    
    # 遍历目录下的所有项目
    for item in source_path.iterdir():
        # 只处理文件，跳过文件夹
        if item.is_file():
            suffix = item.suffix.lower()
            moved = False
            
            # 检查文件类型并移动
            for category, extensions in FILE_CATEGORIES.items():
                if suffix in extensions:
                    # 创建目标文件夹（如果不存在）
                    dest_dir = source_path / category
                    dest_dir.mkdir(exist_ok=True)
                    
                    # 移动文件
                    try:
                        shutil.move(str(item), str(dest_dir / item.name))
                        print(f"✅ 已移动: {item.name} -> {category}/")
                        moved = True
                        break
                    except Exception as e:
                        print(f"⚠️ 移动 {item.name} 失败: {e}")
            
            if not moved:
                print(f"⏭️ 跳过未知类型文件: {item.name}")

    print("✨ 整理完成！")

if __name__ == "__main__":
    # ⚠️ 注意：这里默认整理当前脚本所在的文件夹
    # 你可以修改为具体路径，例如: r"D:\Users\你的用户名\Downloads"
    target = os.path.dirname(os.path.abspath(__file__))
    
    print(f"当前目标路径: {target}")
    confirm = input("确定要开始整理吗？(y/n): ")
    
    if confirm.lower() == 'y':
        organize_files(target)
    else:
        print("已取消。")
