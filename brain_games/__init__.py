# from brain_games.cli import welcome_user больше не используем
import brain_games.logic.game_logic as logic
from brain_games.logic.games_logic.module import user_greet
from brain_games.logic.games_logic.module_calc import calc_games
from brain_games.logic.games_logic.module_even import even_games

__all__ = (
    "user_greet",
    "even_games",
    "logic",
    "calc_games"
)   