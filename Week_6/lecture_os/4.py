import os

# os.getcwd() ==> return path to specific file or dir
base_url = os.getcwd()
print(base_url)

# os.chdir(path) ==> какую файл хочем открыть
os.chdir('dir1')
with open('new.txt','w') as f:
   f.write('new content\n')
   f.write('directed to path\n')

# for all in os.listdir(base_url):
#    print(all)

# os.path.join(path,*paths) - join two or more pathes into one general path separating by '\'
dir1_path = os.getcwd()
print(os.path.join(base_url,dir1_path))



