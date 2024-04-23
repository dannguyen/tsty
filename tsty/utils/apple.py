import subprocess


def get_color_change_command(
    r: int, g: int, b: int, attribute: str = "background color"
) -> str:
    rx, gx, bx = [(c * 65535) // 255 if c > 0 else 0 for c in (r, g, b)]
    rgbvals = f"{{{rx}, {gx}, {bx}}}"

    app_text = '''tell application "Terminal"'''
    target_text = """window 1"""

    ocmd = f"""{app_text} to set {attribute} of {target_text} to {rgbvals}"""
    return ocmd


def run_command(cmd: str) -> None:
    subprocess.run(["osascript", "-e", cmd], text=True)
