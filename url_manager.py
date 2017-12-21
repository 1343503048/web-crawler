class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, root_url):
        if root_url is None:
            return
        if root_url in self.new_urls:
            return
        if root_url in self.old_urls:
            return
        self.new_urls.add(root_url)

    def has_new_url(self):
        if len(self.new_urls) == 0:
            return 0
        else:
            return 1

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)
