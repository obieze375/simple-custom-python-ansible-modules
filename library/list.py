from ansible.module_utils.basic import *

def main():
    fields = {
        "hello": {"default": True, "type": "str"},
        "ourlist": {"default": True, "type": "list"}
    } # Dictionary contains values

    module = AnsibleModule(argument_spec=fields) # fields dictionary passed here
    # updating the vars
    module.params.update({"hello": "Hello World Now"}) # params.update() updates dictionary with new value
    new_list = [1,2,3,4,5,6] # new values
    module.params.update({"ourlist":new_list}) # values appended to dictionary
    
    module.exit_json(changed=True, meta= module.params) # values retuned to commandline

if __name__ == '__main__':
    main()