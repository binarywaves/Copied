__version__ = '2.5.0'

# Required to distribute different parts of this
# package as multiple distributables
try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
