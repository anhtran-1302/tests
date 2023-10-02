from . import api_client, random_refs

headers = {"Content-Type": "application/json", "Authorization": "Bearer ***"}
headers_get = {"Authorization": "Bearer ***"}


def test_happy_path_template(api_url):
    text = random_refs.random_text
    group_ids = random_refs.random_group_ids
    create_template_res = api_client.post_template(
        api_url, headers=headers, text=text, group_ids=group_ids
    )
    assert create_template_res.status_code == 201

    response_body = create_template_res.json()
    assert "id" in response_body
    assert "text" in response_body
    assert "group_ids" in response_body

    template_id = response_body["id"]
    group_id = response_body["group_ids"]

    get_template_res_by_id = api_client.get_template(
        api_url, headers=headers_get, template_id=template_id, group_ids=""
    )
    assert get_template_res_by_id.status_code == 200

    get_template_res_by_group_id = api_client.get_template(
        api_url, headers=headers_get, template_id="", group_ids=group_id
    )
    assert get_template_res_by_group_id.status_code == 200

    get_template_res_by_id_and_group_id = api_client.get_template(
        api_url, headers=headers_get, template_id=template_id, group_ids=group_id
    )
    assert get_template_res_by_id_and_group_id.status_code == 200

    new_text = random_refs.random_name
    new_group_ids = random_refs.random_group_ids

    update_template_res = api_client.update_template(
        api_url,
        headers=headers,
        template_id=template_id,
        text=new_text,
        group_ids=new_group_ids,
    )
    assert update_template_res.status_code == 201

    get_after_upadte = api_client.get_template(
        api_url, headers=headers_get, template_id=template_id, template_name=""
    )
    assert get_after_upadte.status_code == 200
    assert get_after_upadte.json() == [
        {"id": template_id, "name": new_text, "group_ids": new_group_ids}
    ]


def test_unhappy_path_template(api_url):
    non_existent_api = ""
    create_template_400 = api_client.get_template(
        api_url=api_url, headers=headers, template_id="", template_name=""
    )
    assert create_template_400.status_code == 400

    create_template_403 = api_client.get_template(
        api_url=api_url, headers={}, template_id="", template_name=""
    )
    assert create_template_403.status_code == 403

    create_template_404 = api_client.get_template(
        api_url=non_existent_api, headers=headers, template_id="", group_ids=""
    )
    assert create_template_404 == 404

    get_template_403 = api_client.get_template(
        api_url=api_url, headers={}, template_id="", template_name=""
    )
    assert get_template_403.status_code == 403

    update_template_403 = api_client.update_template(
        api_url=api_url, headers={}, template_id="", template_name=""
    )
    assert update_template_403.status_code == 403

    update_template_404 = api_client.update_template(
        api_url=non_existent_api, headers=headers, template_id="", template_name=""
    )
    assert update_template_404.status_code == 404
