from scrape_members import sample_telegram_member_count
from scrape_links import get_telegram_links

import threading
from time import sleep
import schedule
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    def run_threaded(job_func):
        job_thread = threading.Thread(target=job_func)
        job_thread.start()

    schedule.every().day.at('00:30').do(run_threaded, get_telegram_links)
    schedule.every().day.at('12:30').do(run_threaded, get_telegram_links)
    schedule.every().day.at('15:15').do(run_threaded, sample_telegram_member_count)  # debug

    for idx in range(24):
        time = '{:02d}:00'.format(idx)
        schedule.every().day.at(time).do(run_threaded, sample_telegram_member_count)

    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    main()
