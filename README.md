<img width="1542" height="1028" alt="image" src="https://github.com/user-attachments/assets/99f46bcb-ae38-4d84-991f-a778d26b463e" /><img width="1542" height="1028" alt="image" src="https://github.com/user-attachments/assets/4090266e-6426-40fa-97aa-6cc145cb9d8c" /># 🐢 Turtle Quest: Entity Navigation & AI System

A 2D top-down exploration engine built in Python using the `turtle` graphics library. This project showcases custom animation state machines, relative-motion camera systems, and intelligent "stale-tracking" enemy AI.

## 🚀 Key Features

* **Dynamic Animation Engine:** Implements a frame-mapped cycle (Stand-Left-Stand-Right) using a `curr_frame` pointer system to ensure smooth bipedal movement.
* **Inverse Camera Transformation:** A custom "Relative Motion" system that keeps NPCs and health bars locked to a scrolling world map by shifting them inversely to player movement.
* **Stale-Targeting Enemy AI:** Features a "Target Lock" system where enemies track the player's previous coordinates, reaching the old location before updating to the new one for realistic "hunting" behavior.
* **Hybrid Class Architecture:** Utilizes Python’s multiple inheritance to combine physical entity logic with a dynamic scaling health system.

## 🛠️ Technical Architecture

This project was built using Object-Oriented Programming (OOP) to handle complex game states efficiently:

### Class Hierarchy
* **`entity`**: The base class handling physics, movement flags, and the animation timer.
* **`health_system`**: Manages damage calculations and real-time health bar rendering.
* **`Character`**: The primary actor class inheriting from both `entity` and `health_system`.
* **`Enemy`**: A specialized class adding the `track_player` behavior and combat logic.

### Core Logic: The Animation Cycle
The walking cycle is handled via a 4-state counter system that eliminates "skipping" frames:
- **Frame 0 & 2:** Neutral/Standing
- **Frame 1:** Left Stride
- **Frame 3:** Right Stride

## 🎮 How to Run

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/smireku38/Turtle_Mayhem]
    ```

## ⌨️ Controls
* **WASD / Arrow Keys:** Movement
* **Auto-Track:** Enemies automatically calculate the path to your last known position.

---

### Project Context
Developed as a core technical project for the **UIC Computer Science Expo 2026**. This engine focuses on optimizing O(1) lookups for animations and maintaining high-performance game logic within the Turtle graphics framework.

<img width="1542" height="1028" alt="image" src="https://github.com/user-attachments/assets/f1460134-814a-41b0-a735-0b7588575bd2" />

