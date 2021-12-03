import concurrent.futures
from urllib.request import Request, urlopen
import cProfile


pr = cProfile.Profile()
pr.enable()

links = open('res.txt', encoding='utf8').read().split('\n')


def load_url(url):
    request = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    )
    return urlopen(request, timeout=5)


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    responds = {executor.submit(load_url, url): url for url in links}
    for respond in concurrent.futures.as_completed(responds):
        url = responds[respond]
        try:
            print(respond.result().code)
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))


pr.disable()
pr.print_stats(sort=1)