def get_domain_name(url: str) -> str:
    process = ""

    if url.startswith("https://www."):
        process = url.split("https://www.")[1].split(".")[0]
    elif url.startswith("http://www."):
        process = url.split("http://www.")[1].split(".")[0]
    elif url.startswith("http://"):
        process = url.split("http://")[1].split(".")[0]
    elif url.startswith("https://"):
        process = url.split("https://")[1].split(".")[0]
    elif url.startswith("www."):
        process = url.split("www.")[1].split(".")[0]

    return(process)