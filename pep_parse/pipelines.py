import csv
import datetime
from pathlib import Path
from collections import defaultdict

from pep_parse.constants import RESULTS_DIR

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        status = item.get('status')
        if status:
            self.status_counts[status] += 1
        return item

    def close_spider(self, spider):
        now = datetime.datetime.now()
        time_str = now.strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{time_str}.csv'

        filepath = self.results_dir / filename

        total_peps = sum(self.status_counts.values())

        with open(filepath, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(['Статус', 'Количество'])

            for status, count in self.status_counts.items():
                writer.writerow([status, count])

            writer.writerow(['Total', total_peps])
