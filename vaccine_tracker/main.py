from typing import List

from vaccine_tracker.aws import get_links, save_links
from vaccine_tracker.files import File, get_files
from vaccine_tracker.telegram import notify_text


def main():
    web_files = list(get_files())

    if not web_files:
        return

    current_links = get_links()

    files_to_notify: List[File] = []
    for file in web_files:
        if file.url not in current_links:
            files_to_notify.append(file)

    if not files_to_notify:
        return

    files_as_str = "\n".join([f"- [{x.title}]({x.url})" for x in files_to_notify])
    msg = "Nuevas convocatorias de la vacuna:\n" + files_as_str
    notify_text(msg)

    new_links = current_links + [x.url for x in files_to_notify]
    new_links.sort()
    save_links(new_links)
