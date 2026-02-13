from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo


def get_datetime() -> str:
    """ Return a local date/time string """
    dt = datetime.now(tz=ZoneInfo("Europe/London"))
    time_str = dt.strftime("%H:%M").lstrip("0")

    return f"{dt.strftime('%a, %d %b %Y')} at {time_str}"


def update_readme_top(text: str) -> None:
    """ Insert text at the top of readme.md """
    readme = Path(__file__).resolve().parent / "README.md"
    text_block = text.rstrip() + "\n\n"
    existing = readme.read_text(encoding="utf-8")
    new = text_block + existing.lstrip()
    readme.write_text(new, encoding="utf-8")


if __name__ == "__main__":

    time = get_datetime() 
    update_readme_top(time)