from gym.envs.registration import register

register(
    id='mastermind-v0',
    entry_point='mastermind_env.envs:CodeBreaker_Machine_Env',
)