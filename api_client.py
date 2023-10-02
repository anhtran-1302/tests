import requests


def post_template(api_url, headers, text, group_ids):
    return requests.post(
        f"{api_url}/templates",
        headers=headers,
        json={"text": text, "group_ids": group_ids},
    )


def post_group(api_url, headers, name):
    return requests.post(
        f"{api_url}/templates/groups", headers=headers, json={"name": name}
    )


def get_template(api_url, headers, template_id, group_ids):
    return requests.get(
        f"{api_url}/templates",
        headers=headers,
        params={"id": template_id, "group_ids": group_ids},
    )


def get_group(api_url, headers, group_id, group_name):
    return requests.get(
        f"{api_url}/templates/groups",
        headers=headers,
        headers={"Content-Type": "application/json"},
        params={"id": group_id, "name": group_name},
    )


def update_group(api_url, headers, group_id, group_name):
    return requests.put(
        f"{api_url}/templates/groups/{group_id}",
        headers=headers,
        json={"name": group_name},
    )


def update_template(api_url, headers, template_id, text, group_ids):
    return requests.post(
        f"{api_url}/templates/{template_id}",
        headers=headers,
        json={"text": text, "group_ids": group_ids},
    )
