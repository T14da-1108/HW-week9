def count_util(text: str, flags: str | None = None) -> dict[str, int]:
    if not flags:
        flags = "-m -l -L -w"

    active_flags = set(flags.replace("-", "").replace(" ", ""))
    result = {}

    lines = text.splitlines()

    if "l" in active_flags:
        result["lines"] = len(lines) if text else 0

    if "m" in active_flags:
        result["chars"] = len(text)

    if "w" in active_flags:
        result["words"] = sum(len(line.split()) for line in lines)

    if "L" in active_flags:
        result["longest_line"] = max((len(line) for line in lines), default=0)

    return result

