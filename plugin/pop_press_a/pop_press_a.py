import time

from talon import Context, Module, actions, settings

ctx = Context()
mod = Module()

mod.tag("pop_press_a", desc="tag for enabling pop to press the a key")

ctx.matches = r"""
mode: command
and tag: user.pop_press_a
"""


@ctx.action_class("user")
class UserActions:
    def noise_trigger_pop():
        actions.key("a")
