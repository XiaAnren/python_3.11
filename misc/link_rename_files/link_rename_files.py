import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

read_dir_path = '/public/home/XiaAnRen/20210515/wrfout_base/'
link_dir_path = '/public/home/XiaAnRen/20210515/expset_x105y95t0/ndown/'

with open('link_rename_file.sh', 'w') as file_sh:
    for file_name in os.listdir(read_dir_path):
        if file_name.startswith('wrfout_d02'):
            file_sh.write('ln -sf ' + read_dir_path + file_name + ' ' + link_dir_path + 'wrfout_d01' + file_name[10:] + '\n')
