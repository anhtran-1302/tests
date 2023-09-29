from . import api_client, random_refs

headers= {
        "Content-Type": "application/json",
        "Authorization": "Bearer ***"
    } 
headers_get = {
        "Authorization": "Bearer ***"
}
def test_happy_path_group(api_url):
    name = random_refs.random_name()
    create_group_res = api_client.get_group(api_url, headers= headers, group_name= name)
    assert create_group_res.status_code == 201

    response_body = create_group_res.json()
    assert "id" in response_body
    assert "name" in response_body
    
    group_id = response_body["id"]
    group_name = response_body["name"]

    get_group_res_by_id = api_client.get_group(api_url, headers= headers_get, group_id=group_id, group_name= "")
    assert get_group_res_by_id.status_code == 200

    get_group_res_by_name = api_client.get_group(api_url, headers= headers_get, group_id="", group_name= group_name)
    assert get_group_res_by_name.status_code == 200

    get_group_res_by_id_and_name = api_client.get_group(api_url, headers = headers_get, group_id=group_id, group_name= group_name)
    assert get_group_res_by_id_and_name.status_code == 200

    new_group_name = random_refs.random_name

    update_group_res = api_client.update_group(api_url, headers= headers, group_id= group_id, group_name= new_group_name)
    assert update_group_res.status_code == 201

    get_after_upadte = api_client.get_group(api_url, headers= headers_get, group_id=group_id, group_name= "")
    assert get_after_upadte.status_code == 200
    assert get_after_upadte.json() == [
	{
        "id" : group_id,
	    "name" : new_group_name
    }
    ]
    
def test_unhappy_path_group(api_url):
    create_group_400 = api_client.get_group(api_url= api_url, headers= headers, group_id= "", group_name="")
    assert create_group_400.status_code == 400

    create_group_403 = api_client.get_group(api_url= api_url, headers= {}, group_id= "", group_name="")
    assert create_group_403.status_code == 403

    get_group_403 = api_client.get_group(api_url=api_url, headers={}, group_id="", group_name="")
    assert get_group_403.status_code == 403

    update_group_400 = api_client.update_group(api_url=api_url, headers=headers, group_id="", group_id="")
    assert update_group_400 == 400

    update_group_403 = api_client.update_group(api_url=api_url, headers={}, group_id="", group_name="")
    assert update_group_403.status_code == 403

    update_group_404 = api_client.update_group(api_url="", headers=headers, group_id="", group_name="")
    assert update_group_404.status_code == 404