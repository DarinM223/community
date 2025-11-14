from talon import Context, Module, actions

mod = Module()
ctx = Context()

@ctx.action_class("user")
class UserActions:
    def noise_trigger_pop():
        actions.key("a")