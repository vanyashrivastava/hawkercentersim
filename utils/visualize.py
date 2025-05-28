from PIL import Image, ImageDraw, ImageFont
import numpy as np

def render_frame(env):
    grid = np.full(env.grid_size[::-1], ".", dtype=str)

    for name, pos in env.locations.items():
        x, y = pos
        grid[y, x] = (
            "F" if name == "fridge"
            else "C" if name == "cutting"
            else "S" if name == "stove"
            else "X"
        )

    ax, ay = env.agent_pos
    grid[ay, ax] = "A"

    # Create image (simple colored blocks)
    cell_size = 32
    img = Image.new("RGB", (cell_size * env.grid_size[0], cell_size * env.grid_size[1]), "white")
    draw = ImageDraw.Draw(img)

    for y in range(env.grid_size[1]):
        for x in range(env.grid_size[0]):
            left = x * cell_size
            top = y * cell_size
            char = grid[y, x]

            color = {
                ".": (220, 220, 220),
                "F": (100, 180, 255),
                "C": (255, 215, 0),
                "S": (255, 100, 100),
                "X": (100, 255, 100),
                "A": (0, 0, 0),
            }.get(char, (200, 200, 200))

            draw.rectangle([left, top, left + cell_size, top + cell_size], fill=color, outline="black")
            draw.text((left + 12, top + 10), char, fill="white" if char != "." else "black")

    return np.array(img)
