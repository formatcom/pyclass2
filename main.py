# make class Example

# step 1
class_dict_example = {}

# step 2
class_body_example = '''
def __init__(self):
    print("call __init__")
def info(self):
    print("method info")
'''

# step 3
exec(class_body_example, globals(), class_dict_example)

# step 4
Example = type('Example', (object,), class_dict_example)

o = Example()
o.info()
