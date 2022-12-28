from lesson_02.job2.dal import local_disk


def convert_sales_json_to_avro_save_local_disk(raw_dir: str, stg_dir: str) -> None:
    """
    Get data from sales API for specified date and save it to disk.

    :param raw_dir: path to source dir
    :param stg_dir: path to target dir
    """

    json_content = local_disk.open_from_disk(path=raw_dir)
    local_disk.save_to_disk(json_content=json_content, path=stg_dir)
