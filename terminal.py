def log(log_tag: str, any):
    if(log_tag == ""):
        raise Exception("Invalid log_tag in log()")
    print(log_tag + " : " + any)