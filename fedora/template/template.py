class OERTemplate(object):

    @abstractmethod
    def content(content_container):
        pass

    """ Parse JSON content and parse as OERDataModle """
    @abstractmethod
    def parse(self, json_content=None):
        pass

