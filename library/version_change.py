#!/usr/bin/python

DOCUMENTATION = '''
---
module: version_change
short_description: bump semantic version numbers
'''
EXAMPLES = '''
- hosts: localhost

  tasks:
  - name: Test that my module works
    version_change: 
      version_name: "Before"
      version_no:  1.1.1 
      unchanged_value: "This will pass through"
    register: result

  - debug: var=result    
'''


from ansible.module_utils.basic import *

def main():

    fields = {
        "version_no": {"default": True, "type": "str"},
        "version_name": {"default": True, "type": "str"},
        "unchanged_value": {"default": True, "type": "str"}
    } # values passed from variables in yml to dictionary

    module = AnsibleModule(argument_spec=fields) #fields dictionary passed here
    # change the name
    module.params.update({"version_name": "After"}) # Updating value in dictionary
    # bump minor and patch version
    mylist = module.params["version_no"].split('.') # splitting values after version_no
    mylist[2] = str(int(mylist[2]) + 2) # list manipulation
    mylist[1] = str(int(mylist[1]) + 1) # list manipulation
    mystr= '.'.join(mylist) # rejoined in new variable 
    module.params.update({"version_no": mystr}) # updated dict key value with variable

    
    module.exit_json(changed=True, meta=module.params) # value is returned to command line


if __name__ == '__main__':
    main()