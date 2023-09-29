import uuid

def random_text():
    return f"text_{uuid.uuid4().hex}"

def random_group_ids():
    return f"[id_{uuid.uuid4().hex}]" 

def random_name():
    return f"name_{uuid.uuid4().hex}"