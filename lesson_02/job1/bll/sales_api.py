from lesson_02.job1.dal import local_disk, sales_api


def save_sales_to_local_disk(date: str, raw_dir: str, auth_token: str) -> None:
    """
    Get data from sales API for specified date and save it to disk.

    :param date:  data retrieve the data from
    :param raw_dir: path to target dir
    :param auth_token: authorisation token
    """

    json_content = sales_api.get_sales(date=date, auth_token=auth_token)
    local_disk.save_to_disk(json_content=json_content, path=raw_dir)
