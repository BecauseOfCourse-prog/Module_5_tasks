import os

# os.mkdir("Управление_файлами")
os.chdir(r"C:\Users\User\PycharmProjects\Module_5_tasks\Управление_файлами")
files_and_dirs = os.listdir(".")
print("Файлы и директории:", files_and_dirs)

os.remove("file1.txt")
os.mkdir("Поддиректория")
os.replace(r"file2.txt", r"Поддиректория\file2.txt")
os.chdir(r"C:\Users\User\PycharmProjects\Module_5_tasks")
os.remove("Управление_файлами/Поддиректория/file2.txt")
os.removedirs("Управление_файлами/Поддиректория")
os.rmdir("Управление_файлами")