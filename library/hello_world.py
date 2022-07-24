#!/usr/bin/python

from ansible.module_utils.basic import *

def main():
    module = AnsibleModule(argument_spec={})
    response = {"hello": "world"} # dictionary value
    module.exit_json(changed=False, meta=response) # returns value to commandline

if __name__ == '__main__':
    main()