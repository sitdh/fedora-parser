class OERTemplate(object):

    def content(content_container):
        raise NotImplementedError("Please implement this method")

    """ Parse JSON content and parse as OERDataModle """
    def parse(self, json_content=None):
        raise NotImplementedError("Please implement this method")
