import requests
from urllib.parse import urlparse, parse_qs

def get_key_value(url, referer_url=None):
    ascii = '''
██╗  ██╗███████╗██╗   ██╗ ██████╗ ███████╗███╗   ██╗
██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝ ██╔════╝████╗  ██║
█████╔╝ █████╗   ╚████╔╝ ██║  ███╗█████╗  ██╔██╗ ██║
██╔═██╗ ██╔══╝    ╚██╔╝  ██║   ██║██╔══╝  ██║╚██╗██║
██║  ██╗███████╗   ██║   ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝
'''
    print(ascii)
    headers = {} 
    if referer_url:
        headers['Referer'] = referer_url 

    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 302:
            final_url = response.headers['Location']
            print("Final URL after redirect:", final_url)

            parsed_url = urlparse(final_url)
            query_params = parse_qs(parsed_url.query)

            if "key" in query_params:
                key_value = query_params["key"][0]
                return key_value
            else:
                return "The 'key' parameter was not found in the URL."

        elif response.status_code == 200:
            return "The URL did not redirect. No 'key' parameter found."

        else:
            return f"Failed to retrieve the page. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    url = "https://galaxyswapperv2.com/Key/Create.php"
    referer_url = "https://lootlinks.co/"
    key_value = get_key_value(url, referer_url)
    if key_value:
        print("The generated key is:", key_value)
    else:
        print("No 'key' parameter found in the URL.")