import matplotlib.pyplot as plt

from agents.neuromod_pong_agent import NeuromodPongAgent
from utils import get_env, prep_obs


ENV_STEP = 10


if __name__ == '__main__':

    env, input_size = get_env('Pong-v0')
    agent = NeuromodPongAgent(input_size=input_size,
                              pyr_synapse=100,
                              inh_synapse=100,
                              sim_step=10,
                              max_hz=100)

    action = 0
    for i in range(ENV_STEP):
        obs, reward, done, info = env.step(env.action_space.sample())
        obs = prep_obs(obs)

        if done or reward > 0:
            print('DONE:', reward, done)
            env.reset()

        action = agent.step(observation=obs, reward=reward)

    agent.retina_rec.plot()
    plt.show()

    env.close()
