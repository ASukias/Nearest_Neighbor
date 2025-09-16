UPS Routing Project

## Overview
This project implements a routing program for WGUPS (Western Governors University Parcel Service) as part of the Data Structures and Algorithms II course. It focuses on solving the package delivery optimization problem by designing efficient algorithms and data structures that handle the complexity of multiple packages, time constraints, and dynamic conditions such as address corrections.

## Project Scope
- Design and implement a routing algorithm to deliver packages on time while minimizing total travel distance.
- Utilize advanced data structures to efficiently store, retrieve, and update package information.
- Demonstrate understanding of algorithmic complexity, scalability, and software maintainability.
- Provide a command-line user interface to interact and monitor package statuses dynamically during delivery.

## Key Components and Technical Summary

### Algorithm Selection
- **Nearest Neighbor Greedy Algorithm** is employed as the core routing heuristic. This self-adjusting algorithm incrementally builds the delivery route by always selecting the nearest unvisited package destination.
- The algorithm’s time complexity is \(O(n^2)\), where \(n\) is the number of packages, balancing performance with solution quality.
- Alternatives explored include the Cheapest Insertion and 2-Opt algorithms, offering different trade-offs between computational cost and route optimization.

### Data Structures
- A **Hash Table** is the primary data structure used to store and manage package data, keyed by unique Package IDs. This supports constant-time average complexity for insertion, lookup, and update operations.
- The hash table supports dynamic resizing and collision handling mechanisms, maintaining efficiency as package volume scales.
- Distance data is stored in a **distance matrix** (2D array), enabling constant-time distance retrieval between delivery points.
- Additional considerations include alternative structures like graphs (for complex route relationships) and priority queues (for ordered package processing).

### Code Architecture
- Modular design separates concerns into package management, route calculation, time tracking, and user interface components.
- Inline documentation and comments provide clarity of logic and flow control.
- Development environment included PyCharm IDE with Python 3.11 running on macOS hardware.

### Space-Time Complexity
- Nearest Neighbor Algorithm: \(O(n^2)\) time and \(O(n)\) space complexity.
- Hash Table operations average \(O(1)\) time but may degrade to \(O(n)\) in worst-case collisions.
- Distance matrix consumes \(O(m^2)\) space where \(m\) is the number of addresses.
- The overall system is designed to balance efficient runtime with maintainability and extensibility.

### Scalability and Adaptability
- The hash table easily accommodates growing package counts with dynamic rehashing.
- Distance matrix scales quadratically; suitable for moderate location counts but may require optimization for very large systems.
- Nearest Neighbor’s incremental route building supports on-the-fly adjustments such as address corrections (e.g., delayed update of package #9).
- The system design anticipates enhanced algorithms or data structures to improve optimization as dataset sizes increase.

### User Interface
- A command-line interface allows users to input specific query times and obtain package delivery status snapshots (en route, delivered, at the hub).
- Designed for ease of use, providing real-time feedback and enabling verification of delivery simulation requirements.

### Verification & Results
- The implemented route respects all delivery deadlines, including special constraints such as package grouping and delayed address updates.
- The total combined mileage meets the optimality threshold (<145 miles).
- Multiple status checks and execution screenshots verify correct and timely package delivery.

## How to Use
1. Load package data and distance matrices from CSV files.
2. Execute the routing algorithm to generate optimal delivery routes.
3. Use the interactive menu to query package statuses at any time during the delivery simulation.
4. Review logs or output for delivery timelines and route distances.

## Skills Demonstrated
- Advanced algorithmic problem solving using greedy and heuristic methods.
- Practical implementation of hash tables and matrix data structures.
- Application of Big O notation for analyzing and optimizing algorithm efficiency.
- Software engineering principles: modularity, maintainability, and professional documentation.
- Handling of real-world complexities, including dynamic updates and multi-constraint routing.

---

This repository showcases a thorough academic-to-practical bridge, highlighting both the theoretical grounding and hands-on mastery of critical Computer Science concepts in routing optimization and data management.
