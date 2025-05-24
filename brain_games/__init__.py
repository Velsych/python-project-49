import brain_games.games.game_core as core
from brain_games.cli import welcome_user
from brain_games.games.games_logic import (
    module_calc,
    module_even,
    module_gcd,
    module_prime,
    module_progression,
)


__all__ = (
    "module_even",
    "core",
    "module_calc",
    "module_gcd",
    "module_progression",
    "module_prime",
    "welcome_user"
)   