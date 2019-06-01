def mstring(string):
    return string.replace("\\","\n")

def load(file_object):
    return_ = {}
    namespace = "NONE"
    namespace_vars = {}

    datas = file_object.readlines()
    datas = [x.split("#", 1)[0].strip() for x in datas] # Remove comments and strip whitespace
    datas = [x for x in datas if x] # removes  empty lines

    for data in datas:
        if len(data) > 0 and data[0] == ">":

            if namespace in return_.keys():
                return_[namespace] = {**return_[namespace], **namespace_vars} # Append namespace
            else:
                return_[namespace] = namespace_vars
            namespace = data[1:]
            namespace_vars = {}

        elif len(data) > 0:
            key,value = data.split("::", 1)
            namespace_vars[key] = mstring(value)

    if namespace in return_.keys():
        return_[namespace] = {**return_[namespace], **namespace_vars} # Append namespace
    else:
        return_[namespace] = namespace_vars

    return return_


if __name__ == "__main__":
    import sys
    i = open(sys.argv[1], "r")
    print(load(i))
    i.close()