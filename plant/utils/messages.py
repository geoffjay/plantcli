def info(message):
    return f"[bold]{message}[/bold]"


def warning(message):
    return f"[bold yellow]{message}[/bold yellow]"


def error(message):
    return f"[bold red]{message}[/bold red]"


def success(message):
    return f"[bold green]{message}[/bold green]"


highlight = info
