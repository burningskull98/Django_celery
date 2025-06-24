from celery import shared_task
from enum import StrEnum


class ActionName(StrEnum):
    created = "Created"
    updated = "Updated"
    deleted = "Deleted"


@shared_task
def create_product(product_name: str, action_name: ActionName) -> str:
    return f'{action_name} product "{product_name}"'
