from env.hawker_env import HawkerEnv
from stable_baselines3 import PPO
import imageio
from utils.visualize import render_frame
from utils.kpi_dashboard import show_kpi_dashboard


def main():
    env = HawkerEnv()

    # Optional: Validate custom environment
    # from stable_baselines3.common.env_checker import check_env
    # check_env(env, warn=True)

    # Train the model
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=100_000)  # ⏱️ Train longer for better results

    # Save model
    model.save("ppo_hawker")

    # Evaluate and render live
    obs, _ = env.reset()
    for _ in range(100):
        action, _ = model.predict(obs)
        obs, reward, done, _, _ = env.step(action)
        env.render()
        if done:
            print(f"Episode done with reward {reward}")
            break

    # Save heatmap visualization
    env.render_heatmap("movement_heatmap.png")

    # Save rollout as MP4
    frames = []
    obs, _ = env.reset()
    for _ in range(100):
        action, _ = model.predict(obs)
        obs, reward, done, _, _ = env.step(action)
        frame = render_frame(env)
        frames.append(frame)
        if done:
            print(f"Episode done with reward {reward}")
            break

    # Save video with codec-friendly size
    imageio.mimsave("ppo_run.mp4", frames, fps=2)

    print("🎥 Video saved to ppo_run.mp4")
    print("📊 Heatmap saved to movement_heatmap.png")

    show_kpi_dashboard()

if __name__ == "__main__":
    main()
