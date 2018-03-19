"""
Implementation of garage door openering using dictionary of state transitions functions
and action functions.
"""
from collections import namedtuple
from enum import Enum, auto


# The motor actions are modeled as an enum
class MotorAction(Enum):
    OFF = auto()
    DOWN = auto()
    UP = auto()


# Model inputs as a named tuple
Input = namedtuple('Input', ['open_button', 'close_button', 'limit_switch_open', 'limit_switch_closed'])


# States are represented as strings (they could also be enums)
state_transitions = {
    'closed': lambda input: 'opening' if input.open_button else 'closed',
    'open': lambda input: 'closing' if input.close_button else 'open',
    'opening': lambda input: 'open' if input.limit_switch_open else (
                                'closing' if input.close_button else 'opening'),
    'closing': lambda input: 'closed' if input.limit_switch_closed else (
                                'opening' if input.open_button else 'closing'),
    'error': lambda input: 'error'
}

# Action that are performed on every state on the outgoing edge.
motor_action_transitions = {
    'closed': lambda input:  MotorAction.UP if input.open_button else MotorAction.OFF,
    'open':  lambda input: MotorAction.DOWN if input.close_button else MotorAction.OFF,
    'opening': lambda input: MotorAction.OFF if input.limit_switch_open else (
        MotorAction.DOWN if input.close_button else MotorAction.UP),
    'closing': lambda input: MotorAction.OFF if input.limit_switch_closed else (
        MotorAction.UP if input.open_button else MotorAction.DOWN),
    'error': lambda input: MotorAction.OFF
}


def state_machine(current_state, input):
    """Determines action and next state.

    >>> state_machine('closed', Input(open_button=False, close_button=False, limit_switch_open=False, limit_switch_closed=False))
    MotorAction.OFF
    'closed'
    >>> state_machine('closed', Input(open_button=True, close_button=False, limit_switch_open=False, limit_switch_closed=False))
    MotorAction.UP
    'opening'
    >>> state_machine('closed', Input(open_button=False, close_button=True, limit_switch_open=False, limit_switch_closed=False))
    MotorAction.OFF
    'closed'
    >>> state_machine('opening', Input(open_button=False, close_button=False, limit_switch_open=True, limit_switch_closed=False))
    MotorAction.OFF
    'open'
    >>> state_machine('opening', Input(open_button=False, close_button=True, limit_switch_open=False, limit_switch_closed=False))
    MotorAction.DOWN
    'closing'
    >>> state_machine('opening', Input(open_button=False, close_button=False, limit_switch_open=False, limit_switch_closed=False))
    MotorAction.UP
    'opening'
    >>> state_machine('open', Input(open_button=False, close_button=True, limit_switch_open=False, limit_switch_closed=False))
    MotorAction.DOWN
    'closing'
    >>> state_machine('open', Input(open_button=False, close_button=False, limit_switch_open=False, limit_switch_closed=False))
    MotorAction.OFF
    'open'
    >>> state_machine('closing', Input(open_button=False, close_button=False, limit_switch_open=False, limit_switch_closed=True))
    MotorAction.OFF
    'closed'
    >>> state_machine('closing', Input(open_button=True, close_button=False, limit_switch_open=False, limit_switch_closed=False))
    MotorAction.UP
    'opening'
    >>> state_machine('closing', Input(open_button=False, close_button=False, limit_switch_open=False, limit_switch_closed=False))
    MotorAction.DOWN
    'closing'
    >>> state_machine('nonexistent', Input(open_button=False, close_button=False, limit_switch_open=False, limit_switch_closed=False))
    MotorAction.OFF
    'error'
    """
    next_state = state_transitions.get(current_state, lambda input: 'error')(input)
    action = motor_action_transitions.get(current_state, lambda input: MotorAction.OFF)(input)
    print(action)
    return next_state


if __name__ == '__main__':
    import doctest
    doctest.testmod()