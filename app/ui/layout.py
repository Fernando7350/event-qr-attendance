"""Tema visual, cabecera y contenedor principal de EventQR."""
from collections.abc import Iterator
from contextlib import contextmanager

from nicegui import ui

from app.core.config import settings


@contextmanager
def page_layout(head_html: str = "") -> Iterator[None]:
    """Aplica el tema, el encabezado y el contenedor centrado de la aplicación."""
    if head_html:
        ui.add_head_html(head_html)
    ui.colors(primary="#4338ca")

    with ui.header().classes("items-center gap-3 px-6 py-3 shadow-md"):
        ui.icon("qr_code_2", size="32px")
        ui.label(settings.APP_TITLE).classes("text-h6 text-weight-bold")
        ui.label("Control de asistencia y registro de eventos").classes(
            "text-caption opacity-80"
        )

    with ui.column().classes("w-full max-w-6xl mx-auto p-4 gap-4"):
        yield