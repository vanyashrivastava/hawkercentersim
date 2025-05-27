````markdown
# HawkerBotSim 🍜🤖  
**Optimizing Space and Efficiency in Hawker Kitchens Using RoboSuite + Reinforcement Learning**

This project simulates a human avatar working in a typical Singaporean hawker center to optimize food preparation within an extremely confined kitchen layout (10–13 square meters). By using reinforcement learning in `robosuite`, we train agents to complete food-serving tasks and visualize operational efficiency through a KPI dashboard and movement heatmaps.

## 🔧 How It Works

1. **Environment Setup:**  
   A custom environment simulates a typical hawker kitchen using `robosuite`. The avatar performs tasks like moving, picking, placing, and serving food.

2. **Training with RL:**  
   Reinforcement learning agents are trained to minimize movement inefficiencies and delays in serving food.

3. **KPI Dashboard Output:**  
   After training, the simulation outputs:
   - Movement heatmaps
   - Task delay statistics
   - Optimized layout suggestions via metrics (time to serve, idle time, etc.)
   - An optional video output of the agent’s movement

---

## ▶️ Getting Started

### 1. Clone this Repository
```bash
git clone https://github.com/YOUR_USERNAME/HawkerBotSim.git
cd HawkerBotSim
````

### 2. Install Requirements

Make sure you have Python 3.8+ and the following packages installed:

```bash
pip install -r requirements.txt
```

Requirements include:

* `robosuite`
* `numpy`
* `matplotlib`
* `imageio`
* `seaborn`
* `pandas`

### 3. Run the Simulation

```bash
python run_simulation.py
```

This script trains an agent and visualizes the results.

### 4. Generate KPI Dashboard

```bash
python kpi_dashboard.py
```

This script will generate performance visualizations and movement heatmaps.

### 5. (Optional) Create Video

To generate an .mp4 of the agent’s movement:

```bash
python create_video.py
```

---

## 📈 Output Examples

* Movement heatmaps
* Task duration per episode
* Cumulative reward over time
* Video walkthrough of the simulation

---

## 🙏 Credits

* Developed by \Vanya Shrivastava after a research visit to Singapore’s hawker centers with **USC Marshall**.
* AI simulation and code assistance provided by **ChatGPT-4** (OpenAI, 2025).
* Simulation powered by `robosuite` from **Stanford Vision and Learning Lab**.

> This tool is designed to **enhance**, not replace, the authenticity and human creativity of handmade food. It helps stall owners experiment with layout and strategy without the cost of trial-and-error in real life.

---

## 📬 Contact

For inquiries, collaborations, or licensing, reach out to: \[[vanyashr@usc.edu](mailto:vanyashr@usc.edu)]

---
