# Project
This project is created to make an inventory of professors' profiles, including name, contact, PhD degree, 
and research interest.  

# files  

| file| function | 
|---- | ---- | 
| conf_loader.py | save params for crawlers and elastic-search |
| bs.py | parse html to get information of profs |
| `__main__.py` | save profs' information to local elastic-search |
| diy_search.ipynb | launch flexible search |

# prerequisites 
elastic-search 

> download a proper version from official website and run a client 

# deployment
```shell
pip install -r requirements.txt  
python3 __main__.py
```
