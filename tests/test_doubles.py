import sys


class TestPairs(object):
    """
    Instantiating an object of the TestPairs class will swap in the test
    double version of that module or class. Deleting that object will deactivate
    the test pairs.
    """
    old_objects = []

    def __init__(self, module=None, **test_doubles):
        if module is None:
            modules = sys.modules.values()
        else:
            modules = [module]
        self.old_objects = []
        for object_name in test_doubles:
            for mod_to_patch in modules:
                if mod_to_patch is not None:
                    if hasattr(mod_to_patch, object_name):
                        old_object = getattr(mod_to_patch, object_name)
                    else:
                        old_object = None
                    self.old_objects.append((mod_to_patch,
                                             object_name, old_object))
                    # The object_name will be changed/added in all modules.
                    # So it is not only stubbed in modules which already have
                    setattr(mod_to_patch, object_name, test_doubles[object_name])

    def exit(self):
        """
        De-activate the test doubles and re-instate the original objects.
        """
        self.old_objects.reverse()
        for module, object_name, old_object in self.old_objects:
            if hasattr(old_object, 'reset_method_attributes'):
                if callable(old_object.reset_method_attributes):
                    old_object.reset_method_attributes()

            setattr(module, object_name, old_object)
        self.old_objects = []

    def __del__(self):
        self.exit()

    def __enter__(self):
        """
        Dummy function needed for the context manager. It's dummy because
        the test doubles are already activated when the TestDouble object is
        instantiated.
        """
        return self

    def __exit__(self, type_, value, traceback):
        self.exit()
        return False
