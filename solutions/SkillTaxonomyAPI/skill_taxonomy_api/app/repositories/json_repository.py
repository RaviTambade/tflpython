import json
from pathlib import Path
from typing import Any


DATA_DIRECTORY = Path(__file__).resolve().parents[2] / "data"


class JsonRepository:
    def __init__(self, filename: str):
        self.path = DATA_DIRECTORY / filename

    def list(self) -> list[dict[str, Any]]:
        with self.path.open(encoding="utf-8") as data_file:
            records = json.load(data_file)
        if not isinstance(records, list):
            raise ValueError(f"Expected a JSON array in {self.path.name}")
        return records

    def get(self, record_id: str) -> dict[str, Any] | None:
        return next((record for record in self.list() if record["id"] == record_id), None)

    def create(self, record: dict[str, Any]) -> dict[str, Any]:
        records = self.list()
        records.append(record)
        self._write(records)
        return record

    def update(self, record_id: str, record: dict[str, Any]) -> dict[str, Any]:
        records = self.list()
        for index, current in enumerate(records):
            if current["id"] == record_id:
                records[index] = record
                self._write(records)
                return record
        raise KeyError(record_id)

    def delete(self, record_id: str) -> bool:
        records = self.list()
        remaining = [record for record in records if record["id"] != record_id]
        if len(remaining) == len(records):
            return False
        self._write(remaining)
        return True

    def _write(self, records: list[dict[str, Any]]) -> None:
        temporary_path = self.path.with_suffix(f"{self.path.suffix}.tmp")
        with temporary_path.open("w", encoding="utf-8") as data_file:
            json.dump(records, data_file, indent=2, ensure_ascii=False)
            data_file.write("\n")
        temporary_path.replace(self.path)