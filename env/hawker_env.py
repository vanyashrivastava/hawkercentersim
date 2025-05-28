import gymnasium as gym
import numpy as np
from gymnasium import spaces
import matplotlib.pyplot as plt


class HawkerEnv(gym.Env):
    def __init__(self):
        super(HawkerEnv, self).__init__()

        self.grid_size = (4, 3)  # 4m x 3m kitchen (width, height)
        self.max_steps = 50

        self.agent_pos = [0, 0]
        self.steps_taken = 0

        # Object positions (x, y)
        self.locations = {
            "fridge": (0, 2),
            "cutting": (1, 2),
            "stove": (2, 2),
            "counter": (3, 1)
        }

        # Define actions: [UP, DOWN, LEFT, RIGHT, ACTION]
        self.action_space = spaces.Discrete(5)

        # Observation = flattened grid + task state
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(4 * 3 + 3,), dtype=np.float32
        )

        # Task state
        self.has_veg = False
        self.has_chopped = False
        self.has_cooked = False

        self.frying_steps_required = 3
        self.frying_steps_remaining = 0

        self.heatmap = np.zeros(self.grid_size[::-1], dtype=int)  # (height, width)

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)

        self.agent_pos = [0, 0]
        self.steps_taken = 0

        self.has_veg = False
        self.has_chopped = False
        self.has_cooked = False

        self.frying_steps_remaining = 0
        self.heatmap = np.zeros(self.grid_size[::-1], dtype=int)

        obs = self._get_obs()
        return obs, {}

    def step(self, action):
        self.steps_taken += 1

        # Movement
        x, y = self.agent_pos
        if action == 0 and y < self.grid_size[1] - 1:  # up
            self.agent_pos[1] += 1
        elif action == 1 and y > 0:  # down
            self.agent_pos[1] -= 1
        elif action == 2 and x > 0:  # left
            self.agent_pos[0] -= 1
        elif action == 3 and x < self.grid_size[0] - 1:  # right
            self.agent_pos[0] += 1
        elif action == 4:  # interact
            self._interact()

        # Clamp position to prevent out-of-bounds
        self.agent_pos[0] = max(0, min(self.agent_pos[0], self.grid_size[0] - 1))
        self.agent_pos[1] = max(0, min(self.agent_pos[1], self.grid_size[1] - 1))

        x, y = self.agent_pos

        if hasattr(self, "heatmap") and 0 <= y < self.grid_size[1] and 0 <= x < self.grid_size[0]:
            self.heatmap[y, x] += 1

        reward = 0
        done = False

        # Frying logic
        if self.has_chopped and (x, y) == self.locations["stove"]:
            if self.frying_steps_remaining == 0:
                self.frying_steps_remaining = self.frying_steps_required
            self.frying_steps_remaining -= 1
            if self.frying_steps_remaining == 0:
                self.has_cooked = True

        # Task complete
        if self.has_veg and self.has_chopped and self.has_cooked:
            if (x, y) == self.locations["counter"]:
                reward = 10
                done = True

        if self.steps_taken >= self.max_steps:
            done = True

        return self._get_obs(), reward, done, False, {}

    def _interact(self):
        pos = tuple(self.agent_pos)
        if pos == self.locations["fridge"]:
            self.has_veg = True
        elif pos == self.locations["cutting"] and self.has_veg:
            self.has_chopped = True
        elif pos == self.locations["stove"] and self.has_chopped:
            self.has_cooked = True  # This will get overwritten by frying delay logic

    def _get_obs(self):
        grid_obs = np.zeros(self.grid_size, dtype=np.float32).flatten()
        idx = self.agent_pos[1] * self.grid_size[0] + self.agent_pos[0]
        grid_obs[idx] = 1.0
        task_state = np.array(
            [float(self.has_veg), float(self.has_chopped), float(self.has_cooked)],
            dtype=np.float32,
        )
        return np.concatenate([grid_obs, task_state]).astype(np.float32)

    def render(self):
        grid = np.full(self.grid_size[::-1], " . ")
        for name, pos in self.locations.items():
            grid[pos[1], pos[0]] = (
                "F" if name == "fridge"
                else "C" if name == "cutting"
                else "S" if name == "stove"
                else "X"
            )
        grid[self.agent_pos[1], self.agent_pos[0]] = "A"
        print("\n".join([" ".join(row) for row in grid[::-1]]))

    def render_heatmap(self, save_path=None):
        plt.figure(figsize=(4, 3))
        plt.imshow(self.heatmap, cmap="hot", interpolation="nearest")
        plt.title("Movement Heatmap")
        plt.colorbar(label="Visits")
        plt.xticks(range(self.grid_size[0]))
        plt.yticks(range(self.grid_size[1]))
        plt.gca().invert_yaxis()
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
