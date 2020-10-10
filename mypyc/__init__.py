def load_ipython_extension(ip):
    """Load the extension in IPython via %load_ext mypyc."""
    from .ipython_magic_command import MypycMagics
    ip.register_magics(MypycMagics)
