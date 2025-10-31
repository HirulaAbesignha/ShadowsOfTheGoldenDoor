# The Lost Key: Shadows of the Golden Door

## Story:
You are Alex, a curious adventurer who has ventured into the Ancient Labyrinth, a mysterious maze said to be filled with treasure and secrets. However, the maze is not just a place of riches – it's also a place of danger, with twisting corridors, hidden traps, and locked doors.

The only way out is through the Golden Door – but it is locked. To escape the maze, you must collect 3 Lost Keys hidden throughout the maze. Each key unlocks a new part of the labyrinth, and ultimately, the Golden Door will open, allowing you to escape.

As you navigate the maze, you will face:

Dangerous traps that can hurt you if you're not careful.
Locked doors that require keys to open.
Hidden secrets that will help you on your journey.
Will you find all the keys and escape the maze, or will you get lost forever?

Here is an 8 image Storyboard to illistrate a desired direction and end results for our game. This image is a placeholder and will be updated as the project proceeds. 

![image](https://github.com/user-attachments/assets/c9d56d78-1127-470f-8e84-2645333466bb)


## Setup Guide


This  will help to quickly set up the development environment using **Python**, **Pygame**, and a **virtual environment**.

---



## 🐍 Step 1: Install Python 3.x

### 🪟 Windows

1. Go to the [official Python website](https://www.python.org/downloads/).
2. Download the latest **Python 3.x** installer for Windows.
3. During installation, **check** the box that says:

   ```
   Add Python 3.x to PATH
   ```
4. Complete the installation.

Verify your installation:

```bash
python --version
```

Expected output:

```
Python 3.x.x
```

---

### 🍎 macOS

1. Open **Terminal**.
2. Install Python via Homebrew:

   ```bash
   brew install python
   ```
3. Verify:

   ```bash
   python3 --version
   ```

If you don’t have Homebrew, install it first from [brew.sh](https://brew.sh/).

---

### 🐧 Linux (Ubuntu/Debian)

1. Open your terminal.
2. Run:

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip -y
   ```
3. Verify installation:

   ```bash
   python3 --version
   ```

---

## 🎮 Step 2: Install Pygame

Once Python is installed, you can install Pygame using `pip`:

```bash
pip install pygame
```

> 💡 If `pip` doesn’t work, try:
>
> ```bash
> python -m pip install pygame
> ```
>
> or
>
> ```bash
> python3 -m pip install pygame
> ```

### ✅ Test Your Installation

Run:

```bash
python -m pygame.examples.aliens
```

If a small window opens with a game demo, your installation is successful!

---

## 🧩 Step 3: Set Up a Virtual Environment

A **virtual environment** keeps project dependencies separate from your global Python setup.

### Create the Environment

From your project directory:

```bash
python -m venv venv
```

### Activate It

* **Windows (CMD or PowerShell):**

  ```bash
  venv\Scripts\activate
  ```
* **macOS / Linux:**

  ```bash
  source venv/bin/activate
  ```

You should now see `(venv)` at the beginning of your terminal prompt — that means the environment is active.

### Deactivate

When you’re done:

```bash
deactivate
```

---

## 🧪 Step 4: Verify Your Setup (Optional)

To confirm everything works, run a simple Pygame test:

Create a file named `test_pygame.py` in your project folder:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Test")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
```

Run it:

```bash
python test_pygame.py
```

If a window opens and closes without errors, your setup is complete!

