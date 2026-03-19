import json
import pytest
from task_manager import TaskManager


def test_add_task_saves_task_to_file(tmp_path, capsys):
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    manager = TaskManager()

    manager.add_task("Tarea de prueba")

    captured = capsys.readouterr()
    assert "Tarea añadida" in captured.out

    with open(TaskManager.FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["id"] == 1
    assert data[0]["description"] == "Tarea de prueba"
    assert data[0]["completed"] is False


def test_complete_task_marks_completed_and_persists(tmp_path, capsys):
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    manager = TaskManager()
    manager.add_task("Tarea A")

    manager.complete_task(1)
    captured = capsys.readouterr()
    assert "Tarea completada" in captured.out

    assert manager._tasks[0].completed is True

    with open(TaskManager.FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data[0]["completed"] is True


def test_delete_task_removes_existing_task_and_updates_file(tmp_path, capsys):
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    manager = TaskManager()
    manager.add_task("Tarea 1")
    manager.add_task("Tarea 2")

    manager.delete_task(1)
    captured = capsys.readouterr()
    assert "Tarea eliminada" in captured.out

    assert len(manager._tasks) == 1
    assert manager._tasks[0].id == 2
    assert manager._tasks[0].description == "Tarea 2"

    with open(TaskManager.FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["id"] == 2


def test_delete_nonexistent_task_prints_message_and_keeps_tasks(tmp_path, capsys):
    TaskManager.FILENAME = str(tmp_path / "tasks.json")
    manager = TaskManager()
    manager.add_task("Tarea X")

    manager.delete_task(999)
    captured = capsys.readouterr()
    assert "Tarea no encontrada" in captured.out

    assert len(manager._tasks) == 1
    assert manager._tasks[0].id == 1

    with open(TaskManager.FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
