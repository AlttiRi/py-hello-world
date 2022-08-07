from hello_world.command_line_args import trace


def get_text() -> str:
    if trace:
        print("[trace]: sub.util.pyl:get_text()")
    return "Hello World!"
