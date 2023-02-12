"""Helper methods for controllers and models."""
from __future__ import annotations

import logging
import traceback
import uuid
from datetime import date, datetime
from typing import Any, Dict, Text

from app.common.constants import iso_format
from flask_restful import abort


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.strftime(iso_format)
    if isinstance(obj, uuid.UUID):
        return str(obj)
    return obj


# Validators


def validate_input(schema, json_data: Dict[Text, Any]) -> Dict[Text, Any]:
    """Verifies JSON input in an endpoint against its schema."""
    data = None
    try:
        data = schema.load(json_data)
    except Exception as e:
        abort(400, message=str(e))
    return data


def create_logger():
    """Creates a standard logger"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    log_format = (
        "%(asctime)s-14s | %(levelname)s | %(filename)s |"
        " %(lineno)s | %(message)s"
    )
    logging.basicConfig(format=log_format)

    # return the logger object
    return logger


def log_traceback(ex, ex_traceback=None):
    if ex_traceback is None:
        ex_traceback = ex.__traceback__
    tb_lines = [
        line.rstrip("\n")
        for line in traceback.format_exception(ex.__class__, ex, ex_traceback)
    ]
    logging.log(logging.ERROR, tb_lines)


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)
