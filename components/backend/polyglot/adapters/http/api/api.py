from flask import Blueprint, jsonify, request

from polyglot.adapters.object_storage import ObjectStorage
from polyglot.application.application import TaskService
from polyglot.application.entities import TaskStatus


def create_api(
    bp_api: Blueprint,
    task_service: TaskService,
    object_storage: ObjectStorage,
):

    @bp_api.route("/upload-complete", methods=["POST"])
    def upload_complete():
        data = request.json
        task_id = data.get("task_id")
        result = task_service.set_task_status(task_id, TaskStatus.READY)
        if not result:
            return jsonify({"error": "task not found"}), 404
        return jsonify({"ok": True})

    @bp_api.route("/request-upload", methods=["POST"])
    def request_upload():
        data = request.json
        filename = data.get("filename")
        content_type = data.get("content_type", "application/octet-stream")
        task = task_service.create_task(filename)
        presigned_url = object_storage.generate_presigned_url(
            object_key=task.object_key,
            content_type=content_type,
        )
        return jsonify({"task_id": task.id, "upload_url": presigned_url})

    return bp_api
