
def debug_breakpoint():
    """
    Python debug breakpoint.

    Python script stopes here and gives back controll to the user.
    All variables and namespaces stay intacted for debugging.
    """
    from code import InteractiveConsole
    from inspect import currentframe
    try:
        import readline # noqa
    except ImportError:
        pass

    caller = currentframe().f_back

    env = {}
    env.update(caller.f_globals)
    env.update(caller.f_locals)

    shell = InteractiveConsole(env)
    shell.interact(
        '* Break: {} ::: Line {}\n'
        '* Continue with Ctrl+D or raise SystemExit...'.format(
            caller.f_code.co_filename, caller.f_lineno
        )
    )
