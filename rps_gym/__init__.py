import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='RPS-v0',
    entry_point='rps_gym.envs:RPSEnv',
    max_episode_steps=1000,
)
