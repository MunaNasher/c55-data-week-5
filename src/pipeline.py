import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def get_config() -> dict:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("API_KEY is missing")

    output_dir = os.getenv("OUTPUT_DIR", "output")

    return {
        "api_key": api_key,
        "output_dir": output_dir,
    }


def fetch_data(api_key: str) -> list[dict]:
    return [
        {"id": 1, "name": "Muna", "city": "Amsterdam"},
        {"id": 2, "name": "Ali", "city": "Rotterdam"},
    ]


def save_results(records: list[dict], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / "results.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(f"{record}\n")

    logger.info("%s records written", len(records))


def run() -> None:
    config = get_config()

    logger.info("starting pipeline")

    records = fetch_data(config["api_key"])

    output_dir = Path(config["output_dir"])

    save_results(records, output_dir)

    logger.info("pipeline complete")


if __name__ == "__main__":
    run()