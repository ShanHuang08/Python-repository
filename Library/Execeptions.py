class SMCError(Exception):
    """Raise for `SMCIPMITool Error` exceptions"""    

class TestError(Exception):
    """Raise for `TestError` exceptions""" 

class TestError2(AssertionError):
    """Raise for `TestError2` test failed"""   