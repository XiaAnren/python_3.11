import os

pid = os.getpid()
print(pid)
# os.system('kill -9 {}'.format(pid))

# ps uxa | grep .vscode-server | awk '{print $2}' | xargs kill -9
# !kill -9 $pid
