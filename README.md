# Building Asteroids using Python and Pygame

Build a clone of the classic Asteroids game using Pygame and object-oriented programming concepts.

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Roshani-Udupa/asteroids-game.git
cd asteroids-game
```

### 2. Create and Activate Virtual Environment (optional but recommended)

If you don’t already have a virtual environment:

```bash
uv venv
```

Activate it:

* **Windows:**

  ```bash
  .venv\Scripts\activate
  ```
* **macOS/Linux:**

  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

All dependencies are managed by **uv**. Simply run:

```bash
uv sync
```

### 4. Run the Game

Launch the game using:

```bash
uv run main.py
```

## Controls

* **W** : Move Forward
* **S** : Move Backward
* **A** : Rotate Left
* **D** : Rotate Right
* **Spacebar** : Shoot


## Requirements

* Python 3.10+
* UV package manager