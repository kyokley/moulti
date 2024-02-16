from typing import Any
from textual.app import ComposeResult
from textual.widgets import Button, Static
from ..abstractquestion.tui import AbstractQuestion

DEFAULT_BUTTONS = [
	['yes', 'success', 'Yes'],
	['no', 'error', 'No'],
	['cancel', 'primary', 'Cancel'],
]

class ButtonQuestion(AbstractQuestion):
	"""
	This widget represents an interactive question in a script, program or process.
	"""
	def __init__(self, id: str, **kwargs: Any): # pylint: disable=redefined-builtin
		super().__init__(id='step_' + id, **kwargs)
		self.buttons = []
		for value, classes, label in self.init_kwargs.get('button', DEFAULT_BUTTONS):
			self.buttons.append(Button(label, variant=classes, name=value))

	def compose_question(self) -> ComposeResult:
		with Static(classes='buttons'):
			yield from self.buttons

	def on_button_pressed(self, event: Button.Pressed) -> None:
		answer = event.button.name
		if answer is not None:
			self.got_answer(answer)

	DEFAULT_CSS = """
		Static.buttons {
			layout: horizontal;
			align: center middle;
			& Button { margin-right: 2; margin-left: 2; margin-top: 1; margin-bottom: 1; }
			max-height: 5;
		}
	"""
MoultiWidgetClass = ButtonQuestion